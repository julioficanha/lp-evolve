# -*- coding: utf-8 -*-
"""Troca a URL base do site (canonical, Open Graph, JSON-LD, sitemap, robots, llms.txt).

Uso:   python3 _gerador/trocar_base.py https://www.dominio-novo.com.br

Hoje a base é https://julioficanha.github.io/lp-evolve (sem barra no fim).
"""
import io, os, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ATUAL = "https://julioficanha.github.io/lp-evolve"
ARQUIVOS = [
    "index.html", "evolve.html", "carta-aberta.html", "servicos.html",
    "servicos-operacional-dp.html", "servicos-recrutamento-selecao.html",
    "servicos-riscos-saude.html", "servicos-lideranca-desenvolvimento.html",
    "servicos-estruturacao-negocios.html", "404.html",
    "sitemap.xml", "robots.txt", "llms.txt", "_gerador/trocar_base.py",
]


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    nova = sys.argv[1].rstrip("/")
    for nome in ARQUIVOS:
        caminho = os.path.join(RAIZ, nome)
        if not os.path.exists(caminho):
            continue
        texto = io.open(caminho, encoding="utf-8").read()
        if ATUAL in texto:
            io.open(caminho, "w", encoding="utf-8", newline="\n").write(texto.replace(ATUAL, nova))
            print(f"  {nome}")
    print("Pronto. Confira o git diff.")


if __name__ == "__main__":
    main()
