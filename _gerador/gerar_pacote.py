# -*- coding: utf-8 -*-
"""Monta a pasta (e o .zip) pronta para subir na hospedagem.

Copia só o que o site publicado usa — rastreado a partir das páginas — e
não altera nenhum arquivo do projeto. Diferente do build.py, é seguro rodar.

Uso:
  python3 _gerador/gerar_pacote.py
  python3 _gerador/gerar_pacote.py --dominio https://www.seudominio.com.br
  python3 _gerador/gerar_pacote.py --dominio https://... --planilha https://script.google.com/macros/s/.../exec

Saída (ao lado da pasta do projeto):
  SITE-EVOLVE-UPLOAD/       -> conteúdo a colocar dentro de public_html (ou www)
  SITE-EVOLVE-UPLOAD.zip    -> o mesmo, compactado, para "Extrair" no gerenciador de arquivos
"""
import argparse, io, os, re, shutil, zipfile
from urllib.parse import unquote, urlsplit

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAIDA = os.path.join(os.path.dirname(RAIZ), "SITE-EVOLVE-UPLOAD")
BASE_ATUAL = "https://evolvecapitalhumano.com.br"
ENTRADAS = ["index.html", "404.html", "comece-aqui.html", "robots.txt", "sitemap.xml",
            "site.webmanifest", "llms.txt", "favicon.ico"]
TEXTO = (".html", ".css", ".js", ".webmanifest", ".xml", ".txt")
REF = re.compile(
    r"""(?:src|href|poster|content|data-[\w-]+)\s*=\s*["']([^"']+)["']"""
    r"""|url\(\s*["']?([^"')]+)["']?\s*\)"""
    r"""|srcset\s*=\s*["']([^"']+)["']"""
    r"""|["'`]((?:\.?/)?(?:assets/|[\w-]+\.(?:html|css|js|png|jpe?g|webp|svg|mp4|webm|ico|pdf|woff2?))[^"'`\s]*)["'`]""",
    re.I)

HTACCESS = """# Evolve Capital Humano — configuração para hospedagem Apache (cPanel e similares)
AddDefaultCharset UTF-8
DirectoryIndex index.html
Options -Indexes
ErrorDocument 404 /404.html

# Para forçar HTTPS: ative o SSL gratuito no painel da hospedagem, confirme que
# https://seudominio abre normalmente e só então tire o "#" das 3 linhas abaixo.
# RewriteEngine On
# RewriteCond %{HTTPS} off
# RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

<IfModule mod_mime.c>
  AddType application/manifest+json .webmanifest
  AddType image/webp .webp
  AddType image/svg+xml .svg
  AddType video/mp4 .mp4
</IfModule>

<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css text/plain text/xml application/javascript application/json application/manifest+json image/svg+xml
</IfModule>

# CSS e JS já levam ?v=AAAAMMDD nas páginas; HTML nunca fica em cache
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresDefault "access plus 1 week"
  ExpiresByType text/html "access plus 0 seconds"
  ExpiresByType text/css "access plus 1 year"
  ExpiresByType application/javascript "access plus 1 year"
  ExpiresByType image/webp "access plus 1 year"
  ExpiresByType image/jpeg "access plus 1 year"
  ExpiresByType image/png "access plus 1 year"
  ExpiresByType image/svg+xml "access plus 1 year"
  ExpiresByType video/mp4 "access plus 1 year"
</IfModule>
"""


def rastrear():
    vistos, fila = set(), list(ENTRADAS)
    while fila:
        rel = os.path.normpath(fila.pop())
        caminho = os.path.join(RAIZ, rel)
        if rel in vistos or not os.path.isfile(caminho):
            continue
        vistos.add(rel)
        if not rel.endswith(TEXTO):
            continue
        texto = io.open(caminho, encoding="utf-8", errors="ignore").read()
        base = os.path.dirname(rel)
        for m in REF.finditer(texto):
            for v in (g for g in m.groups() if g):
                partes = [p.strip().split(" ")[0] for p in v.split(",")] if m.group(3) else [v]
                for p in partes:
                    if p.startswith(BASE_ATUAL + "/"):
                        p = p[len(BASE_ATUAL) + 1:] or "index.html"
                    elif not p or re.match(r"^(?:[a-z]+:|#|//|\$|\{)", p, re.I):
                        continue
                    p = unquote(urlsplit(p).path)
                    if not p or "${" in p:
                        continue
                    alvo = os.path.normpath(p.lstrip("/") if p.startswith("/") else os.path.join(base, p))
                    if alvo.startswith(".."):
                        continue
                    if os.path.isdir(os.path.join(RAIZ, alvo)):
                        alvo = os.path.join(alvo, "index.html")
                    fila.append(alvo)
    return sorted(vistos)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dominio", help="endereço final, ex.: https://www.evolve.com.br")
    ap.add_argument("--planilha", help="URL /exec do Apps Script (leads do diagnóstico)")
    a = ap.parse_args()

    arquivos = rastrear()
    if os.path.isdir(SAIDA):
        shutil.rmtree(SAIDA)
    for rel in arquivos:
        destino = os.path.join(SAIDA, rel)
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        shutil.copy2(os.path.join(RAIZ, rel), destino)

    def editar(rel, fn):
        caminho = os.path.join(SAIDA, rel)
        texto = io.open(caminho, encoding="utf-8").read()
        novo = fn(texto)
        if novo != texto:
            io.open(caminho, "w", encoding="utf-8", newline="\n").write(novo)

    # a 404 é servida em qualquer profundidade de URL: a base é a raiz do domínio
    editar("404.html", lambda t: t.replace(f'<base href="{BASE_ATUAL}/">', '<base href="/">'))

    if a.dominio:
        nova = a.dominio.rstrip("/")
        for rel in arquivos:
            if rel.endswith(TEXTO):
                editar(rel, lambda t: t.replace(BASE_ATUAL, nova))

    if a.planilha:
        editar("assets/js/diagnostico.js",
               lambda t: re.sub(r"LEAD_ENDPOINT: '[^']*'", f"LEAD_ENDPOINT: '{a.planilha}'", t, count=1))

    io.open(os.path.join(SAIDA, ".htaccess"), "w", encoding="utf-8", newline="\n").write(HTACCESS)

    zip_path = SAIDA + ".zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for pasta, _, nomes in os.walk(SAIDA):
            for n in sorted(nomes):
                completo = os.path.join(pasta, n)
                z.write(completo, os.path.relpath(completo, SAIDA))

    total = sum(os.path.getsize(os.path.join(p, n)) for p, _, ns in os.walk(SAIDA) for n in ns)
    print(f"{len(arquivos) + 1} arquivos, {total / 1e6:.1f} MB")
    print(f"Pasta: {SAIDA}")
    print(f"Zip:   {zip_path} ({os.path.getsize(zip_path) / 1e6:.1f} MB)")
    print(f"Domínio: {a.dominio or 'NÃO DEFINIDO (canonical/sitemap ainda em ' + BASE_ATUAL + ')'}")
    print(f"Planilha: {a.planilha or 'NÃO LIGADA (leads ficam só no navegador do visitante)'}")


if __name__ == "__main__":
    main()
