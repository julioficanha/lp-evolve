# LP Evolve Capital Humano — nota de entrega

## Estrutura

```
index.html                               COMECE AQUI — abertura da marca + três portais
carta-aberta.html                        CARTA ABERTA — a carta de vendas completa
evolve.html                              A EVOLVE — institucional (equipe, cultura, números)
servicos.html                            NOSSOS SERVIÇOS — hub curto com as 5 frentes
servicos-operacional-dp.html             Frente 01 · Blindagem de RH + teste
servicos-recrutamento-selecao.html       Frente 02 · Recrutamento e Seleção + teste
servicos-riscos-saude.html               Frente 03 · Riscos Psicossociais + teste
servicos-lideranca-desenvolvimento.html  Frente 04 · Cursos, Palestras e Treinamentos + teste
servicos-estruturacao-negocios.html      Frente 05 · Negócio, Governança e Gestão
servicos-pessoas-relacionamento.html     fora do menu · Pessoas e Relações de Trabalho + teste

assets/images/placeholder/               ilustrações próprias em SVG (40 KB no total)
  carta.svg · servicos.svg · equipe.svg  as três imagens dos portais
  retrato-01..06.svg                     retratos provisórios do mosaico da abertura

style.css                                base herdada (cabeçalho, botões, rodapé, modal, FAQ)
assets/css/system.css                    sistema de movimento e componentes novos
assets/js/app.js                         motor de interação (um único laço rAF)
assets/js/diagnostico.js                 teste "Diagnóstico Rápido de RH" (CONFIG + BLOCOS + motor)
DESIGN.md                                design system + sistema de movimento documentado
_gerador/                                gerador das páginas estáticas
```

### Regenerar as páginas

O cabeçalho, o rodapé e o modal são iguais nas sete páginas. Em vez de mantê-los
copiados à mão, eles vivem em `_gerador/partes.py`. Para aplicar uma mudança
global (por exemplo, inserir o telefone oficial no rodapé), edite a parte
correspondente e rode:

```bash
python3 _gerador/build.py
```

Os `.html` na raiz são o produto final e funcionam sozinhos, sem build, sem
servidor e sem dependência de rede além das fontes do Google e do Lenis (CDN).

---

## O teste — Diagnóstico Rápido de RH da sua Empresa

(Substitui o diagnóstico antigo de 4 perguntas com medidor 0–5, excluído em out/2026.)

Quatro blocos, um por página de serviço, na mesma seção `#diagnostico`:

| Bloco | Perguntas | Página(s) |
|---|---|---|
| DP e conformidade trabalhista | 10 | `servicos-operacional-dp.html` (Blindagem de RH) |
| Segurança e Saúde no Trabalho | 9 | `servicos-riscos-saude.html` |
| Estrutura de RH e Gestão de Pessoas | 15 | `servicos-recrutamento-selecao.html` e `servicos-pessoas-relacionamento.html` |
| Liderança e gestão | 7 | `servicos-lideranca-desenvolvimento.html` |

- Respostas: Sim = 2 · Parcialmente = 1 · Não = 0 · Não se aplica (fica fora da conta).
- Cada pergunta tem peso 1, 2 ou 3 (3 = crítica: passivo, multa, saúde, risco legal).
- `Bloco% = Σ(peso × resposta) / Σ(peso × 2) × 100`, só sobre as perguntas respondidas e aplicáveis.
- `Índice Geral = 0,30·DP + 0,30·SST + 0,20·Gestão de Pessoas + 0,20·Liderança`, só quando os 4 blocos
  foram feitos (o progresso fica no navegador); bloco 100% "Não se aplica" sai e os pesos são redistribuídos.
- Faixas: 76–100 RH Estruturado 🟢 · 51–75 RH em Desenvolvimento 🟡 · 26–50 Pontos de Atenção 🟠 · 0–25 Necessidade de Estruturação 🔴.
- Alerta ⚠️: bloco abaixo de 40% ou qualquer pergunta de peso 3 respondida "Não".
- Validade: o bloco só é calculado com pelo menos 70% das perguntas respondidas.

Fluxo: dados da empresa (pedidos uma vez) → perguntas → pontuação pública + "Acesse seu resultado
completo" → cadastro de e-mail e telefone (lead) → resultado completo (por tema, lacunas críticas, índice geral).

Todas as constantes (pesos, faixas, limiares, `LEAD_ENDPOINT`) ficam no objeto `CONFIG`, no topo de
`assets/js/diagnostico.js`; as perguntas, em `BLOCOS`.

---

## O que falta ligar (2 itens)

### 1. Planilha Google de leads

Siga a nota **"Tutorial - Planilha Google de leads (Evolve)"** (Apps Script publicado como Web App) e cole a
URL `/exec` em `CONFIG.LEAD_ENDPOINT`. Cada teste concluído com cadastro gera uma linha na planilha.

**Enquanto `LEAD_ENDPOINT` estiver vazio**, o teste funciona normalmente: os leads ficam no `localStorage`
(chave `evolve_leads_pendentes`) e o console avisa.

### 2. Dados institucionais

Segundo o briefing (item 2.6.2), a página deve exibir **e-mail, telefone e
endereço**. Eles ainda não foram fornecidos. Todos os pontos onde entram estão
marcados visualmente na página com a etiqueta tracejada **PROVISÓRIO** e ficam
em `_gerador/partes.py` (funções `rodape()` e `cta_final()`).

---

## Conteúdo marcado como provisório

Tudo o que não estava nos documentos ficou **visivelmente sinalizado**, nunca
inventado:

- **Rodapé e CTA final** — e-mail, telefone e endereço institucionais.
- **evolve.html · equipe** — nomes completos, formações, registros profissionais e
  fotografias de Amanda e Simone. Só constam nos documentos os primeiros nomes
  (Amanda aparece no depoimento da Integração e no Manual da Cultura; Simone
  consta no briefing como a especialista de DP com mais de 20 anos).
- **evolve.html · números** — quantidade total de clientes, parceiros e projetos.
  O briefing traz apenas "+10.000 pessoas impactadas", "atuação nacional",
  "20+ anos em DP" e "PMEs de 5 a 200 colaboradores". Nenhum outro número foi criado.
- **evolve.html · parceiros** — logotipos e nomes autorizados de clientes.

### Duas decisões que precisam do seu aval

**1. `case_delta.png` foi removida da página.** É uma imagem gerada por IA com uma
placa escrita "REDE DELTA" e uma pessoa que não existe. Publicar isso apresenta
uma pessoa e um local inventados como se fossem um cliente real. Substitua por
uma fotografia real autorizada da Rede Delta.

**2. Cinco imagens da pasta não são fotografias — são recortes de página com
grandes áreas vazias e trechos de texto**, e por isso não foram usadas:
`foto_reuniao_mesa.png`, `foto_evento_lideranca.png`, `foto_palestra_resiliencia.png`,
`presenca_construtora.png`, `foto_equipe_sala.png`. Além disso, três pares são a
mesma foto em recortes diferentes (`presenca_industria` = `foto_cliente_fabrica`,
`presenca_comercio` = `foto_cliente_posto_auto`, `presenca_servicos` =
`foto_cliente_distribuidora`).

**Fotografias reais efetivamente em uso:** `foto_equipe_delta_blue`,
`foto_executivo_gravata_costas`, `presenca_industria`, `presenca_comercio`,
`presenca_servicos` e `foto_treinamento_equipe` (recortada à esquerda).
`hero_editorial.png` e `solutions_leadership.png` são imagens editoriais neutras
usadas como marcador, conforme o próprio briefing autoriza — devem ser trocadas
por fotografia real da Evolve quando houver.

---

## Divergência de nomenclatura que vale resolver

O manual comercial (**Serviços Evolve**) organiza o portfólio em quatro áreas:

1. Pessoas e Resultados do Negócio
2. Pessoas e Relações de Trabalho *(recrutamento e seleção está dentro desta)*
3. Riscos Psicossociais e Saúde Organizacional
4. Liderança e Desenvolvimento Humano Organizacional

A estrutura de páginas existente promove **Recrutamento e Seleção** a frente
própria e não tem página para a **Área 1**. Como você pediu para manter as quatro
páginas, foi feito o seguinte:

- Recrutamento e Seleção manteve página própria, e o cabeçalho dela declara
  explicitamente que é "uma solução da área Pessoas e Relações de Trabalho".
- A **Área 1** aparece em `servicos.html` como **o eixo que atravessa as quatro**
  — que é exatamente o papel que ela tem no manual ("Quatro áreas, uma mesma
  transformação") e o argumento central da carta de vendas.

Se preferir espelhar o manual ao pé da letra, o caminho é criar
`servicos-pessoas-resultados.html` e recolher Recrutamento como seção interna da
frente 01. Basta dizer.

---

## Verificações executadas

- Sete páginas: HTTP 200, sem erros de console, sem links quebrados, sem imagens
  quebradas, um único `<h1>` por página, `alt` em todas as imagens.
- Sem rolagem horizontal em 1920, 1600, 1440, 1280, 1100, 1024, 900, 768 e 390 px.
- Hero "SOLIDÃO" ocupa **exatamente uma tela** (medido: 900px em viewport de
  900px), sem vazar a cena seguinte — era o problema relatado.
- Diagnóstico testado nos três cenários extremos: 0,0 → Risco ativo · 5,0 →
  Maturidade instalada · 2,25 → Dependência estrutural. Medidor, faixa,
  refazer e captação de dados funcionando.
- Cena fixada: três tempos na ordem correta, notificação chegando no segundo,
  zoom progressivo de 1.085 a 1.165.
- Contadores, scrub antes/depois, canvas, ticker de territórios, faixa que
  inverte e acordeão dos pilares: todos verificados em execução.
