# -*- coding: utf-8 -*-
"""Gabarito das quatro páginas de serviço, com diagnóstico de 4 perguntas."""
import partes as P


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


DIAGNOSTICO = """
    <!-- DIAGNÓSTICO EM 4 PERGUNTAS -->
    <section class="diag" id="diagnostico" data-diag="%SLUG%">
      <div class="u-wrap">
        <div class="diag__head" data-reveal>
          <span class="diag__eyebrow">Diagnóstico rápido · 4 perguntas · 1 minuto</span>
          <h2 class="diag__title">%TITULO_DIAG%</h2>
          <p class="diag__lead">
            Responda com o cenário real, não com o desejado. O indicador vai de 0 a 5 e mede
            <strong>risco</strong>: zero significa estrutura instalada, cinco significa risco ativo.
            Ao final você recebe uma leitura do seu estágio e os três próximos movimentos recomendados.
          </p>
        </div>

        <noscript>
          <div class="capta__ok" style="margin-bottom:2rem">
            <strong>O diagnóstico interativo precisa de JavaScript ativado.</strong>
            <p>Se preferir, fale com a nossa equipe: as mesmas quatro perguntas são feitas na conversa inicial, com a leitura completa do seu cenário.</p>
          </div>
        </noscript>

        <div class="diag__shell">
          <div>
            <div class="diag__track" aria-hidden="true"></div>
            <div class="diag__stage"></div>

            <div class="diag__result" hidden>
              <span class="diag__result-badge" data-result-badge>Resultado</span>
              <h3 class="diag__result-title" data-result-title></h3>
              <p class="diag__result-read" data-result-read></p>

              <div class="diag__result-next">
                <h4>O que a Evolve faria primeiro</h4>
                <ol data-result-steps></ol>
              </div>

              <form class="capta" novalidate>
                <input type="hidden" name="payload" data-payload>
                <p style="font-size:0.9rem;line-height:1.6;color:rgba(239,239,237,0.72);max-width:52ch">
                  Quer receber esta leitura por escrito, com o olhar de um especialista sobre o seu caso?
                  Deixe os seus dados. O retorno é feito por uma pessoa da equipe, não por um robô.
                </p>

                <div class="capta__row">
                  <div class="capta__field">
                    <label for="d-nome-%SLUG%">Nome completo</label>
                    <input id="d-nome-%SLUG%" name="nome" type="text" required autocomplete="name" placeholder="Nome e sobrenome">
                  </div>
                  <div class="capta__field">
                    <label for="d-cargo-%SLUG%">Seu cargo</label>
                    <input id="d-cargo-%SLUG%" name="cargo" type="text" autocomplete="organization-title" placeholder="Ex.: sócio-diretor">
                  </div>
                </div>

                <div class="capta__row">
                  <div class="capta__field">
                    <label for="d-empresa-%SLUG%">Empresa</label>
                    <input id="d-empresa-%SLUG%" name="empresa" type="text" required autocomplete="organization" placeholder="Razão social ou nome fantasia">
                  </div>
                  <div class="capta__field">
                    <label for="d-colab-%SLUG%">Número de colaboradores</label>
                    <select id="d-colab-%SLUG%" name="colaboradores">
                      <option value="ate-5">Até 5</option>
                      <option value="5-20" selected>De 5 a 20</option>
                      <option value="21-50">De 21 a 50</option>
                      <option value="51-100">De 51 a 100</option>
                      <option value="101-200">De 101 a 200</option>
                      <option value="200-mais">Mais de 200</option>
                    </select>
                  </div>
                </div>

                <div class="capta__row">
                  <div class="capta__field">
                    <label for="d-email-%SLUG%">E-mail profissional</label>
                    <input id="d-email-%SLUG%" name="email" type="email" required autocomplete="email" placeholder="nome@suaempresa.com.br">
                  </div>
                  <div class="capta__field">
                    <label for="d-zap-%SLUG%">WhatsApp</label>
                    <input id="d-zap-%SLUG%" name="whatsapp" type="tel" required autocomplete="tel" placeholder="(00) 00000-0000">
                  </div>
                </div>

                <div class="capta__row">
                  <div class="capta__field">
                    <label for="d-seg-%SLUG%">Segmento</label>
                    <input id="d-seg-%SLUG%" name="segmento" type="text" placeholder="Ex.: indústria metalúrgica">
                  </div>
                  <div class="capta__field">
                    <label for="d-cidade-%SLUG%">Cidade / UF</label>
                    <input id="d-cidade-%SLUG%" name="cidadeUf" type="text" placeholder="Ex.: Pato Branco / PR">
                  </div>
                </div>

                <div class="capta__field">
                  <label for="d-desafio-%SLUG%">Em uma frase, qual é o seu principal desafio hoje?</label>
                  <textarea id="d-desafio-%SLUG%" name="desafio" rows="2" placeholder="Escreva com as suas palavras."></textarea>
                </div>

                <label class="capta__consent">
                  <input type="checkbox" name="consentimento" required>
                  <span>Autorizo a Evolve a entrar em contato sobre este diagnóstico e concordo com o uso dos meus dados exclusivamente para essa finalidade.</span>
                </label>

                <button type="submit" class="btn btn-terracota btn-lg" data-verb="enviar"><span>Receber a leitura completa</span></button>
              </form>

              <div class="diag__result-actions">
                <button type="button" class="btn btn-outline-light" data-restart data-verb="refazer"><span>Refazer o diagnóstico</span></button>
                <button type="button" class="btn btn-link-light open-contact-trigger" data-subject="%ASSUNTO%" data-verb="conversar"><span>Falar com a equipe agora</span></button>
              </div>

              <p class="diag__disclaimer">
                Este diagnóstico é uma leitura inicial baseada em quatro variáveis. O diagnóstico completo
                é conduzido presencialmente pela equipe da Evolve, junto com a diretoria e com quem executa
                o trabalho. Ele não substitui avaliação clínica, jurídica, médica ou de engenharia de segurança.
              </p>
            </div>
          </div>

          <aside class="medidor" aria-live="polite">
            <svg class="medidor__svg" viewBox="0 0 200 120" aria-hidden="true">
              <path class="medidor__rail" d="M 16 100 C 60 100, 62 24, 100 24 C 138 24, 140 100, 184 100"/>
              <path class="medidor__fill" d="M 16 100 C 60 100, 62 24, 100 24 C 138 24, 140 100, 184 100"/>
              <circle class="medidor__knob" cx="16" cy="100" r="5"/>
            </svg>
            <div class="medidor__score">
              <span class="val">0,0</span>
              <span class="max">/ 5,0</span>
            </div>
            <span class="medidor__stage">Aguardando respostas</span>
            <p class="medidor__direcao">
              <strong>0</strong> = estrutura instalada &nbsp;·&nbsp; <strong>5</strong> = risco ativo.
              Quanto mais alto o indicador, maior a exposição do seu negócio.
            </p>

            <div class="medidor__scale">
              <div class="medidor__scale-row" data-faixa="maturidade"><span class="chip">0–1,2</span> Maturidade instalada</div>
              <div class="medidor__scale-row" data-faixa="lacunas"><span class="chip">1,3–2,4</span> Estrutura com lacunas</div>
              <div class="medidor__scale-row" data-faixa="iniciada"><span class="chip">2,5–3,4</span> Organização iniciada</div>
              <div class="medidor__scale-row" data-faixa="dependencia"><span class="chip">3,5–4,4</span> Dependência estrutural</div>
              <div class="medidor__scale-row" data-faixa="risco"><span class="chip">4,5–5,0</span> Risco ativo</div>
            </div>
          </aside>
        </div>
      </div>
    </section>
"""



def _abertura(s):
    """Quatro composições distintas. A foto entra na proporção natural do
    recorte (--prop), então nada é esmagado nem cortado ao acaso."""
    texto = f"""        <div class="svc-abre__texto">
          <span class="svc-abre__indice">{s['indice']}</span>
          <h1 class="svc-abre__titulo rise"><span>{s['h1a']}</span></h1>
          <p class="svc-abre__titulo svc-abre__titulo--eco" data-reveal><em>{s['h1b']}</em></p>
          <p class="svc-abre__q" data-reveal style="--d:300ms">{s['pergunta']}</p>
          <div class="svc-abre__acoes" data-reveal style="--d:480ms">
            <a href="#diagnostico" class="btn btn-terracota btn-lg" data-verb="responder">
              <span>Fazer o diagnóstico · 4 perguntas</span>
              <svg class="btn-arrow" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
            </a>
            <button type="button" class="btn btn-outline-light btn-lg open-contact-trigger" data-subject="{s['assunto']}" data-verb="orçamento"><span>Solicitar orçamento</span></button>
          </div>
        </div>"""

    foto = f"""        <figure class="svc-abre__foto" style="--prop:{s['proporcao']}" data-reveal style="--d:200ms">
          <img src="{s['imagem']}" alt="{s['imagem_alt']}" width="900" height="600" fetchpriority="high">
          <figcaption>{s['legenda']}</figcaption>
        </figure>"""

    v = s['variante']

    if v == 'b':
        # texto centralizado e a fotografia como faixa larga embaixo
        return f"""
  <main id="main-content">

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
  <main id="main-content">

    <section class="svc-abre svc-abre--{v}">
      <div class="u-wrap svc-abre__grid">
{ordem}
      </div>
    </section>
"""


def render(s):
    diag = (DIAGNOSTICO
            .replace("%SLUG%", s["slug"])
            .replace("%TITULO_DIAG%", s["titulo_diag"])
            .replace("%ASSUNTO%", s["assunto"]))

    corpo = _abertura(s) + f"""
    <!-- RESULTADO VENDIDO -->
    <section class="resultado">
      <div class="u-wrap">
        <span class="resultado__label">Resultado vendido</span>
        <p class="resultado__text" data-reveal>{s['resultado']}</p>
      </div>
    </section>

    <!-- PARA QUEM É -->
    <section class="bloco" style="background:var(--off-white)">
      <div class="u-wrap">
        <div class="bloco__head" data-reveal>
          <span class="no-secao"><span class="no-secao__dot"></span>Para quem é</span>
          <h2 class="bloco__title" style="margin-top:1.25rem">{s['para_quem_titulo']}</h2>
          <p class="bloco__lead" style="max-width:56ch">{s['para_quem']}</p>
        </div>

        <div class="bloco__head" data-reveal style="margin-bottom:1.5rem">
          <span class="bloco__eyebrow">Problemas que chegam até nós</span>
        </div>
        <ol class="lista-chegam" data-reveal>
          {_li(s['problemas'])}
        </ol>
      </div>
    </section>

{diag}

    <!-- COMO FUNCIONA -->
    <section class="rotina" id="como-funciona">
      <div class="u-wrap">
        <div class="bloco__head" data-reveal>
          <span class="no-secao"><span class="no-secao__dot"></span>Como funciona</span>
          <h2 class="bloco__title" style="margin-top:1.25rem">Do diagnóstico à autonomia, em quatro fases.</h2>
          <p class="bloco__lead">A mesma metodologia sustenta as quatro frentes. Os prazos são definidos no alinhamento inicial, conforme o porte e o estágio da sua empresa.</p>
        </div>

        <div class="rotina__rail rotina__rail--4">
          <div class="rotina__step">
            <span class="rotina__when">Fase 01</span>
            <h4>Diagnóstico</h4>
            <ul>{_li(s['fase1'])}</ul>
          </div>
          <div class="rotina__step">
            <span class="rotina__when">Fase 02</span>
            <h4>Plano de ação 5W2H</h4>
            <ul>{_li(s['fase2'])}</ul>
          </div>
          <div class="rotina__step">
            <span class="rotina__when">Fase 03</span>
            <h4>Implantação acompanhada</h4>
            <ul>{_li(s['fase3'])}</ul>
          </div>
          <div class="rotina__step">
            <span class="rotina__when">Fase 04</span>
            <h4>Transferência de método</h4>
            <ul>{_li(s['fase4'])}</ul>
          </div>
        </div>
      </div>
    </section>

    <!-- SOLUÇÕES -->
    <section class="bloco" style="background:var(--azul-petroleo);color:var(--off-white)">
      <div class="u-wrap">
        <div class="bloco__head" data-reveal>
          <span class="no-secao" style="color:rgba(239,239,237,0.55)"><span class="no-secao__dot"></span>Soluções</span>
          <h2 class="bloco__title" style="color:var(--off-white);margin-top:1.25rem">O que exatamente colocamos em pé.</h2>
        </div>
        <div class="mag-grid mag-grid--dark" data-stagger="80">
          {"".join(f'<article class="mag" data-reveal><span class="mag__num">{i+1:02d}</span><h3 class="mag__title">{t}</h3><p class="mag__desc">{d}</p></article>' for i, (t, d) in enumerate(s['solucoes']))}
        </div>
      </div>
    </section>

    <!-- ENTREGAS -->
    <section class="bloco" style="background:var(--off-white)">
      <div class="u-wrap">
        <div class="bloco__head" data-reveal>
          <span class="no-secao"><span class="no-secao__dot"></span>Entregáveis</span>
          <h2 class="bloco__title" style="margin-top:1.25rem">O que você recebe, de forma concreta.</h2>
        </div>
        <div class="entregaveis" data-stagger="70">
          {_entregas(s['entregas'])}
        </div>

        <div class="bloco__head u-mt-xl" data-reveal>
          <span class="bloco__eyebrow">Formatos de contratação</span>
          <p class="bloco__lead" style="margin-top:0;max-width:56ch">Escolhemos o formato conforme o estágio do negócio e a capacidade de sustentação. Valores e prazos são definidos após o alinhamento inicial.</p>
        </div>
        <div class="formatos" data-reveal>
          {_formatos(s['formatos'])}
        </div>
      </div>
    </section>

    <!-- LIMITES: PONTOS FORTES E PONTOS FRACOS -->
    <section class="limites">
      <div class="u-wrap">
        <div class="bloco__head" data-reveal>
          <span class="no-secao"><span class="no-secao__dot"></span>Escopo com honestidade</span>
          <h2 class="bloco__title" style="margin-top:1.25rem">O que esta frente resolve bem — e o que ela não resolve.</h2>
          <p class="bloco__lead" style="max-width:58ch">Dizemos os limites antes de assinar, não depois. Assumimos apenas aquilo que temos competência e capacidade para entregar.</p>
        </div>

        <div class="limites__grid">
          <div class="limite" data-reveal>
            <h4>Pontos fortes desta frente</h4>
            <ul>
              {"".join('<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg><span>' + x + '</span></li>' for x in s['fortes'])}
            </ul>
          </div>
          <div class="limite limite--fora" data-reveal style="--d:120ms">
            <h4>Limites e o que não fazemos aqui</h4>
            <ul>
              {"".join('<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M18 6L6 18M6 6l12 12"/></svg><span>' + x + '</span></li>' for x in s['limites'])}
            </ul>
          </div>
        </div>

        <div class="bloco__head u-mt-xl" data-reveal>
          <span class="bloco__eyebrow">Conexão com o portfólio</span>
          <p class="bloco__lead" style="margin-top:0;max-width:60ch">{s['conexao']}</p>
        </div>
      </div>
    </section>

    <!-- AUTORIDADE -->
    <section class="bloco" style="background:var(--off-white-card);padding:clamp(3.5rem,7vw,5.5rem) 0">
      <div class="u-wrap">
        <div class="indicadores">
          <div class="indicador" data-reveal>
            <span class="indicador__num"><span class="value">NR-1</span></span>
            <span class="indicador__label">Certificação Internacional em Segurança Psicológica do Trabalho.</span>
          </div>
          <div class="indicador" data-reveal style="--d:90ms">
            <span class="indicador__num" data-count="10000" data-count-group="true"><span class="prefix">+</span><span class="value">0</span></span>
            <span class="indicador__label">Pessoas impactadas direta e indiretamente, em atuação nacional.</span>
          </div>
          <div class="indicador" data-reveal style="--d:180ms">
            <span class="indicador__num" data-count="20"><span class="value">0</span><span class="suffix">anos+</span></span>
            <span class="indicador__label">De experiência prática em DP dentro de empresas familiares.</span>
          </div>
          <div class="indicador" data-reveal style="--d:270ms">
            <span class="indicador__num"><span class="value">5</span><span class="suffix">a 200</span></span>
            <span class="indicador__label">Faixa de colaboradores das PMEs que atendemos.</span>
          </div>
        </div>
      </div>
    </section>

    <!-- DEPOIMENTO -->
    <section class="vozes">
      <div class="u-wrap">
        <article class="voz" style="grid-template-columns:1fr">
          <blockquote class="voz__quote" data-reveal style="max-width:56rem">
            <p>{s['depoimento']}</p>
            <footer class="voz__who">
              <span class="nome">{s['depoente']}</span>
              <span class="cargo">{s['depoente_cargo']}</span>
              <span class="empresa">{s['depoente_empresa']}</span>
            </footer>
          </blockquote>
        </article>
      </div>
    </section>
"""

    return (
        P.head(s["titulo"], s["descricao"])
        + P.cabecalho("servicos")
        + corpo
        + P.cta_final(s["cta_titulo"], s["cta_sub"], "Solicitar orçamento", s["assunto"])
        + "\n  </main>\n"
        + P.rodape()
        + P.modal(f"Falar sobre {s['nome_curto']}")
        + P.scripts('\n  <script src="assets/js/diagnostico.js" defer></script>')
    )
