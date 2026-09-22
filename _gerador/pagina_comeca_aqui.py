# -*- coding: utf-8 -*-
"""COMECE AQUI — Abertura B2B Direct com foto da palestra à direita e apresentação corporativa sem ícones de portal."""
import partes as P
from pagina_carta_aberta import PRESENCA

TITULO = "Comece Aqui — Evolve Capital Humano"
DESC = ("Estruturamos negócios para que pessoas e resultados evoluam juntos. "
        "Consultoria de gestão, cultura e desenvolvimento para pequenas e médias empresas.")

HERO_ALT = """
  <main id="main-content">

    <!-- HERO B2B DIRECT (Foto da palestra à direita) -->
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
            <a href="#modal-diagnostico" class="btn btn-terracota btn-lg open-contact-trigger" data-subject="comece-aqui">Conversar sobre minha empresa</a>
            <a href="servicos.html" class="link-next">Encontrar meu próximo passo +</a>
          </div>
          <div class="hero-alt__meta">
            PMEs de 5 a 200 colaboradores &nbsp;·&nbsp; Atuação nacional
          </div>
        </div>

        <div class="hero-alt__media-card">
          <div class="hero-alt__card-inner">
            <div class="hero-alt__image-wrapper">
              <img src="assets/images/parceria/amanda_palestra_casaco.png" alt="Palestra e treinamento corporativo conduzido pela Evolve Capital Humano" loading="eager">
            </div>
            <div class="hero-alt__card-body">
              <span class="hero-alt__card-kicker">DESENVOLVIMENTO & ESTRUTURA</span>
              <h2 class="hero-alt__card-title">Da conversa à prática.</h2>
              <p class="hero-alt__card-sub">Junto de quem faz acontecer.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
"""

APRESENTACAO = """
    <!-- APRESENTAÇÃO INSTITUCIONAL DA EMPRESA (Apresentação limpa, sem os ícones dos 3 cartões) -->
    <section class="bloco" style="background:var(--off-white);padding:clamp(4rem,8vw,6.5rem) 0">
      <div class="u-wrap">
        <div class="bloco__head" data-reveal>
          <span class="no-secao"><span class="no-secao__dot"></span>Como atuamos</span>
          <h2 class="bloco__title" style="margin-top:1.25rem;color:var(--azul-petroleo)">Entramos no problema junto com a sua equipe.</h2>
          <p style="margin-top:0.75rem;font-size:1.05rem;line-height:1.6;color:var(--azul-cinza);max-width:65ch">
            Não entregamos relatórios teóricos para a sua prateleira. Construímos processos, treinamos lideranças e deixamos capacidade instalada para a sua empresa rodar com autonomia.
          </p>
        </div>

        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:2rem;margin-top:3rem">
          
          <a href="carta-aberta.html" class="card-metodo" data-reveal style="text-decoration:none;background:#FFFFFF;border:1px solid rgba(2,23,59,0.08);border-radius:1.25rem;padding:2rem;box-shadow:0 6px 20px rgba(2,23,59,0.03);transition:transform 0.3s ease">
            <span style="font-size:0.75rem;font-weight:700;color:var(--terracota);text-transform:uppercase;letter-spacing:0.08em;display:block;margin-bottom:0.6rem">01 · Para ler primeiro</span>
            <h3 style="font-family:var(--font-serif);font-size:1.35rem;font-weight:700;color:var(--azul-petroleo);margin-bottom:0.75rem">Carta aberta aos empresários</h3>
            <p style="font-size:0.92rem;line-height:1.6;color:var(--azul-cinza);margin-bottom:1.25rem">
              Para quem centraliza decisões, passa o dia apagando incêndios e sente que a empresa não roda sem a sua presença. Você não está sozinho.
            </p>
            <span style="font-size:0.85rem;font-weight:700;color:var(--terracota);display:inline-flex;align-items:center;gap:0.4rem">Ler a carta →</span>
          </a>

          <a href="servicos.html" class="card-metodo" data-reveal style="--d:100ms;text-decoration:none;background:#FFFFFF;border:1px solid rgba(2,23,59,0.08);border-radius:1.25rem;padding:2rem;box-shadow:0 6px 20px rgba(2,23,59,0.03);transition:transform 0.3s ease">
            <span style="font-size:0.75rem;font-weight:700;color:var(--terracota);text-transform:uppercase;letter-spacing:0.08em;display:block;margin-bottom:0.6rem">02 · O que fazemos</span>
            <h3 style="font-family:var(--font-serif);font-size:1.35rem;font-weight:700;color:var(--azul-petroleo);margin-bottom:0.75rem">Nossos serviços & Diagnóstico</h3>
            <p style="font-size:0.92rem;line-height:1.6;color:var(--azul-cinza);margin-bottom:1.25rem">
              Quatro frentes especializadas: Pessoas e Relações de Trabalho, Recrutamento e Seleção, Riscos Psicossociais e Liderança. Faça um diagnóstico rápido.
            </p>
            <span style="font-size:0.85rem;font-weight:700;color:var(--terracota);display:inline-flex;align-items:center;gap:0.4rem">Conhecer serviços →</span>
          </a>

          <a href="evolve.html#equipe" class="card-metodo" data-reveal style="--d:200ms;text-decoration:none;background:#FFFFFF;border:1px solid rgba(2,23,59,0.08);border-radius:1.25rem;padding:2rem;box-shadow:0 6px 20px rgba(2,23,59,0.03);transition:transform 0.3s ease">
            <span style="font-size:0.75rem;font-weight:700;color:var(--terracota);text-transform:uppercase;letter-spacing:0.08em;display:block;margin-bottom:0.6rem">03 · Quem faz</span>
            <h3 style="font-family:var(--font-serif);font-size:1.35rem;font-weight:700;color:var(--azul-petroleo);margin-bottom:0.75rem">Nossa equipe técnica</h3>
            <p style="font-size:0.92rem;line-height:1.6;color:var(--azul-cinza);margin-bottom:1.25rem">
              Conheça os responsáveis técnicos que conduzem a gestão estratégica de pessoas, departamento pessoal, processos, finanças e riscos psicossociais.
            </p>
            <span style="font-size:0.85rem;font-weight:700;color:var(--terracota);display:inline-flex;align-items:center;gap:0.4rem">Conhecer a equipe →</span>
          </a>

        </div>
      </div>
    </section>
"""


def render():
    return (
        P.head(TITULO, DESC)
        + P.cabecalho("comece")
        + HERO_ALT
        + APRESENTACAO
        + PRESENCA
        + P.cta_final(
            "Por onde a sua empresa<br>precisa começar?",
            "Se preferir conversar antes de ler ou escolher um serviço, fale com a nossa equipe.")
        + "\n  </main>\n"
        + P.rodape()
        + P.modal()
        + P.scripts()
    )
