# -*- coding: utf-8 -*-
"""Página Inicial Alternativa (Hero B2B Direct com foto da equipe na ACEFB)."""
import partes as P

TITULO = "Evolve Capital Humano — Consultoria para PMEs"
DESC = ("Organizamos a gestão de pessoas, desenvolvemos lideranças e construímos processos "
        "com a sua equipe. Para a sua empresa crescer sem depender de você para tudo.")

HERO_ALT = """
  <main id="main-content">

    <!-- HERO ALTERNATIVO -->
    <section class="hero-alt">
      <div class="container hero-alt__grid">
        <div class="hero-alt__content">
          <span class="hero-alt__kicker">CONSULTORIA PARA PEQUENAS E MÉDIAS EMPRESAS</span>
          <h1 class="hero-alt__title">
            Sua empresa pode<br>
            crescer.<br>
            <span class="hero-alt__title-emphasis">Sem depender de você<br>para tudo.</span>
          </h1>
          <p class="hero-alt__lead">
            Organizamos a gestão de pessoas, desenvolvemos lideranças e construímos processos com a sua equipe. Para o negócio ganhar estrutura — e você, espaço para decidir o futuro.
          </p>
          <div class="hero-alt__actions">
            <a href="#contato" class="btn btn-terracota btn-lg">Conversar sobre minha empresa</a>
            <a href="servicos.html" class="link-next">Encontrar meu próximo passo +</a>
          </div>
          <div class="hero-alt__meta">
            PMEs de 5 a 200 colaboradores &nbsp;·&nbsp; Atuação nacional
          </div>
        </div>

        <div class="hero-alt__media-card">
          <div class="hero-alt__card-inner">
            <div class="hero-alt__image-wrapper">
              <img src="assets/images/parceria/foto_cliente_acefb.png" alt="Equipe Evolve reunida na ACEFB" loading="eager">
            </div>
            <div class="hero-alt__card-body">
              <span class="hero-alt__card-kicker">ESTRUTURA SE CONSTRÓI COM PESSOAS.</span>
              <h2 class="hero-alt__card-title">Da conversa à prática.</h2>
              <p class="hero-alt__card-sub">Junto de quem faz acontecer.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
"""

PORTAIS = """
    <!-- TRÊS PORTAIS -->
    <section class="bloco" style="background:var(--off-white);padding-top:clamp(3rem,7vw,5.5rem)">
      <div class="u-wrap">

        <!-- 01 · CARTA ABERTA -->
        <article class="portal" data-reveal>
          <span class="portal__indice">01 · Para ler primeiro</span>
          <div class="portal__media">
            <img src="assets/images/placeholder/carta.svg"
                 alt="Uma carta aberta sobre a mesa, com a marca da Evolve no topo da folha e uma assinatura ao pé"
                 loading="lazy" width="800" height="620">
          </div>
          <div class="portal__texto">
            <h2 class="portal__titulo">Carta aberta aos empresários</h2>
            <p>
              Para quem centraliza decisões, passa o dia apagando incêndios e sente que a empresa
              não roda sem a sua presença. <strong>Você não está sozinho.</strong>
            </p>
            <a href="carta-aberta.html#cena" class="btn btn-terracota btn-lg" data-verb="ler">
              <span>Ler a carta</span>
              <svg class="btn-arrow" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </a>
          </div>
        </article>

        <!-- 02 · NOSSOS SERVIÇOS -->
        <article class="portal" data-reveal>
          <span class="portal__indice">02 · O que fazemos</span>
          <div class="portal__media">
            <img src="assets/images/placeholder/servicos.svg"
                 alt="As quatro frentes de atuação da Evolve conectadas por uma única linha contínua"
                 loading="lazy" width="800" height="620">
          </div>
          <div class="portal__texto">
            <h2 class="portal__titulo">Nossos serviços</h2>
            <p>
              Quatro frentes especializadas: Pessoas e Relações de Trabalho, Recrutamento e Seleção,
              Riscos Psicossociais e Saúde Organizacional, Liderança e Desenvolvimento.
              <strong>Cada uma responde a uma pergunta do negócio</strong> — e traz um diagnóstico
              de quatro perguntas para você medir onde está.
            </p>
            <a href="servicos.html" class="btn btn-outline-dark btn-lg" data-verb="conhecer">
              <span>Conhecer os serviços</span>
              <svg class="btn-arrow" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </a>
          </div>
        </article>

        <!-- 03 · NOSSA EQUIPE -->
        <article class="portal" data-reveal>
          <span class="portal__indice">03 · Quem faz</span>
          <div class="portal__media">
            <img src="assets/images/placeholder/equipe.svg"
                 alt="Espaço reservado para a fotografia oficial da equipe Evolve"
                 loading="lazy" width="800" height="620">
          </div>
          <div class="portal__texto">
            <h2 class="portal__titulo">Nossa equipe</h2>
            <p>
              Uma rede, não um escritório. Profissionais conectados em torno da mesma direção:
              <strong>entrar junto no problema e sair deixando capacidade instalada.</strong>
            </p>
            <a href="evolve.html#equipe" class="btn btn-outline-dark btn-lg" data-verb="conhecer">
              <span>Conhecer a equipe</span>
              <svg class="btn-arrow" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </a>
          </div>
        </article>

      </div>
    </section>
"""


def render():
    return (
        P.head(TITULO, DESC)
        + P.cabecalho("comece")
        + HERO_ALT
        + PORTAIS
        + P.cta_final(
            "Por onde a sua empresa<br>precisa começar?",
            "Se preferir conversar antes de ler ou escolher um serviço, fale com a nossa equipe.")
        + "\n  </main>\n"
        + P.rodape()
        + P.modal()
        + P.scripts()
    )
