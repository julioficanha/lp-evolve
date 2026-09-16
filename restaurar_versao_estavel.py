#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Restauração Instantânea — Evolve Capital Humano
Executar este script restaura 100% do projeto (textos, imagens de estúdio, layouts, CSS, JS e protótipo)
de volta ao Snapshot Estável gravado no Git.
"""
import subprocess
import os

WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))

print("Iniciando restauração para o Snapshot Estável...")
try:
    subprocess.run(["git", "reset", "--hard", "versao-estavel"], cwd=WORKSPACE_DIR, check=True)
    subprocess.run(["git", "clean", "-fd"], cwd=WORKSPACE_DIR, check=True)
    print("Repositório restaurado com sucesso para a tag 'versao-estavel'!")
    
    print("Recompilando páginas estáticas e protótipo...")
    subprocess.run(["python3", "_gerador/build.py"], cwd=WORKSPACE_DIR, check=True)
    subprocess.run(["python3", "build_interactive_prototype.py"], cwd=WORKSPACE_DIR, check=True)
    print("TUDO PRONTO! O projeto foi 100% restaurado para a versão estável.")
except Exception as e:
    print(f"Erro durante a restauração: {e}")
