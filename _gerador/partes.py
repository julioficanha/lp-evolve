# -*- coding: utf-8 -*-
"""Partes compartilhadas das páginas da Evolve (cabeçalho, rodapé, modal, head)."""

SERVICOS = [
    ("servicos-pessoas-relacionamento.html",
     "Pessoas e Relações de Trabalho",
     "Contratar e administrar pessoas com segurança e organização"),
    ("servicos-recrutamento-selecao.html",
     "Recrutamento e Seleção",
     "As pessoas certas nos lugares certos, com curadoria de perfil"),
    ("servicos-riscos-saude.html",
     "Riscos Psicossociais e Saúde Organizacional",
     "Da exigência da NR-1 à gestão real das condições de trabalho"),
    ("servicos-lideranca-desenvolvimento.html",
     "Liderança e Desenvolvimento Humano",
     "Preparar quem conduz pessoas, decisões e resultados"),
]

MARCA_SVG = """<svg class="brand-mark-svg" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <path d="M 36 36 L 22 50 C 16 56 16 64 22 70 L 50 98 L 78 70 C 84 64 84 56 78 50 L 64 36" />
          <path d="M 50 2 C 64 16 64 36 50 46 C 36 56 36 76 50 90 C 64 76 64 56 50 46 C 36 36 36 16 50 2 Z" />
        </svg>"""


def ph_equipe(classes="", titulo="Foto da equipe Evolve Capital Humano", nota=""):
    """Fotografia oficial da equipe reunida."""
    cls = ("ph-equipe " + classes).strip()
    return f"""<div class="{cls}" role="img" aria-label="{titulo}">
          <img src="assets/images/equipe_evolve_editorial.png" alt="{titulo}" style="width:100%;height:100%;object-fit:cover;object-position:center;" loading="eager">
        </div>"""


def head(titulo, descricao, extra_css=""):
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{titulo}</title>
  <meta name="description" content="{descricao}">
  <meta name="theme-color" content="#02173B">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{titulo}">
  <meta property="og:description" content="{descricao}">
  <meta property="og:locale" content="pt_BR">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="style.css">
  <link rel="stylesheet" href="assets/css/system.css?v=20260921-equipe-2">{extra_css}

  <script src="https://cdn.jsdelivr.net/npm/lenis@1.1.18/dist/lenis.min.js" defer></script>
</head>
<body class="bg-editorial">
"""


def cabecalho(ativo):
    """ativo: 'comece' | 'carta' | 'evolve' | 'servicos'"""
    def cls(chave):
        return " active" if chave == ativo else ""

    itens = "\n".join(
        f"""              <a href="{href}" class="dropdown-item" role="menuitem">
                <span class="dropdown-item-title">{nome}</span>
                <span class="dropdown-item-sub">{sub}</span>
              </a>"""
        for href, nome, sub in SERVICOS
    )

    return f"""
  <a class="sr-only" href="#main-content">Ir direto para o conteúdo</a>

  <header class="site-header header-dark" id="site-header">
    <div class="container header-container">

      <a href="index.html" class="brand-link" aria-label="Evolve Capital Humano — página inicial">
        {MARCA_SVG}
        <div class="brand-text-block">
          <span class="brand-name">EVOLVE</span>
          <span class="brand-sub">CAPITAL HUMANO</span>
        </div>
      </a>

      <nav class="main-nav" id="main-nav" aria-label="Navegação principal">
        <ul class="nav-list">
          <li class="nav-item-btn">
            <a href="index.html" class="nav-link-creative{cls('comece')}"><span>COMECE AQUI</span></a>
          </li>
          <li class="nav-item-btn">
            <a href="carta-aberta.html" class="nav-link-creative{cls('carta')}"><span>CARTA ABERTA</span></a>
          </li>
          <li class="nav-item-btn">
            <a href="evolve.html" class="nav-link-creative{cls('evolve')}"><span>EVOLVE</span></a>
          </li>
          <li class="nav-item-btn has-dropdown">
            <a href="servicos.html" class="nav-link-creative{cls('servicos')}" aria-haspopup="true" aria-expanded="false">
              <span>NOSSOS SERVIÇOS</span>
              <svg class="dropdown-arrow" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
            </a>
            <div class="nav-dropdown-menu" role="menu">
{itens}
            </div>
          </li>
        </ul>
      </nav>

      <div class="header-actions">
        <a href="#modal-diagnostico" class="btn btn-terracota btn-header-cta">Vamos conversar</a>
        <button type="button" class="mobile-menu-toggle" id="mobile-menu-toggle" aria-label="Abrir menu de navegação" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>

    </div>
  </header>
"""


def faixa(itens, velocidade="46s"):
    conteudo = "".join(f'<span class="faixa__item">{t}</span>' for t in itens)
    return f"""
  <div class="faixa" style="--faixa-speed: {velocidade}" aria-hidden="true">
    <div class="faixa__track">{conteudo}{conteudo}</div>
  </div>
"""


def cta_final(titulo, subtitulo, botao="Conversar sobre minha empresa", assunto="geral"):
    return f"""
  <section class="section-padding section-cta-final bg-azul-petroleo text-light" id="contato">
    <div class="container text-center">
      <div class="cta-final-box" data-reveal>
        <span class="eyebrow eyebrow-terracota">O próximo passo</span>
        <h2 class="cta-final-title">{titulo}</h2>
        <p class="cta-final-subtitle">{subtitulo}</p>
        <div class="cta-final-actions">
          <button type="button" class="btn btn-terracota btn-xl open-contact-trigger" data-subject="{assunto}" data-verb="conversar">
            <span>{botao}</span>
            <svg class="btn-arrow" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </button>
        </div>
        <p class="provisional-note-light">
          <span class="provisorio provisorio--light">Provisório</span>
          E-mail, telefone e endereço institucionais entram aqui quando os dados oficiais forem liberados.
        </p>
      </div>
    </div>
  </section>
"""


def rodape():
    links_svc = "\n".join(
        f'          <li><a href="{href}">{nome}</a></li>' for href, nome, _ in SERVICOS
    )
    return f"""
  <footer class="site-footer bg-azul-petroleo-deep text-light">
    <div class="container footer-container">
      <div class="footer-brand-col">
        <a href="index.html" class="brand-link">
          {MARCA_SVG}
          <div class="brand-text-block">
            <span class="brand-name">EVOLVE</span>
            <span class="brand-sub">CAPITAL HUMANO</span>
          </div>
        </a>
        <p class="footer-tagline">
          Estruturamos negócios para que pessoas e resultados evoluam juntos.
        </p>
      </div>

      <div class="footer-links-col">
        <h4 class="footer-title">Navegação</h4>
        <ul class="footer-links">
          <li><a href="index.html">Comece Aqui</a></li>
          <li><a href="evolve.html">A Evolve</a></li>
          <li><a href="servicos.html">Nossos Serviços</a></li>
        </ul>
      </div>

      <div class="footer-links-col">
        <h4 class="footer-title">Soluções</h4>
        <ul class="footer-links">
{links_svc}
        </ul>
      </div>

      <div class="footer-info-col">
        <h4 class="footer-title">Atendimento</h4>
        <p class="footer-info-text">Atuação nacional, em todo o Brasil.</p>
        <p class="footer-info-text">Foco em PMEs de 5 a 200 colaboradores.</p>
        <p class="footer-info-text" style="margin-top:1rem">
          <span class="provisorio provisorio--light">Provisório</span>
        </p>
        <p class="footer-info-text">Contatos institucionais a confirmar.</p>
      </div>
    </div>

    <div class="footer-bottom container">
      <p class="copyright">&copy; 2026 Evolve Capital Humano. Todos os direitos reservados.</p>
    </div>
  </footer>
"""


def modal(titulo="Conversar com a Evolve",
          subtitulo="Preencha os dados abaixo para que a nossa equipe compreenda o cenário atual da sua empresa."):
    opcoes = "\n".join(
        f'            <option value="{href.replace(".html","")}">{nome}</option>'
        for href, nome, _ in SERVICOS
    )
    return f"""
  <div class="modal-backdrop" id="contact-modal" aria-hidden="true" role="dialog" aria-modal="true" aria-labelledby="modal-title">
    <div class="modal-dialog">
      <button type="button" class="modal-close-btn" id="modal-close-btn" aria-label="Fechar">&times;</button>

      <div class="modal-header text-center">
        <span class="eyebrow eyebrow-terracota">Atendimento sob medida</span>
        <h2 class="modal-title" id="modal-title">{titulo}</h2>
        <p class="modal-subtitle">{subtitulo}</p>
      </div>

      <form class="modal-form" id="contact-form">
        <div class="form-group">
          <label for="form-name">Seu nome completo</label>
          <input type="text" id="form-name" name="nome" required autocomplete="name" placeholder="Nome e sobrenome">
        </div>
        <div class="form-group">
          <label for="form-company">Nome da sua empresa</label>
          <input type="text" id="form-company" name="empresa" required autocomplete="organization" placeholder="Razão social ou nome fantasia">
        </div>
        <div class="form-row">
          <div class="form-group">
            <label for="form-email">E-mail profissional</label>
            <input type="email" id="form-email" name="email" required autocomplete="email" placeholder="nome@suaempresa.com.br">
          </div>
          <div class="form-group">
            <label for="form-phone">Telefone / WhatsApp</label>
            <input type="tel" id="form-phone" name="whatsapp" required autocomplete="tel" placeholder="(00) 00000-0000">
          </div>
        </div>
        <div class="form-group">
          <label for="form-subject">Frente de interesse</label>
          <select id="form-subject" name="servico">
            <option value="geral">Estruturação de gestão (visão geral)</option>
{opcoes}
          </select>
        </div>
        <div class="form-group">
          <label for="form-message">Conte, em poucas linhas, o seu principal desafio hoje</label>
          <textarea id="form-message" name="desafio" rows="3" placeholder="Ex.: as decisões operacionais passam quase todas por mim e preciso preparar a minha linha de gestores."></textarea>
        </div>
        <button type="submit" class="btn btn-terracota btn-block btn-lg" data-verb="enviar"><span>Enviar mensagem</span></button>
        <p class="provisional-note" style="margin-top:1rem;font-size:0.72rem;line-height:1.5;color:var(--verde-acinzentado)">
          <span class="provisorio">Provisório</span>
          O destino do formulário será ligado ao canal oficial da Evolve (e-mail ou Google Forms com notificação).
        </p>
      </form>
    </div>
  </div>
"""


def scripts(extra=""):
    return f"""
  <script src="assets/js/app.js" defer></script>{extra}
</body>
</html>
"""
