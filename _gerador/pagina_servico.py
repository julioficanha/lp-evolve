# -*- coding: utf-8 -*-
"""Gabarito das páginas de serviço. Cada seção é opcional e controlada pelos
dados de `dados_servicos.py`; o teste (quiz) é montado por assets/js/diagnostico.js."""
import partes as P

SETA = ('<svg class="btn-arrow" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg>')
SETA_BAIXO = ('<svg class="btn-arrow" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
              'stroke-width="2" aria-hidden="true"><path d="M12 5v14M5 12l7 7 7-7"/></svg>')
ICO_OK = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">'
          '<path d="M20 6L9 17l-5-5"/></svg>')
ICO_X = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">'
         '<path d="M18 6L6 18M6 6l12 12"/></svg>')

# Blocos do teste: nome exibido e número de perguntas (o conteúdo vive no JS)
BLOCOS_TESTE = {
    "dp":  ("Departamento Pessoal e conformidade trabalhista", 10),
    "sst": ("Segurança e Saúde no Trabalho", 9),
    "rh":  ("Estrutura de RH e Gestão de Pessoas", 15),
    "lid": ("Liderança e gestão", 7),
}


def _li(itens):
    return "".join(f"<li>{x}</li>" for x in itens)


def _entregas(itens):
    ico = ('<svg class="entregavel__ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
           'stroke-width="1.4" stroke-linecap="round" aria-hidden="true">'
           '<path d="M4 6h16M4 12h16M4 18h10"/></svg>')
    return "".join(
        f'<div class="entregavel" data-reveal>{ico}<h4>{t}</h4><p>{d}</p></div>'
        for t, d in itens
    )


def _formatos(itens):
    return "".join(f'<span class="formato">{x}</span>' for x in itens)


def _indicador(ind, i):
    atraso = f' style="--d:{i*90}ms"' if i else ""
    if "count" in ind:
        grupo = ' data-count-group="true"' if ind.get("group") else ""
        pre = f'<span class="prefix">{ind["prefix"]}</span>' if ind.get("prefix") else ""
        suf = f'<span class="suffix">{ind["suffix"]}</span>' if ind.get("suffix") else ""
        num = f'<span class="indicador__num" data-count="{ind["count"]}"{grupo}>{pre}<span class="value">0</span>{suf}</span>'
    else:
        suf = f'<span class="suffix">{ind["suffix"]}</span>' if ind.get("suffix") else ""
        num = f'<span class="indicador__num"><span class="value">{ind["valor"]}</span>{suf}</span>'
    return (f'\n          <div class="indicador" data-reveal{atraso}>\n            {num}\n'
            f'            <span class="indicador__label">{ind["label"]}</span>\n          </div>')


def _teste(s):
    nome, n = BLOCOS_TESTE[s["bloco"]]
    return f"""
    <!-- TESTE · DIAGNÓSTICO RÁPIDO DE RH (bloco: {nome}) -->
    <section class="diag teste" id="diagnostico" data-diag="{s['slug']}" data-bloco="{s['bloco']}">
      <div class="u-wrap">
        <div class="diag__head" data-reveal>
          <span class="diag__eyebrow">Teste rápido · {n} perguntas · {nome}</span>
          <h2 class="diag__title">{s['teste_titulo']}</h2>
          <p class="diag__lead">
            Responda com o cenário real, não com o desejado. Ao final, você vê a pontuação da sua
            empresa neste tema e pode acessar o resultado completo, com os pontos de atenção.
          </p>
        </div>

        <noscript>
          <div class="capta__ok" style="margin-bottom:2rem">
            <strong>O teste interativo precisa de JavaScript ativado.</strong>
            <p>Se preferir, fale com a nossa equipe: as mesmas perguntas são feitas na conversa inicial.</p>
          </div>
        </noscript>

        <div class="teste__app" data-teste-app data-assunto="{s['assunto']}"></div>
      </div>
    </section>
"""


def _abertura(s):
    """Quatro composições distintas. A foto entra na proporção natural do
    recorte (--prop), então nada é esmagado nem cortado ao acaso."""
    if s.get("bloco"):
        _, n = BLOCOS_TESTE[s["bloco"]]
        acoes = f"""            <a href="#diagnostico" class="btn btn-terracota btn-lg" data-verb="responder">
              <span>Fazer o teste · {n} perguntas</span>
              {SETA_BAIXO}
            </a>
            <button type="button" class="btn btn-outline-light btn-lg open-contact-trigger" data-subject="{s['assunto']}" data-verb="orçamento"><span>Solicitar orçamento</span></button>"""
    else:
        acoes = f"""            <button type="button" class="btn btn-terracota btn-lg open-contact-trigger" data-subject="{s['assunto']}" data-verb="conversar">
              <span>Conversar sobre minha empresa</span>
              {SETA}
            </button>"""

    texto = f"""        <div class="svc-abre__texto">
          <span class="svc-abre__indice">{s['indice']}</span>
          <h1 class="svc-abre__titulo rise"><span>{s['h1a']}</span></h1>
          <p class="svc-abre__titulo svc-abre__titulo--eco" data-reveal><em>{s['h1b']}</em></p>
          <p class="svc-abre__q" data-reveal style="--d:300ms">{s['pergunta']}</p>
          <div class="svc-abre__acoes" data-reveal style="--d:480ms">
{acoes}
          </div>
        </div>"""

    foto = f"""        <figure class="svc-abre__foto" style="--prop:{s['proporcao']};--d:200ms" data-reveal>
          <img src="{s['imagem']}" alt="{s['imagem_alt']}" width="{s.get('imagem_width', 900)}" height="{s.get('imagem_height', 600)}" fetchpriority="high" decoding="async">
          <figcaption>{s['legenda']}</figcaption>
        </figure>"""

    v = s['variante']

    if v == 'b':
        # texto centralizado e a fotografia como faixa larga embaixo
        return f"""
  <main id="main-content" data-servico="{s['slug']}">

    <section class="svc-abre svc-abre--b">
      <div class="u-wrap svc-abre__centro">
{texto}
      </div>
      <div class="u-wrap">
{foto}
      </div>
    </section>
"""

    # a: texto à esquerda · c: fotografia à esquerda · d: fotografia sangrando à direita
    ordem = (foto + "\n" + texto) if v == 'c' else (texto + "\n" + foto)
    return f"""
  <main id="main-content" data-servico="{s['slug']}">

    <section class="svc-abre svc-abre--{v}">
      <div class="u-wrap svc-abre__grid">
{ordem}
      </div>
    </section>
"""


def _para_quem(s):
    lead = (f'\n          <p class="bloco__lead" style="max-width:56ch">{s["para_quem"]}</p>'
            if s.get("para_quem") else "")
    extra = (f'\n          <p class="bloco__lead" style="max-width:60ch;margin-top:1.25rem">{s["para_quem_extra"]}</p>'
             if s.get("para_quem_extra") else "")
    return f"""
    <!-- PARA QUEM É -->
    <section class="bloco" style="background:var(--off-white)">
      <div class="u-wrap">
        <div class="bloco__head" data-reveal>
          <span class="no-secao"><span class="no-secao__dot"></span>Para quem é</span>
          <h2 class="bloco__title" style="margin-top:1.25rem">{s['para_quem_titulo']}</h2>{lead}{extra}
        </div>

        <div class="bloco__head" data-reveal style="margin-bottom:1.5rem">
          <span class="bloco__eyebrow">Problemas que chegam até nós</span>
        </div>
        <ol class="lista-chegam" data-reveal>
          {_li(s['problemas'])}
        </ol>
      </div>
    </section>
"""


def _fases(f):
    passos = "".join(f"""
          <div class="rotina__step">
            <span class="rotina__when">{quando}</span>
            <h4>{titulo}</h4>
            <ul>{_li(itens)}</ul>
          </div>""" for quando, titulo, itens in f["passos"])
    return f"""
    <!-- COMO FUNCIONA -->
    <section class="rotina" id="como-funciona">
      <div class="u-wrap">
        <div class="bloco__head" data-reveal>
          <span class="no-secao"><span class="no-secao__dot"></span>Como funciona</span>
          <h2 class="bloco__title" style="margin-top:1.25rem">{f['titulo']}</h2>
          <p class="bloco__lead">{f['lead']}</p>
        </div>

        <div class="rotina__rail rotina__rail--4">{passos}
        </div>
      </div>
    </section>
"""


def _solucoes(s):
    cards = "".join(
        f'<article class="mag" data-reveal><span class="mag__num">{i+1:02d}</span><h3 class="mag__title">{t}</h3><p class="mag__desc">{d}</p></article>'
        for i, (t, d) in enumerate(s['solucoes']))
    return f"""
    <!-- SOLUÇÕES -->
    <section id="solucoes" class="bloco" style="background:var(--azul-petroleo);color:var(--off-white)">
      <div class="u-wrap">
        <div class="bloco__head" data-reveal>
          <span class="no-secao" style="color:rgba(239,239,237,0.55)"><span class="no-secao__dot"></span>{s.get('solucoes_eyebrow', 'Soluções')}</span>
          <h2 class="bloco__title" style="color:var(--off-white);margin-top:1.25rem">{s.get('solucoes_titulo', 'O que exatamente colocamos em pé.')}</h2>
        </div>
        <div class="mag-grid mag-grid--dark" data-stagger="80">
          {cards}
        </div>
      </div>
    </section>
"""


def _extra(x):
    """Seções complementares: cartões ('cards') ou colunas com lista ('colunas')."""
    lead = f'\n          <p class="bloco__lead" style="max-width:58ch">{x["lead"]}</p>' if x.get("lead") else ""
    if "cards" in x:
        corpo = '<div class="mag-grid" data-stagger="80">' + "".join(
            f'<article class="mag" data-reveal><h3 class="mag__title">{t}</h3><p class="mag__desc">{d}</p></article>'
            for t, d in x["cards"]) + "</div>"
    else:
        corpo = '<div class="limites__grid">' + "".join(
            f'<div class="limite" data-reveal><h4>{t}</h4><ul>'
            + "".join(f'<li>{ICO_OK}<span>{i}</span></li>' for i in itens)
            + '</ul></div>' for t, itens in x["colunas"]) + "</div>"
    return f"""
    <!-- {x['eyebrow'].upper()} -->
    <section class="bloco" style="background:var(--off-white)">
      <div class="u-wrap">
        <div class="bloco__head" data-reveal>
          <span class="no-secao"><span class="no-secao__dot"></span>{x['eyebrow']}</span>
          <h2 class="bloco__title" style="margin-top:1.25rem">{x['titulo']}</h2>{lead}
        </div>
        {corpo}
      </div>
    </section>
"""


def _entregas_secao(s):
    entregas = '<div class="entregaveis" data-stagger="70">' + _entregas(s['entregas']) + '</div>'
    if s['slug'] == 'lideranca':
        grupos = []
        for fase in ('Antes', 'Durante', 'Depois'):
            itens = [(t.split(' · ', 1)[1], d) for t, d in s['entregas'] if t.startswith(fase + ' · ')]
            grupos.append(f'<section class="trilha-formacao__fase" data-reveal><h3>{fase}</h3>' + _entregas(itens) + '</section>')
        entregas = '<div class="trilha-formacao">' + ''.join(grupos) + '</div>'
    formatos = ""
    if s.get("formatos"):
        formatos = f"""
        <div class="bloco__head u-mt-xl" data-reveal>
          <span class="bloco__eyebrow">Formatos de contratação</span>
          <p class="bloco__lead" style="margin-top:0;max-width:56ch">{s.get('formatos_lead', 'Escolhemos o formato conforme o estágio do negócio e a capacidade de sustentação. Valores e prazos são definidos após o alinhamento inicial.')}</p>
        </div>
        <div class="formatos" data-reveal>
          {_formatos(s['formatos'])}
        </div>"""
    return f"""
    <!-- ENTREGAS -->
    <section id="entregas" class="bloco" style="background:var(--off-white)">
      <div class="u-wrap">
        <div class="bloco__head" data-reveal>
          <span class="no-secao"><span class="no-secao__dot"></span>{s.get('entregas_eyebrow', 'Entregáveis')}</span>
          <h2 class="bloco__title" style="margin-top:1.25rem">{s.get('entregas_titulo', 'O que você recebe, de forma concreta.')}</h2>
        </div>
        {entregas}{formatos}
      </div>
    </section>
"""


def _limites(s):
    lead = s.get("limites_lead", "Dizemos os limites antes de assinar, não depois. Assumimos apenas aquilo que temos competência e capacidade para entregar.")
    lead_html = f'\n          <p class="bloco__lead" style="max-width:58ch">{lead}</p>' if lead else ""
    conexao = ""
    if s.get("conexao"):
        conexao = f"""

        <div class="bloco__head u-mt-xl" data-reveal>
          <span class="bloco__eyebrow">Conexão com o portfólio</span>
          <p class="bloco__lead" style="margin-top:0;max-width:60ch">{s['conexao']}</p>
        </div>"""
    return f"""
    <!-- LIMITES: PONTOS FORTES E PONTOS FRACOS -->
    <section class="limites">
      <div class="u-wrap">
        <div class="bloco__head" data-reveal>
          <span class="no-secao"><span class="no-secao__dot"></span>Escopo com honestidade</span>
          <h2 class="bloco__title" style="margin-top:1.25rem">{s.get('limites_titulo', 'O que esta frente resolve bem — e o que ela não resolve.')}</h2>{lead_html}
        </div>

        <div class="limites__grid">
          <div class="limite" data-reveal>
            <h4>{s.get('fortes_titulo', 'Pontos fortes desta frente')}</h4>
            <ul>
              {"".join(f'<li>{ICO_OK}<span>{x}</span></li>' for x in s['fortes'])}
            </ul>
          </div>
          <div class="limite limite--fora" data-reveal style="--d:120ms">
            <h4>Limites e o que não fazemos aqui</h4>
            <ul>
              {"".join(f'<li>{ICO_X}<span>{x}</span></li>' for x in s['limites'])}
            </ul>
          </div>
        </div>{conexao}
      </div>
    </section>
"""


def _indicadores(s):
    return f"""
    <!-- AUTORIDADE · números escolhidos para esta frente -->
    <section id="autoridade" class="bloco" style="background:var(--off-white-card);padding:clamp(3.5rem,7vw,5.5rem) 0">
      <div class="u-wrap">
        <div class="indicadores indicadores--{s['slug']}">{"".join(_indicador(x, i) for i, x in enumerate(s['indicadores']))}
        </div>
      </div>
    </section>
"""


def _depoimento(s):
    empresa = f'\n              <span class="empresa">{s["depoente_empresa"]}</span>' if s.get("depoente_empresa") else ""
    return f"""
    <!-- DEPOIMENTO -->
    <section class="vozes">
      <div class="u-wrap">
        <article class="voz" style="grid-template-columns:1fr">
          <blockquote class="voz__quote" data-reveal style="max-width:56rem">
            <p>{s['depoimento']}</p>
            <footer class="voz__who">
              <span class="nome">{s['depoente']}</span>
              <span class="cargo">{s['depoente_cargo']}</span>{empresa}
            </footer>
          </blockquote>
        </article>
      </div>
    </section>
"""


def render(s):
    corpo = _abertura(s) + f"""
    <!-- RESULTADO ENTREGUE -->
    <section class="resultado">
      <div class="u-wrap">
        <span class="resultado__label">Resultado entregue</span>
        <p class="resultado__text" data-reveal>{s['resultado']}</p>
      </div>
    </section>
""" + _para_quem(s)

    if s.get("bloco"):
        corpo += _teste(s)
    if s.get("fases"):
        corpo += _fases(s["fases"])
    corpo += _solucoes(s)
    for x in s.get("extras", []):
        corpo += _extra(x)
    if s.get("entregas"):
        corpo += _entregas_secao(s)
    if s.get("fortes"):
        corpo += _limites(s)
    if s.get("indicadores"):
        corpo += _indicadores(s)
    if s.get("depoimento"):
        corpo += _depoimento(s)

    script = '\n  <script src="assets/js/diagnostico.js?v=20261004-nomes" defer></script>' if s.get("bloco") else ""
    return (
        P.head(s["titulo"], s["descricao"])
        + P.cabecalho("servicos")
        + corpo
        + P.cta_final(s["cta_titulo"], s["cta_sub"], s.get("cta_botao", "Solicitar orçamento"), s["assunto"])
        + "\n  </main>\n"
        + P.rodape()
        + P.modal(f"Falar sobre {s['nome_curto']}")
        + P.scripts(script)
    )
