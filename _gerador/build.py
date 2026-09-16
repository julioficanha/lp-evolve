# -*- coding: utf-8 -*-
"""Gera as páginas estáticas da LP Evolve.

Uso:   python3 _gerador/build.py
"""
import io, os, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)

import pagina_comeca_aqui, pagina_carta_aberta, pagina_evolve, pagina_servicos, pagina_servico, pagina_index_alternativo
from dados_servicos import SERVICOS

REDIRECT = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Comece Aqui — Evolve Capital Humano</title>
  <link rel="canonical" href="index.html">
  <meta http-equiv="refresh" content="0; url=index.html">
  <meta name="robots" content="noindex">
</head>
<body>
  <p>A página <strong>Comece Aqui</strong> vive em <a href="index.html">index.html</a>.</p>
  <script>location.replace('index.html');</script>
</body>
</html>
"""


def escreve(nome, conteudo):
    io.open(os.path.join(RAIZ, nome), "w", encoding="utf-8", newline="\n").write(conteudo)
    print(f"  {nome:46s} {len(conteudo):>7,} bytes")


def main():
    print("Gerando páginas da LP Evolve:")
    escreve("index.html",             pagina_comeca_aqui.render())
    escreve("index-alternativo.html", pagina_index_alternativo.render())
    escreve("carta-aberta.html",      pagina_carta_aberta.render())
    escreve("evolve.html",            pagina_evolve.render())
    escreve("servicos.html",          pagina_servicos.render())
    for s in SERVICOS:
        escreve(s["arquivo"], pagina_servico.render(s))
    escreve("comece-aqui.html", REDIRECT)
    print("Pronto.")


if __name__ == "__main__":
    main()
