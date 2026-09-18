# -*- coding: utf-8 -*-
"""EVOLVE — página institucional reformulada: fundo branco, novo texto, equipe em destaque e verticalizada."""
import partes as P

TITULO = "A Evolve — quem somos, como trabalhamos e o que já construímos"
DESC = ("A história, a equipe, a cultura e a rede da Evolve Capital Humano: uma consultoria de "
        "estruturação de pequenas e médias empresas, com atuação nacional e mais de 10.000 pessoas impactadas.")

HERO = """
  <main id="main-content">

    <section class="svc-hero svc-hero--claro">
      <div class="svc-hero__text">
        <span class="svc-hero__index">Bem-vindo à Evolve</span>
        <h1 class="svc-hero__title rise" style="font-size:clamp(2.1rem,5vw,3.5rem);margin-bottom:1rem">
          O ser humano, a estrutura do negócio, o resultado financeiro.
        </h1>
        <p class="svc-hero__q" data-reveal style="--d:300ms">
          Somos a favor da tecnologia, do lucro, da hierarquia e da mudança. Também não aceitamos que 
          esses elementos justifiquem relações que adoecem, processos que aprisionam ou resultados que 
          não se sustentam. É contra isso que lutamos.
        </p>

        <div class="svc-hero__actions" data-reveal style="--d:480ms">
          <a href="servicos.html" class="btn btn-terracota btn-lg" data-verb="conhecer">
            <span>Conheça nossos serviços</span>
            <svg class="btn-arrow" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </a>
          <a href="carta-aberta.html" class="btn btn-outline-dark btn-lg" data-verb="ler"><span>Leia a carta do empresário</span></a>
          <a href="#equipe" class="btn btn-link-dark btn-lg" data-verb="conhecer"><span>Conheça nossa equipe</span></a>
        </div>
      </div>
      """ + P.ph_equipe("svc-hero__visual") + """
    </section>

    <!-- QUEM FAZ — EQUIPE (4 MEMBROS VERTICAIS COM IMAGEM NA LATERAL) -->
    <section class="rede" id="equipe" style="background:var(--off-white);padding:clamp(4rem,8vw,6.5rem) 0">
      <div class="u-wrap">
        <div class="bloco__head" data-reveal>
          <span class="no-secao"><span class="no-secao__dot"></span>Quem faz</span>
          <h2 class="bloco__title" style="margin-top:1.25rem;color:var(--azul-petroleo)">Uma rede, não um escritório.</h2>
          <p style="margin-top:0.75rem;font-size:1.05rem;line-height:1.6;color:var(--azul-cinza);max-width:65ch">
            Conheça os responsáveis técnicos que conduzem as áreas de gestão de pessoas, processos, finanças, departamento pessoal e desenvolvimento organizacional da Evolve.
          </p>
        </div>

        <div class="equipe-vert-list" data-stagger="120">

          <!-- 1º Membro: Amanda Cristina Favaretto -->
          <article class="equipe-card-vert" data-reveal>
            <div class="equipe-card-vert__frame">
              <img src="assets/images/amanda.png" alt="Foto oficial de Amanda Cristina Favaretto — Psicóloga (CRP-08/35489)" style="width:100%;height:100%;object-fit:cover;object-position:center 15%" loading="lazy">
            </div>
            <div class="equipe-card-vert__content">
              <span class="equipe-card-vert__badge">Gestão de Pessoas & DHO</span>
              <h3 class="equipe-card-vert__name">Amanda Cristina Favaretto <span style="font-size:1.05rem;font-weight:600;color:var(--verde-acinzentado)">(CRP-08/35489)</span></h3>
              <div class="equipe-card-vert__role">
                Responsável técnica pela área de Gestão de Pessoas, Riscos Psicossociais e Desenvolvimento Organizacional · Psicóloga
              </div>
              <div class="equipe-card-vert__credentials">
                Psicóloga (CRP-08/35489) · Especialista em Psicologia Organizacional · Certificação Internacional em Segurança Psicológica
              </div>
              <p class="equipe-card-vert__bio">
                Psicóloga (CRP-08/35489) especialista em Psicologia Organizacional e Mentoria de Lideranças, com formação em Análise do Comportamento e Neurociência. Possui Certificação Internacional em Segurança Psicológica. Como administradora da Evolve, lidera a gestão de pessoas, governança, cultura, fatores psicossociais (NR-1) e soluções tecnológicas aplicadas (IA em RH), transformando ciência em resultados práticos.
              </p>
              <div class="equipe-card-vert__tags">
                <span class="equipe-card-vert__tag">Psicóloga (CRP-08/35489)</span>
                <span class="equipe-card-vert__tag">Segurança Psicológica (Internacional)</span>
                <span class="equipe-card-vert__tag">Neurociência & Comportamento</span>
                <span class="equipe-card-vert__tag">Gestão de Pessoas & DHO</span>
                <span class="equipe-card-vert__tag">IA & Modelos Preditivos</span>
              </div>
            </div>
          </article>

          <!-- 2º Membro: Simone Ap. Luciano -->
          <article class="equipe-card-vert" data-reveal>
            <div class="equipe-card-vert__frame">
              <img src="assets/images/simone.jpg" alt="Foto oficial de Simone Ap. Luciano — Gestora de Operações de DP e R&S" style="width:100%;height:100%;object-fit:cover;object-position:center 15%" loading="lazy">
            </div>
            <div class="equipe-card-vert__content">
              <span class="equipe-card-vert__badge">Operações de DP & R&S</span>
              <h3 class="equipe-card-vert__name">Simone Ap. Luciano</h3>
              <div class="equipe-card-vert__role">
                Gestora de Operações de Departamento Pessoal e Recrutamento e Seleção · Responsável técnica pela área de Departamento Pessoal e Recrutamento e Seleção
              </div>
              <div class="equipe-card-vert__credentials">
                Graduada em Ciências Contábeis · Pós-graduada em Gestão Empresarial (ênfase em Gestão de Pessoas) · +20 Anos de Experiência
              </div>
              <p class="equipe-card-vert__bio">
                Especialista em Gestão de Pessoas e Recursos Humanos com mais de 20 anos de atuação estratégica. Graduada em Ciências Contábeis e pós em Gestão Empresarial, une visão financeira e prática de negócio ao trabalhar diretamente ao lado da alta direção. Conduz a estruturação de DP, DHO, R&S e relações trabalhistas — construindo soluções sob medida orientadas a resultados.
              </p>
              <div class="equipe-card-vert__tags">
                <span class="equipe-card-vert__tag">+20 Anos de Experiência</span>
                <span class="equipe-card-vert__tag">Ciências Contábeis & Negócios</span>
                <span class="equipe-card-vert__tag">Parceria com Alta Direção</span>
                <span class="equipe-card-vert__tag">DP & Conformidade</span>
                <span class="equipe-card-vert__tag">Recrutamento & Seleção</span>
              </div>
            </div>
          </article>

          <!-- 3º Membro: Rita -->
          <article class="equipe-card-vert" data-reveal>
            <div class="equipe-card-vert__frame">
              <img src="assets/images/rita.jpg" alt="Foto oficial de Rita — Responsável técnica pela área de Processos e Finanças" style="width:100%;height:100%;object-fit:cover;object-position:center 15%" loading="lazy">
            </div>
            <div class="equipe-card-vert__content">
              <span class="equipe-card-vert__badge">Processos & Finanças</span>
              <h3 class="equipe-card-vert__name">Rita</h3>
              <div class="equipe-card-vert__role">
                Responsável técnica pela área de Processos e Finanças
              </div>
              <div class="equipe-card-vert__credentials">
                Responsabilidade Técnica · Mapeamento de Processos · Gestão Financeira · DRE & Custos Operacionais
              </div>
              <p class="equipe-card-vert__bio">
                Responsável pela liderança técnica na estruturação financeira e revisão contínua dos fluxos operacionais da empresa. Garante a integração entre organização de rotinas, controle de custos e governança de processos, viabilizando eficiência e previsibilidade para o negócio.
              </p>
              <div class="equipe-card-vert__tags">
                <span class="equipe-card-vert__tag">Mapeamento de Processos</span>
                <span class="equipe-card-vert__tag">Gestão Financeira</span>
                <span class="equipe-card-vert__tag">DRE & Orçamentos</span>
                <span class="equipe-card-vert__tag">Organização Operacional</span>
              </div>
            </div>
          </article>

          <!-- 4º Membro: Guilherme (Último) -->
          <article class="equipe-card-vert" data-reveal>
            <div class="equipe-card-vert__frame">
              <img src="assets/images/guilherme.png" alt="Foto oficial de Guilherme — Implantação de Processos e Riscos Psicossociais" style="width:100%;height:100%;object-fit:cover;object-position:center 15%" loading="lazy">
            </div>
            <div class="equipe-card-vert__content">
              <span class="equipe-card-vert__badge">Implantação & Riscos Psicossociais</span>
              <h3 class="equipe-card-vert__name">Guilherme</h3>
              <div class="equipe-card-vert__role">
                Atua na implantação de processos de gestão de pessoas e planos e ações de riscos psicossociais
              </div>
              <div class="equipe-card-vert__credentials">
                Implantação Prática · Gestão de Processos de Pessoas · Planos de Ação NR-1 · Execução no Dia a Dia
              </div>
              <p class="equipe-card-vert__bio">
                Atuação prática na implantação de métodos de gestão de pessoas e rotinas operacionais nas empresas. Conduz a execução de planos de ação diretos para mitigação de riscos psicossociais (NR-1), garantindo alinhamento de processos e aplicação efetiva no ambiente de trabalho.
              </p>
              <div class="equipe-card-vert__tags">
                <span class="equipe-card-vert__tag">Implantação Prática</span>
                <span class="equipe-card-vert__tag">Riscos Psicossociais (NR-1)</span>
                <span class="equipe-card-vert__tag">Processos de RH</span>
                <span class="equipe-card-vert__tag">Execução & Acompanhamento</span>
              </div>
            </div>
          </article>

        </div>

        <p style="margin-top:2.5rem;font-size:0.82rem;line-height:1.6;color:var(--azul-petroleo);opacity:0.75;max-width:65ch">
          <span class="provisorio">Evolve Capital Humano</span>
          Equipe técnica multidisciplinar em atuação contínua e integrada em todo o território nacional.
        </p>
      </div>
    </section>

    <!-- COMPETÊNCIAS E AUTORIDADE TÉCNICA DILUÍDAS AO LONGO DA PÁGINA -->
    <section class="bloco" style="background:var(--off-white-card);padding:clamp(4.5rem,8vw,6.5rem) 0">
      <div class="u-wrap">
        <div class="bloco__head" data-reveal>
          <span class="no-secao"><span class="no-secao__dot"></span>Pilares & Habilidades da Equipe</span>
          <h2 class="bloco__title" style="margin-top:1.25rem;color:var(--azul-petroleo)">Conhecimento científico, prática corporativa e visão de negócio.</h2>
          <p style="margin-top:0.75rem;font-size:1.05rem;line-height:1.6;color:var(--azul-cinza);max-width:65ch">
            A autoridade do time Evolve se consolida na união de especialidades técnicas que transformam desafios humanos e operacionais em resultados reais para a organização.
          </p>
        </div>

        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:2rem;margin-top:3rem">
          
          <div class="card-metodo" data-reveal style="background:#FFFFFF;border:1px solid rgba(2,23,59,0.08);border-radius:1.25rem;padding:2rem;box-shadow:0 6px 20px rgba(2,23,59,0.03)">
            <span style="font-size:0.75rem;font-weight:700;color:var(--terracota);text-transform:uppercase;letter-spacing:0.08em;display:block;margin-bottom:0.6rem">Gestão Corporativa & Negócios</span>
            <h3 style="font-family:var(--font-serif);font-size:1.3rem;font-weight:700;color:var(--azul-petroleo);margin-bottom:0.75rem">Visão de Negócio & Liderança em RH</h3>
            <p style="font-size:0.92rem;line-height:1.6;color:var(--azul-cinza)">
              Com mais de 20 anos de atuação estratégica liderados por <strong>Simone Ap. Luciano</strong> (graduada em Ciências Contábeis e pós em Gestão Empresarial), une-se a prática contábil à gestão corporativa. Atuação direta ao lado da alta direção para conectar pessoas, rotinas de DP, DHO e R&S aos objetivos de sustentabilidade e lucratividade do negócio.
            </p>
          </div>

          <div class="card-metodo" data-reveal style="--d:100ms;background:#FFFFFF;border:1px solid rgba(2,23,59,0.08);border-radius:1.25rem;padding:2rem;box-shadow:0 6px 20px rgba(2,23,59,0.03)">
            <span style="font-size:0.75rem;font-weight:700;color:var(--terracota);text-transform:uppercase;letter-spacing:0.08em;display:block;margin-bottom:0.6rem">Psicologia & Segurança Psicológica</span>
            <h3 style="font-family:var(--font-serif);font-size:1.3rem;font-weight:700;color:var(--azul-petroleo);margin-bottom:0.75rem">Governança & Riscos Psicossociais</h3>
            <p style="font-size:0.92rem;line-height:1.6;color:var(--azul-cinza)">
              Responsabilidade técnica de <strong>Amanda Cristina Favaretto (CRP-08/35489)</strong>, especialista em Psicologia Organizacional com Certificação Internacional em Segurança Psicológica. Aplica Análise do Comportamento e Neurociência na gestão de fatores de riscos psicossociais (NR-1), mentoria de lideranças e cultura corporativa.
            </p>
          </div>

          <div class="card-metodo" data-reveal style="--d:200ms;background:#FFFFFF;border:1px solid rgba(2,23,59,0.08);border-radius:1.25rem;padding:2rem;box-shadow:0 6px 20px rgba(2,23,59,0.03)">
            <span style="font-size:0.75rem;font-weight:700;color:var(--terracota);text-transform:uppercase;letter-spacing:0.08em;display:block;margin-bottom:0.6rem">Inovação & Inteligência Artificial</span>
            <h3 style="font-family:var(--font-serif);font-size:1.3rem;font-weight:700;color:var(--azul-petroleo);margin-bottom:0.75rem">Tecnologia Aplicada a Pessoas</h3>
            <p style="font-size:0.92rem;line-height:1.6;color:var(--azul-cinza)">
              Desenvolvimento e aplicação de soluções tecnológicas de ponta na Psicologia Organizacional e RH: avaliação socioemocional, diagnóstico de cultura por dados, modelos preditivos aplicados ao contexto de trabalho e inteligência artificial para potencializar a análise de perfil e retenção de talentos.
            </p>
          </div>

          <div class="card-metodo" data-reveal style="--d:300ms;background:#FFFFFF;border:1px solid rgba(2,23,59,0.08);border-radius:1.25rem;padding:2rem;box-shadow:0 6px 20px rgba(2,23,59,0.03)">
            <span style="font-size:0.75rem;font-weight:700;color:var(--terracota);text-transform:uppercase;letter-spacing:0.08em;display:block;margin-bottom:0.6rem">Processos & Operação de Campo</span>
            <h3 style="font-family:var(--font-serif);font-size:1.3rem;font-weight:700;color:var(--azul-petroleo);margin-bottom:0.75rem">Estruturação Financeira & Implantação</h3>
            <p style="font-size:0.92rem;line-height:1.6;color:var(--azul-cinza)">
              Integração prática de fluxos conduzida por <strong>Rita</strong> (responsável por Processos e Finanças, DRE e controle de custos) e <strong>Guilherme</strong> (responsável pela implantação em campo de métodos de gestão de pessoas e ações diretas de NR-1), garantindo que os métodos sejam vivenciados e consolidados pela equipe.
            </p>
          </div>

        </div>
      </div>
    </section>

    <!-- NÚMEROS DE IMPACTO -->
    <section class="bloco" style="background:var(--off-white);padding:clamp(3.5rem,7vw,5.5rem) 0">
      <div class="u-wrap">
        <div class="indicadores">
          <div class="indicador" data-reveal>
            <span class="indicador__num"><span class="value">Nacional</span></span>
            <span class="indicador__label">Atuação em todo o território brasileiro.</span>
          </div>
          <div class="indicador" data-reveal style="--d:90ms">
            <span class="indicador__num" data-count="10000" data-count-group="true"><span class="prefix">+</span><span class="value">0</span></span>
            <span class="indicador__label">Pessoas impactadas direta e indiretamente.</span>
          </div>
          <div class="indicador" data-reveal style="--d:180ms">
            <span class="indicador__num" data-count="20"><span class="value">0</span><span class="suffix">anos+</span></span>
            <span class="indicador__label">De experiência em DP e Gestão Estratégica de RH.</span>
          </div>
          <div class="indicador" data-reveal style="--d:270ms">
            <span class="indicador__num"><span class="value">NR-1</span></span>
            <span class="indicador__label">Gestão técnica de Riscos Psicossociais & Saúde.</span>
          </div>
        </div>
      </div>
    </section>

  </main>
"""

def render():
    return (
        P.head(TITULO, DESC)
        + P.cabecalho("evolve")
        + HERO
        + P.cta_final(
            "Uma empresa mais autônoma<br>começa com estrutura.",
            "Converse com a nossa equipe e descubra o próximo movimento para o seu negócio.")
        + "\n  </main>\n"
        + P.rodape()
        + P.modal()
        + P.scripts()
    )
