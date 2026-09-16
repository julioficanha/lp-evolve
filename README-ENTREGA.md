# LP Evolve Capital Humano — nota de entrega

## Estrutura

```
index.html                               COMECE AQUI — abertura da marca + três portais
carta-aberta.html                        CARTA ABERTA — a carta de vendas completa
evolve.html                              A EVOLVE — institucional (equipe, cultura, números)
servicos.html                            NOSSOS SERVIÇOS — hub curto com as 4 frentes
servicos-pessoas-relacionamento.html     Frente 01 + diagnóstico
servicos-recrutamento-selecao.html       Frente 02 + diagnóstico
servicos-riscos-saude.html               Frente 03 + diagnóstico
servicos-lideranca-desenvolvimento.html  Frente 04 + diagnóstico

assets/images/placeholder/               ilustrações próprias em SVG (40 KB no total)
  carta.svg · servicos.svg · equipe.svg  as três imagens dos portais
  retrato-01..06.svg                     retratos provisórios do mosaico da abertura

style.css                                base herdada (cabeçalho, botões, rodapé, modal, FAQ)
assets/css/system.css                    sistema de movimento e componentes novos
assets/js/app.js                         motor de interação (um único laço rAF)
assets/js/diagnostico.js                 motor do quiz + banco de perguntas e devolutivas
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

## O algoritmo do diagnóstico

Quatro perguntas por serviço, quatro alternativas cada, com pesos **0 · 1 · 3 · 5**
(0 = não existe, 5 = maduro). O indicador exibido mede **risco**, então a média é
invertida:

```
nota = 5 − [(p1 + p2 + p3 + p4) / 4]
```

Assim **0 significa estrutura instalada e 5 significa risco ativo** — quanto mais
alto o número, mais grave o cenário. A direção fica escrita ao lado do medidor,
para não depender de interpretação.

Os pesos são propositalmente não lineares. A distância entre "não existe" e
"existe no improviso" é pequena na prática; o salto para "existe formalizado" é
grande. Com 0-1-2-3 quatro respostas medianas gerariam uma nota falsamente boa.

| Nota | Faixa | Leitura | Cor |
|------|-------|---------|-----|
| 0,0 – 1,2 | Maturidade instalada | Ganho maior está em outra frente | verde azulado |
| 1,3 – 2,4 | Estrutura com lacunas | Lacunas pontuais e localizáveis | oliva |
| 2,5 – 3,4 | Organização iniciada | Base montada, frágil nas bordas | terracota |
| 3,5 – 4,4 | Dependência estrutural | Funciona porque alguém segura | terracota fechado |
| 4,5 – 5,0 | **Risco ativo** | Nada estruturado; exposição real | **vermelho vinho** |

Na faixa crítica o medidor inteiro entra em alerta: traço, valor, moldura e o
selo do resultado passam para vermelho vinho (`#722033`).

São **20 devolutivas** (4 serviços × 5 faixas), cada uma com título, leitura e
três próximos passos extraídos das entregas daquele serviço no manual comercial.
O tom segue o Manual da Cultura: apresentar o que foi identificado sem rótulos,
simplificações ou acusações, e sempre indicar o próximo movimento.

Toda a lógica e todo o texto estão em `assets/js/diagnostico.js`, no início do
arquivo, comentados em português.

---

## O que falta ligar (2 itens)

### 1. Google Forms + notificação para a Evolve

Abra `assets/js/diagnostico.js` e preencha `FORM_CONFIG` no topo do arquivo:

```js
const FORM_CONFIG = {
  formId: '',        // ex: '1FAIpQLSd...'  (só o ID, sem /viewform)
  entries: { nome: 'entry.111111111', empresa: '...', /* ... */ }
};
```

Passo a passo:

1. Crie o formulário com estes campos, nesta ordem: **nome, empresa, cargo,
   e-mail, whatsapp, colaboradores, segmento, cidade/UF, desafio, serviço, nota,
   faixa, respostas**. Os quatro últimos são preenchidos automaticamente pela página.
2. No Forms, aba **Respostas** → menu de três pontos → **Receber notificações por
   e-mail de novas respostas**. É isso que avisa a Evolve a cada preenchimento.
3. Abra o formulário publicado, inspecione cada campo e copie o atributo `name`
   (formato `entry.123456789`).
4. Cole os valores em `FORM_CONFIG.entries` e o ID em `formId`.

**Enquanto o `formId` estiver vazio**, o diagnóstico funciona normalmente: os
dados vão para o `console` e para o `localStorage` (chaves `evolve_diagnosticos`
e `evolve_contatos`), o que permite testar o fluxo completo sem back-end.

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
