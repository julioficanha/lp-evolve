/* ==========================================================================
   EVOLVE CAPITAL HUMANO — MOTOR DE INTERAÇÃO
   --------------------------------------------------------------------------
   Princípio: um único laço de animação (rAF) lê o scroll uma vez por quadro e
   distribui para os módulos inscritos. Nada de listeners de scroll espalhados.
   Tudo degrada com elegância: sem JS, o conteúdo continua legível; com
   prefers-reduced-motion, o movimento para e o conteúdo permanece visível.
   ========================================================================== */
(() => {
  'use strict';

  const REDUCED = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const TOUCH   = window.matchMedia('(hover: none), (pointer: coarse)').matches;

  /* ---------------------------------------------------------------- helpers */
  const $  = (sel, ctx = document) => ctx.querySelector(sel);
  const $$ = (sel, ctx = document) => Array.from(ctx.querySelectorAll(sel));
  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
  const lerp  = (a, b, t) => a + (b - a) * t;
  /* progresso de um elemento atravessando a viewport: 0 ao entrar, 1 ao sair */
  const crossProgress = (rect, vh) =>
    clamp((vh - rect.top) / (vh + rect.height));

  /* ------------------------------------------------------- laço central rAF */
  const frame = {
    subs: [],
    y: 0,
    lastY: 0,
    dir: 1,
    vh: window.innerHeight,
    docH: 1,
    running: false,
    add(fn) { this.subs.push(fn); return fn; },
    measure() {
      this.vh = window.innerHeight;
      this.docH = Math.max(1, document.documentElement.scrollHeight - this.vh);
    },
    tick() {
      const y = window.scrollY || window.pageYOffset || 0;
      if (Math.abs(y - frame.y) > 0.4) frame.dir = y > frame.y ? 1 : -1;
      frame.lastY = frame.y;
      frame.y = y;
      for (let i = 0; i < frame.subs.length; i++) frame.subs[i](frame);
      requestAnimationFrame(frame.tick);
    },
    start() {
      if (this.running) return;
      this.running = true;
      this.measure();
      requestAnimationFrame(this.tick);
      window.addEventListener('resize', () => this.measure(), { passive: true });
    }
  };

  /* ------------------------------------------------- 01. scroll suave Lenis */
  function initSmoothScroll() {
    if (REDUCED || typeof window.Lenis === 'undefined') return null;
    const lenis = new window.Lenis({
      duration: 0.85,
      easing: (t) => 1 - Math.pow(1 - t, 3.2),  /* desacelera sem arrastar */
      smoothWheel: true,
      wheelMultiplier: 1.0,
      touchMultiplier: 1.4,
      lerp: 0.11
    });
    const raf = (t) => { lenis.raf(t); requestAnimationFrame(raf); };
    requestAnimationFrame(raf);
    window.lenis = lenis;

    /* âncoras internas passam a usar o Lenis */
    document.addEventListener('click', (e) => {
      const a = e.target.closest('a[href^="#"]');
      if (!a) return;
      const id = a.getAttribute('href');
      if (!id || id === '#') return;
      const target = document.querySelector(id);
      if (!target) return;
      e.preventDefault();
      lenis.scrollTo(target, { offset: -96, duration: 1.1 });
    });
    return lenis;
  }

  /* -------------------------------------------- 02. revelação ao entrar em cena
     Um único IntersectionObserver serve a todos os seletores de revelação.
     Elementos com data-stagger distribuem o atraso entre os filhos.          */
  function initReveal() {
    const SELECTOR = '[data-reveal], [data-reveal-rule], .rise, .no-secao, .rotina__step, .pull-frame';
    const nodes = $$(SELECTOR);
    if (!nodes.length) return;

    if (REDUCED) {
      nodes.forEach((n) => { n.classList.add('is-in', 'revealed'); });
      return;
    }

    /* distribui atrasos dentro de contêineres marcados */
    $$('[data-stagger]').forEach((group) => {
      const step = parseInt(group.dataset.stagger, 10) || 90;
      $$(':scope > *', group).forEach((child, i) => {
        child.style.setProperty('--d', `${i * step}ms`);
      });
    });

    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-in', 'revealed');
        io.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.12 });

    nodes.forEach((n) => io.observe(n));
  }

  /* ------------------------------------------------- 03. FOTOS QUE SÃO PUXADAS
     A moldura tem overflow oculto e a imagem, escalada, desloca em sentido
     contrário ao scroll. O olho lê como se a foto estivesse sendo arrancada
     de dentro do papel — não como um parallax de fundo.                      */
  function initPull() {
    if (REDUCED) return;
    const items = $$('[data-pull]').map((el) => ({
      el,
      amount: parseFloat(el.dataset.pull) || 64,
      host: el.closest('.pull-frame, .hero-solidao__visual, .svc-hero__visual, .cena__stage') || el.parentElement
    }));
    if (!items.length) return;

    frame.add(({ vh }) => {
      for (const it of items) {
        const r = it.host.getBoundingClientRect();
        if (r.bottom < -200 || r.top > vh + 200) continue;
        const p = crossProgress(r, vh);          /* 0 → 1 */
        const offset = (p - 0.5) * -2 * it.amount;
        it.el.style.setProperty('--pull', `${offset.toFixed(2)}px`);
      }
    });
  }

  /* ------------------------------------- 04. FIO DE PROGRESSO (linha contínua)
     A curva S da marca vira um fio de 1px na borda da tela que se desenha
     conforme a leitura avança. Discreto por decisão: é assinatura, não enfeite. */
  function initFio() {
    if (REDUCED || TOUCH) return;
    const fio = document.createElement('div');
    fio.className = 'fio-progresso';
    fio.innerHTML = '<span class="fio-progresso__fill"></span><span class="fio-progresso__knob"></span>';
    document.body.appendChild(fio);
    const fill = $('.fio-progresso__fill', fio);
    const knob = $('.fio-progresso__knob', fio);
    let smooth = 0;

    frame.add(({ y, docH, vh }) => {
      const target = clamp(y / docH);
      smooth = lerp(smooth, target, 0.12);
      fill.style.transform = `scaleY(${smooth.toFixed(4)})`;
      knob.style.transform = `translateY(${(smooth * (vh - 24)).toFixed(1)}px)`;
    });
  }

  /* ------------------------------------------------ 05. CURSOR DE CAMPO
     Anel fino que segue o ponteiro com inércia. Sobre elementos marcados com
     data-verb, abre e mostra o verbo daquela ação. É a única "mágica" que o
     usuário controla diretamente com a mão.                                  */
  function initCursor() {
    if (REDUCED || TOUCH) return;
    const cur = document.createElement('div');
    cur.className = 'campo-cursor';
    cur.innerHTML = '<span class="campo-cursor__verb"></span>';
    document.body.appendChild(cur);
    const verb = $('.campo-cursor__verb', cur);

    let tx = window.innerWidth / 2, ty = window.innerHeight / 2;
    let cx = tx, cy = ty;

    window.addEventListener('pointermove', (e) => {
      tx = e.clientX; ty = e.clientY;
      cur.classList.add('is-on');
      const hit = e.target.closest('[data-verb]');
      if (hit) {
        cur.classList.add('is-wide');
        verb.textContent = hit.dataset.verb;
      } else {
        cur.classList.remove('is-wide');
      }
    }, { passive: true });

    window.addEventListener('pointerleave', () => cur.classList.remove('is-on'));

    const run = () => {
      cx = lerp(cx, tx, 0.19);
      cy = lerp(cy, ty, 0.19);
      cur.style.transform = `translate3d(${cx.toFixed(1)}px, ${cy.toFixed(1)}px, 0)`;
      requestAnimationFrame(run);
    };
    requestAnimationFrame(run);
  }

  /* ----------------------------------------- 06. CONTADORES COM INÉRCIA
     Sobe rápido, passa um pouco do alvo e assenta — como um ponteiro real.
     Roda uma única vez, quando o número entra em cena.                       */
  function initCounters() {
    const nodes = $$('[data-count]');
    if (!nodes.length) return;

    const render = (el, v) => {
      const dec = parseInt(el.dataset.countDecimals, 10) || 0;
      const val = dec ? v.toFixed(dec) : Math.round(v).toString();
      el.querySelector('.value').textContent =
        el.dataset.countGroup === 'true'
          ? val.replace(/\B(?=(\d{3})+(?!\d))/g, '.')
          : val;
    };

    if (REDUCED) {
      nodes.forEach((el) => render(el, parseFloat(el.dataset.count)));
      return;
    }

    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const el = entry.target;
        io.unobserve(el);
        const target = parseFloat(el.dataset.count);
        const dur = parseInt(el.dataset.countDur, 10) || 1700;
        const t0 = performance.now();
        const step = (now) => {
          const p = clamp((now - t0) / dur);
          /* easing com leve ultrapassagem que assenta no valor exato */
          const e = p < 1
            ? 1 - Math.pow(1 - p, 3) + Math.sin(p * Math.PI) * 0.045 * (1 - p)
            : 1;
          render(el, target * e);
          if (p < 1) requestAnimationFrame(step);
          else render(el, target);
        };
        requestAnimationFrame(step);
      });
    }, { threshold: 0.5 });

    nodes.forEach((el) => io.observe(el));
  }

  /* ------------------------------------- 07. TERRITÓRIOS (word ticker vertical)
     Os cinco territórios de comunicação da marca giram dentro da frase-âncora.
     Vertical, não horizontal: a leitura não é interrompida.                   */
  function initTerritorios() {
    $$('.territorio-slot').forEach((slot) => {
      const list = $('.territorio-slot__list', slot);
      if (!list) return;
      const items = $$('.territorio-slot__item', list);
      if (items.length < 2) return;
      /* duplica o primeiro no fim para o retorno ser invisível */
      list.appendChild(items[0].cloneNode(true));
      if (REDUCED) return;

      let i = 0;
      let timer = null;
      const advance = () => {
        i += 1;
        list.style.transition = 'transform 760ms cubic-bezier(0.16,1,0.30,1)';
        list.style.transform = `translateY(-${i * 1.16}em)`;
        if (i === items.length) {
          setTimeout(() => {
            list.style.transition = 'none';
            list.style.transform = 'translateY(0)';
            i = 0;
          }, 780);
        }
      };
      const io = new IntersectionObserver(([e]) => {
        if (e.isIntersecting && !timer) timer = setInterval(advance, 2300);
        else if (!e.isIntersecting && timer) { clearInterval(timer); timer = null; }
      }, { threshold: 0.3 });
      io.observe(slot);
    });
  }

  /* -------------------------------- 08. FAIXA que inverte com o sentido do scroll
     Diferente de um marquee comum: o sentido da faixa segue o sentido da
     leitura. Rolando para baixo, corre para a esquerda; para cima, inverte.  */
  function initFaixa() {
    const faixas = $$('.faixa');
    if (!faixas.length || REDUCED) return;
    frame.add(({ dir }) => {
      const val = dir < 0 ? 'reverse' : 'forward';
      for (const f of faixas) {
        if (f.dataset.dir !== val) f.dataset.dir = val;
      }
    });
  }

  /* --------------------------------------- 09. ANTES → DEPOIS COM SCRUB
     Cada linha tem um progresso 0→1. O scroll o move; o ponteiro sobre a linha
     assume o controle; arrastar trava o valor. O "antes" perde nitidez, o
     "depois" ganha. A transformação não é ilustrada: é operada pelo leitor.  */
  function initScrub() {
    const rows = $$('.scrub-row');
    if (!rows.length) return;

    if (REDUCED) { rows.forEach((r) => r.style.setProperty('--p', 1)); return; }

    const state = rows.map((row) => ({
      row,
      p: 0,
      manual: false,
      fill: $('.fill', row),
      handle: $('.scrub-row__handle', row),
      len: 0
    }));

    state.forEach((s) => {
      if (s.fill && s.fill.getTotalLength) {
        s.len = s.fill.getTotalLength();
        s.fill.style.strokeDasharray = s.len;
        s.fill.style.strokeDashoffset = s.len;
        s.fill.style.transition = 'stroke-dashoffset 160ms linear';
      }
      /* controle pelo ponteiro */
      s.row.addEventListener('pointermove', (e) => {
        const r = s.row.getBoundingClientRect();
        s.manual = true;
        s.p = clamp((e.clientX - r.left) / r.width);
        paint(s);
      });
      s.row.addEventListener('pointerleave', () => { s.manual = false; });
      s.row.addEventListener('pointerdown', () => s.row.classList.add('is-dragging'));
      window.addEventListener('pointerup', () => s.row.classList.remove('is-dragging'));
    });

    function paint(s) {
      s.row.style.setProperty('--p', s.p.toFixed(3));
      if (s.fill && s.len) s.fill.style.strokeDashoffset = (s.len * (1 - s.p)).toFixed(2);
      if (s.handle) s.handle.style.left = `calc(${(s.p * 100).toFixed(2)}% - 5.5px)`;
    }

    frame.add(({ vh }) => {
      for (const s of state) {
        if (s.manual) continue;
        const r = s.row.getBoundingClientRect();
        if (r.bottom < 0 || r.top > vh) continue;
        /* a linha completa a transformação enquanto cruza o terço central */
        const raw = (vh * 0.78 - r.top) / (r.height + vh * 0.34);
        const p = clamp(raw);
        if (Math.abs(p - s.p) > 0.002) { s.p = p; paint(s); }
      }
    });
  }

  /* ------------------------------------------ 10. CENA FIXADA EM TRÊS TEMPOS
     A seção tem 3 alturas de tela. O palco fica fixo e os tempos se sucedem:
     (1) a chegada em casa, (2) a mensagem que chega, (3) o reconhecimento.
     O zoom da foto avança devagar durante todo o trecho.                     */
  function initCena() {
    const cena = $('.cena');
    if (!cena) return;
    const beats  = $$('.cena__beat', cena);
    const ping   = $('.cena__ping', cena);
    const bg     = $('.cena__bg', cena);
    const deep   = $('.cena__veil--deep', cena);
    const pips   = $$('.cena__progress span', cena);
    const total  = beats.length || 1;

    if (REDUCED) {
      beats.forEach((b) => b.classList.add('is-live'));
      if (ping) ping.classList.add('is-live');
      pips.forEach((p) => p.classList.add('is-done'));
    } else {
      frame.add(({ vh }) => {
        const r = cena.getBoundingClientRect();
        if (r.bottom < 0 || r.top > vh) return;
        const scrollable = Math.max(1, cena.offsetHeight - vh);
        const p = clamp(-r.top / scrollable);

        /* qual tempo está no ar */
        const idx = Math.min(total - 1, Math.floor(p * total * 0.999));
        beats.forEach((b, i) => b.classList.toggle('is-live', i === idx));
        pips.forEach((s, i) => s.classList.toggle('is-done', i <= idx));

        /* a mensagem chega no segundo tempo */
        if (ping) ping.classList.toggle('is-live', p > 0.30);

        /* zoom lento e véu que fecha no final */
        if (bg)  bg.style.setProperty('--cena-zoom', (1.02 + p * 0.06).toFixed(4));
        if (deep) deep.style.setProperty('--veil', (clamp((p - 0.62) / 0.38) * 0.55).toFixed(3));
      });
    }

    /* cartão de evidência */
    const openers  = $$('[data-open-evidence]', cena);
    const evidence = $('.cena__evidence', cena);
    const closeBtn = $('.cena__evidence-close', cena);
    if (evidence) {
      openers.forEach((btn) => btn.addEventListener('click', (e) => {
        e.preventDefault();
        evidence.classList.toggle('is-open');
      }));
      if (closeBtn) closeBtn.addEventListener('click', () => evidence.classList.remove('is-open'));
      document.addEventListener('click', (e) => {
        if (!evidence.classList.contains('is-open')) return;
        if (evidence.contains(e.target) || e.target.closest('[data-open-evidence]')) return;
        evidence.classList.remove('is-open');
      });
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') evidence.classList.remove('is-open');
      });
    }
  }

  /* -------------------------------- 11. ORDEM A PARTIR DO RUÍDO (canvas 2D)
     Traços curtos em ângulos aleatórios que, conforme a seção é lida, giram
     até se alinharem numa malha perfeita. É a tese da marca desenhada:
     a mesma matéria, reorganizada, deixa de ser ruído e passa a ser estrutura. */
  function initOrdem() {
    const canvas = $('.ordem__canvas');
    if (!canvas || REDUCED) return;
    const host = canvas.closest('.ordem');
    const ctx = canvas.getContext('2d');
    let dots = [];
    let dpr = Math.min(2, window.devicePixelRatio || 1);
    let progress = 0, shown = 0;

    function build() {
      const w = host.offsetWidth, h = host.offsetHeight;
      canvas.width = w * dpr;
      canvas.height = h * dpr;
      canvas.style.width = w + 'px';
      canvas.style.height = h + 'px';
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

      const gap = w < 760 ? 38 : 52;
      const cols = Math.ceil(w / gap) + 1;
      const rows = Math.ceil(h / gap) + 1;
      dots = [];
      for (let i = 0; i < cols; i++) {
        for (let j = 0; j < rows; j++) {
          dots.push({
            x: i * gap + gap / 2,
            y: j * gap + gap / 2,
            a0: Math.random() * Math.PI * 2,          /* ângulo caótico  */
            jx: (Math.random() - 0.5) * gap * 0.55,   /* desvio inicial  */
            jy: (Math.random() - 0.5) * gap * 0.55,
            len: gap * 0.40
          });
        }
      }
    }

    function draw() {
      const w = parseFloat(canvas.style.width), h = parseFloat(canvas.style.height);
      ctx.clearRect(0, 0, w, h);
      const t = shown;
      /* ease para que o alinhamento aconteça no miolo da leitura */
      const e = t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
      for (const d of dots) {
        const ang = d.a0 * (1 - e);
        const x = d.x + d.jx * (1 - e);
        const y = d.y + d.jy * (1 - e);
        const dx = Math.cos(ang) * d.len;
        const dy = Math.sin(ang) * d.len;
        ctx.beginPath();
        ctx.moveTo(x - dx / 2, y - dy / 2);
        ctx.lineTo(x + dx / 2, y + dy / 2);
        /* o traço esquenta em terracota à medida que encontra o eixo */
        ctx.strokeStyle = `rgba(${lerp(126, 155, e).toFixed(0)}, ${lerp(113, 81, e).toFixed(0)}, ${lerp(97, 47, e).toFixed(0)}, ${(0.22 + e * 0.30).toFixed(3)})`;
        ctx.lineWidth = 1;
        ctx.lineCap = 'round';
        ctx.stroke();
      }
    }

    build();
    frame.add(({ vh }) => {
      const r = host.getBoundingClientRect();
      if (r.bottom < -100 || r.top > vh + 100) return;
      progress = clamp((vh * 0.9 - r.top) / (r.height + vh * 0.5));
      shown = lerp(shown, progress, 0.09);
      draw();
    });
    window.addEventListener('resize', () => { dpr = Math.min(2, window.devicePixelRatio || 1); build(); draw(); }, { passive: true });
  }

  /* ------------------------------------------- 12. HAIRLINE MAGNÉTICA (cards)
     Nada de tilt 3D. O que se move é o fio: um segmento terracota corre pela
     borda superior acompanhando o ponteiro. Sutil e proprietário.            */
  function initMag() {
    if (TOUCH) return;
    $$('.mag').forEach((card) => {
      card.addEventListener('pointermove', (e) => {
        const r = card.getBoundingClientRect();
        const px = clamp((e.clientX - r.left) / r.width);
        /* o segmento tem 6rem; centraliza no ponteiro sem passar das bordas */
        card.style.setProperty('--mx', `${(px * 100).toFixed(1)}`);
        const seg = 96; /* px aproximados de 6rem */
        const max = Math.max(0, r.width - seg);
        card.style.setProperty('--mx', `0`);
        card.style.setProperty('--seg-x', `${(clamp((e.clientX - r.left - seg / 2) / (max || 1)) * max).toFixed(1)}px`);
      }, { passive: true });
    });
  }

  /* ------------------------------------------------------ 13. CABEÇALHO
     Compacta e ganha fundo sólido ao sair do topo; recolhe ao descer e
     reaparece ao subir, para não competir com a leitura.                     */
  function initHeader() {
    const header = $('#site-header');
    if (!header) return;
    let hidden = false;
    frame.add(({ y, dir }) => {
      header.classList.toggle('is-compact', y > 40);
      const shouldHide = dir > 0 && y > 420;
      if (shouldHide !== hidden) {
        hidden = shouldHide;
        header.classList.toggle('is-tucked', hidden);
      }
    });
  }

  /* --------------------------------------------- 14. NAV ATIVA + MENU MÓVEL */
  function initNav() {
    const page = (location.pathname.split('/').pop() || 'index.html').toLowerCase();
    $$('.nav-link-creative').forEach((link) => {
      const href = (link.getAttribute('href') || '').toLowerCase();
      link.classList.remove('active');
      const isHome = page === '' || page === 'index.html' || page === 'comece-aqui.html';
      if (href === page) link.classList.add('active');
      else if (isHome && (href === 'index.html' || href === 'comece-aqui.html')) link.classList.add('active');
      else if (page.startsWith('servicos') && href === 'servicos.html') link.classList.add('active');
    });

    const toggle = $('#mobile-menu-toggle');
    const nav = $('#main-nav');
    if (toggle && nav) {
      toggle.addEventListener('click', () => {
        const open = nav.classList.toggle('mobile-active');
        toggle.setAttribute('aria-expanded', String(open));
        document.body.style.overflow = open ? 'hidden' : '';
      });
      $$('.nav-item-btn.has-dropdown > .nav-link-creative').forEach((btn) => {
        btn.addEventListener('click', (e) => {
          if (window.innerWidth <= 900) {
            e.preventDefault();
            btn.parentElement.classList.toggle('mobile-open');
          }
        });
      });
    }
  }

  /* ------------------------------------------------- 15. ACORDEÕES (FAQ/pilares) */
  function initAccordions() {
    /* FAQ — um aberto por vez */
    const faqItems = $$('.faq-item');
    faqItems.forEach((item) => {
      const trigger = $('.faq-trigger', item);
      const content = $('.faq-content', item);
      if (!trigger || !content) return;
      trigger.addEventListener('click', () => {
        const wasOpen = item.classList.contains('active');
        faqItems.forEach((i) => {
          i.classList.remove('active');
          const t = $('.faq-trigger', i), c = $('.faq-content', i);
          if (t) t.setAttribute('aria-expanded', 'false');
          if (c) c.setAttribute('hidden', 'true');
        });
        if (!wasOpen) {
          item.classList.add('active');
          trigger.setAttribute('aria-expanded', 'true');
          content.removeAttribute('hidden');
        }
      });
    });

    /* Pilares culturais — vários podem ficar abertos */
    $$('.pilar').forEach((pilar) => {
      const head = $('.pilar__head', pilar);
      if (!head) return;
      head.addEventListener('click', () => {
        const open = pilar.classList.toggle('is-open');
        head.setAttribute('aria-expanded', String(open));
      });
    });
  }

  /* --------------------------------------------------------- 16. MODAL CONTATO */
  function initModal() {
    const modal = $('#contact-modal');
    if (!modal) return;
    const select = $('#form-subject', modal);
    let lastFocus = null;

    const open = (subject) => {
      lastFocus = document.activeElement;
      modal.classList.add('active');
      modal.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
      if (window.lenis) window.lenis.stop();
      if (subject && select) {
        const opt = Array.from(select.options)
          .find((o) => o.value === subject || o.text.toLowerCase().includes(String(subject).toLowerCase()));
        if (opt) select.value = opt.value;
      }
      const first = modal.querySelector('input, select, textarea, button');
      if (first) setTimeout(() => first.focus(), 60);
    };
    const close = () => {
      modal.classList.remove('active');
      modal.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
      if (window.lenis) window.lenis.start();
      if (lastFocus) lastFocus.focus();
    };

    document.addEventListener('click', (e) => {
      const trigger = e.target.closest('.open-contact-trigger');
      if (trigger) { e.preventDefault(); open(trigger.dataset.subject); return; }
      if (e.target === modal || e.target.closest('#modal-close-btn')) close();
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modal.classList.contains('active')) close();
    });
    window.EvolveModal = { open, close };

    /* Envio do formulário de contato.
       Enquanto o canal oficial não estiver ligado, o registro fica no
       localStorage e no console para conferência. Ver README-ENTREGA.md. */
    const form = $('#contact-form', modal);
    if (form) {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        const dados = Object.fromEntries(new FormData(form).entries());
        const registro = { ...dados, quando: new Date().toISOString(), pagina: location.pathname };
        try {
          const chave = 'evolve_contatos';
          const lista = JSON.parse(localStorage.getItem(chave) || '[]');
          lista.push(registro);
          localStorage.setItem(chave, JSON.stringify(lista));
        } catch (_) {}
        console.info('[Evolve · contato registrado]', registro);

        const box = form.parentNode;
        const ok = document.createElement('div');
        ok.className = 'capta__ok';
        ok.style.marginTop = '1rem';
        ok.innerHTML = `<strong>Mensagem recebida, ${(dados.nome || '').split(' ')[0] || 'obrigado'}.</strong>
          <p>A equipe da Evolve vai analisar o cenário da ${dados.empresa || 'sua empresa'} e retornar o contato. Quem responde é uma pessoa, não um robô.</p>`;
        form.hidden = true;
        box.appendChild(ok);
      });
    }
  }

  /* ------------------------------------- 17. SUMÁRIO DA CARTA (seção corrente) */
  function initCartaToc() {
    const toc = $('.carta__toc');
    if (!toc) return;
    const links = $$('a[href^="#"]', toc);
    const targets = links.map((a) => $(a.getAttribute('href'))).filter(Boolean);
    if (!targets.length) return;

    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        links.forEach((a) => a.classList.toggle('is-current', a.getAttribute('href') === `#${entry.target.id}`));
      });
    }, { rootMargin: '-30% 0px -55% 0px' });
    targets.forEach((t) => io.observe(t));
  }

  /* --------------------------------------------- 18. TRILHA DA ROTINA (fill) */
  function initRotina() {
    const rail = $('.rotina__rail');
    if (!rail || REDUCED) return;
    frame.add(({ vh }) => {
      const r = rail.getBoundingClientRect();
      if (r.bottom < 0 || r.top > vh) return;
      const p = clamp((vh * 0.75 - r.top) / (r.height * 0.7 + vh * 0.25));
      rail.style.setProperty('--rotina-fill', `${(p * 100).toFixed(1)}%`);
    });
  }

  /* -------------------------------------------- 19. DICA DE ROLAGEM DO HERO */
  function initScrollCue() {
    const cue = $('.scroll-cue');
    if (!cue) return;
    frame.add(({ y }) => cue.classList.toggle('is-hidden', y > 80));
  }

  /* ------------------------------------------------------------------ boot */
  function boot() {
    initSmoothScroll();
    frame.start();
    initReveal();
    initPull();
    initFio();
    initCursor();
    initCounters();
    initTerritorios();
    initFaixa();
    initScrub();
    initCena();
    initOrdem();
    initMag();
    initHeader();
    initNav();
    initAccordions();
    initModal();
    initCartaToc();
    initRotina();
    initScrollCue();
    document.documentElement.classList.add('js-ready');
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();

/* ==========================================================================
   ABERTURA — mosaico que reage ao ponteiro + entrada da palavra EVOLVE
   O foco do zoom de cada retrato acompanha o ponteiro: a origem da
   transformação é a posição do cursor mapeada dentro daquele retrato.
   ========================================================================== */
(() => {
  'use strict';
  const abertura = document.querySelector('.abertura');
  if (!abertura) return;

  const REDUZIDO = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* entrada: letra por letra */
  requestAnimationFrame(() => abertura.classList.add('is-on'));

  if (REDUZIDO) return;

  const tiles = Array.from(abertura.querySelectorAll('.abertura__tile'));
  if (!tiles.length) return;
  if (matchMedia('(pointer: coarse)').matches) return;

  const alvo  = { x: 0.5, y: 0.5 };
  const atual = { x: 0.5, y: 0.5 };
  let ativo = false, rodando = false;

  abertura.addEventListener('pointermove', (e) => {
    const r = abertura.getBoundingClientRect();
    alvo.x = (e.clientX - r.left) / r.width;
    alvo.y = (e.clientY - r.top) / r.height;
    ativo = true;
    if (!rodando) { rodando = true; requestAnimationFrame(passo); }
  });

  abertura.addEventListener('pointerleave', () => {
    alvo.x = 0.5; alvo.y = 0.5; ativo = true;
    if (!rodando) { rodando = true; requestAnimationFrame(passo); }
  });

  function passo() {
    atual.x += (alvo.x - atual.x) * 0.12;
    atual.y += (alvo.y - atual.y) * 0.12;

    const cx = atual.x * innerWidth;
    const cy = atual.y * innerHeight;

    /* queda medida na diagonal da janela: previsível em qualquer tela */
    const diag = Math.hypot(innerWidth, innerHeight);

    tiles.forEach((tile) => {
      const r = tile.getBoundingClientRect();

      /* a origem do zoom é o ponto do retrato que está sob o ponteiro */
      const px = (cx - r.left) / r.width;
      const py = (cy - r.top) / r.height;
      const ox = Math.max(0, Math.min(1, px));
      const oy = Math.max(0, Math.min(1, py));

      /* proximidade real: distância do ponteiro ao centro deste retrato */
      const d = Math.hypot(cx - (r.left + r.width / 2), cy - (r.top + r.height / 2));
      const perto = Math.max(0, 1 - d / (diag * 0.42));
      const z = 1.12 + perto * 0.34;

      tile.style.setProperty('--ox', (ox * 100).toFixed(2) + '%');
      tile.style.setProperty('--oy', (oy * 100).toFixed(2) + '%');
      tile.style.setProperty('--z', z.toFixed(3));
      tile.style.opacity = (0.15 + perto * 0.17).toFixed(3);
    });

    const parado = Math.abs(alvo.x - atual.x) < 0.0008 && Math.abs(alvo.y - atual.y) < 0.0008;
    if (parado && !ativo) { rodando = false; return; }
    ativo = false;
    requestAnimationFrame(passo);
  }
})();

/* ==========================================================================
   SOM DA NOTIFICAÇÃO — dois toques curtos, como o alerta de mensagem.
   Só dispara depois de um gesto do visitante: navegador nenhum permite
   áudio automático, e forçar isso só geraria erro no console.
   ========================================================================== */
(() => {
  'use strict';
  const cena = document.querySelector('.cena');
  if (!cena || matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  let ctx = null, liberado = false, tocado = false;

  const liberar = () => {
    liberado = true;
    window.removeEventListener('pointerdown', liberar);
    window.removeEventListener('keydown', liberar);
    window.removeEventListener('wheel', liberar);
  };
  window.addEventListener('pointerdown', liberar, { once: true, passive: true });
  window.addEventListener('keydown', liberar, { once: true });
  window.addEventListener('wheel', liberar, { once: true, passive: true });

  function toque(t0, freq, volume) {
    const osc = ctx.createOscillator();
    const g = ctx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(freq, t0);
    g.gain.setValueAtTime(0, t0);
    g.gain.linearRampToValueAtTime(volume, t0 + 0.012);
    g.gain.exponentialRampToValueAtTime(0.0001, t0 + 0.17);
    osc.connect(g).connect(ctx.destination);
    osc.start(t0);
    osc.stop(t0 + 0.2);
  }

  function soar() {
    if (tocado || !liberado) return;
    try {
      ctx = ctx || new (window.AudioContext || window.webkitAudioContext)();
      if (ctx.state === 'suspended') ctx.resume();
      const t = ctx.currentTime + 0.02;
      toque(t,        1318, 0.085);   // E6
      toque(t + 0.13, 1760, 0.070);   // A6
      tocado = true;
    } catch (_) { /* áudio indisponível: a cena funciona sem ele */ }
  }

  /* dispara quando o segundo tempo da cena (a mensagem) entra */
  const ping = cena.querySelector('.cena__ping');
  if (!ping) return;
  const obs = new MutationObserver(() => {
    if (ping.classList.contains('is-live')) { soar(); obs.disconnect(); }
  });
  obs.observe(ping, { attributes: true, attributeFilter: ['class'] });
})();

/* ==========================================================================
   BARRA DE LEITURA DA CARTA
   Aparece quando a carta entra e acompanha o quanto já foi lido dela.
   ========================================================================== */
(() => {
  'use strict';
  const barra = document.querySelector('.leitura');
  const carta = document.querySelector('.carta');
  if (!barra || !carta) return;

  const fill = barra.querySelector('.leitura__fill');
  let topo = 0, alturaUtil = 1;

  function medir() {
    topo = carta.getBoundingClientRect().top + window.scrollY;
    /* 0% quando o topo da carta encosta no topo da janela;
       100% quando o fim da carta encosta no fim da janela. */
    alturaUtil = Math.max(1, carta.offsetHeight - innerHeight);
  }

  function quadro() {
    const y = window.scrollY;
    const p = Math.max(0, Math.min(1, (y - topo) / alturaUtil));
    const fim = topo + carta.offsetHeight;
    const naTela = y + innerHeight > topo && y < fim;
    barra.classList.toggle('is-on', naTela);
    fill.style.transform = `scaleX(${p.toFixed(4)})`;
  }

  medir();
  quadro();
  addEventListener('resize', () => { medir(); quadro(); }, { passive: true });

  /* scroll com um quadro de folga, para não recalcular mais de uma vez por frame */
  let agendado = false;
  addEventListener('scroll', () => {
    if (agendado) return;
    agendado = true;
    requestAnimationFrame(() => { agendado = false; quadro(); });
  }, { passive: true });
})();

/* ==========================================================================
   GRAFO DE SERVIÇOS
   Um núcleo e quatro ramificações. Cada ponto pode ser arrastado com o
   ponteiro e aberto com clique ou teclado.

   Entrada: os nós nascem colapsados no centro e explodem para fora quando
   a seção entra na tela. A própria física leva eles até o lugar — a mola de
   volta ao repouso é o que dispara o arremesso.

   Física: mola da ligação com o núcleo, repulsão entre as ramificações e
   mola fraca de volta à posição de repouso — o grafo reage ao arrasto sem
   nunca virar uma bagunça ilegível.
   ========================================================================== */
(() => {
  'use strict';
  const raiz = document.querySelector('[data-grafo]');
  if (!raiz) return;

  const svg = raiz.querySelector('.grafo__svg');
  const REDUZIDO = matchMedia('(prefers-reduced-motion: reduce)').matches;

  const centroEl = raiz.querySelector('[data-no="centro"]');
  const satEls   = Array.from(raiz.querySelectorAll('[data-no]:not([data-no="centro"])'));
  const linkEls  = Array.from(raiz.querySelectorAll('.grafo__link'));
  if (!centroEl || satEls.length === 0) return;

  const ler = (el) => ({
    el,
    x:  +el.dataset.x,  y:  +el.dataset.y,
    rx: +el.dataset.x,  ry: +el.dataset.y,   // repouso
    vx: 0, vy: 0,
    r:  +el.dataset.r,
    s: 1, vs: 0, sAlvo: 1                    // escala, para o estouro
  });

  const nucleo = ler(centroEl);
  const sats   = satEls.map(ler);
  const todos  = [nucleo, ...sats];

  /* ---------------- desenho ---------------- */
  function pinta() {
    todos.forEach((n) => {
      const e = n.s < 0.999 || n.s > 1.001 ? ` scale(${n.s.toFixed(4)})` : '';
      n.el.setAttribute('transform', `translate(${n.x.toFixed(2)} ${n.y.toFixed(2)})${e}`);
    });
    sats.forEach((n, i) => {
      const l = linkEls[i];
      if (!l) return;
      const dx = n.x - nucleo.x, dy = n.y - nucleo.y;
      const d = Math.hypot(dx, dy);
      /* enquanto o nó está praticamente sobre o centro, não há linha a traçar */
      if (d < nucleo.r + n.r * n.s + 2) { l.setAttribute('d', ''); return; }
      const ux = dx / d, uy = dy / d;
      const mx = (nucleo.x + n.x) / 2 + (-uy) * 26;
      const my = (nucleo.y + n.y) / 2 + ( ux) * 26;
      const ax = nucleo.x + ux * nucleo.r,       ay = nucleo.y + uy * nucleo.r;
      const bx = n.x - ux * (n.r * n.s),         by = n.y - uy * (n.r * n.s);
      l.setAttribute('d', `M ${ax.toFixed(1)} ${ay.toFixed(1)} Q ${mx.toFixed(1)} ${my.toFixed(1)} ${bx.toFixed(1)} ${by.toFixed(1)}`);
    });
  }

  /* ---------------- física ---------------- */
  const L_REPOUSO = 250;
  const K_LIGA    = 0.010;
  const K_VOLTA   = 0.014;
  const REPULSAO  = 46000;
  const ATRITO    = 0.86;

  let arrastando = null, rodando = false, explodiu = false;

  function passo() {
    sats.forEach((n) => {
      /* escala com mola: dá o estalo do estouro */
      n.vs += (n.sAlvo - n.s) * 0.20;
      n.vs *= 0.76;
      n.s  += n.vs;

      if (n === arrastando) return;

      const dx = n.x - nucleo.x, dy = n.y - nucleo.y;
      const d = Math.hypot(dx, dy) || 1;
      const f = (d - L_REPOUSO) * K_LIGA;
      n.vx -= (dx / d) * f;
      n.vy -= (dy / d) * f;

      sats.forEach((o) => {
        if (o === n) return;
        const ox = n.x - o.x, oy = n.y - o.y;
        const od = Math.max(40, Math.hypot(ox, oy));
        const fr = REPULSAO / (od * od);
        n.vx += (ox / od) * fr * 0.016;
        n.vy += (oy / od) * fr * 0.016;
      });

      n.vx += (n.rx - n.x) * K_VOLTA;
      n.vy += (n.ry - n.y) * K_VOLTA;

      n.vx *= ATRITO; n.vy *= ATRITO;
      n.x += n.vx;    n.y += n.vy;
    });

    if (nucleo !== arrastando) {
      nucleo.vs += (nucleo.sAlvo - nucleo.s) * 0.20;
      nucleo.vs *= 0.76;
      nucleo.s  += nucleo.vs;
      nucleo.vx += (nucleo.rx - nucleo.x) * 0.06;
      nucleo.vy += (nucleo.ry - nucleo.y) * 0.06;
      nucleo.vx *= 0.82; nucleo.vy *= 0.82;
      nucleo.x += nucleo.vx; nucleo.y += nucleo.vy;
    }

    pinta();

    const quieto = todos.every((n) =>
      Math.hypot(n.vx, n.vy) < 0.05 && Math.abs(n.vs) < 0.0015 && Math.abs(n.sAlvo - n.s) < 0.004);
    if (!arrastando && quieto) { rodando = false; return; }
    requestAnimationFrame(passo);
  }

  function acorda() { if (!rodando) { rodando = true; requestAnimationFrame(passo); } }

  /* ---------------- entrada: colapsa no centro ---------------- */
  function arma() {
    raiz.classList.add('is-armado');
    todos.forEach((n) => {
      n.x = nucleo.rx; n.y = nucleo.ry;
      n.vx = n.vy = 0;
      n.s = 0.01; n.vs = 0; n.sAlvo = 0.01;
    });
    pinta();
  }

  function explode() {
    if (explodiu) return;
    explodiu = true;
    raiz.classList.remove('is-armado');
    raiz.classList.add('is-explodindo');

    /* o núcleo abre primeiro */
    nucleo.sAlvo = 1;
    acorda();

    /* e as ramificações saem em sequência, cada uma na sua direção */
    sats.forEach((n, i) => {
      setTimeout(() => {
        const ang = Math.atan2(n.ry - nucleo.ry, n.rx - nucleo.rx);
        const impulso = 15;
        n.vx = Math.cos(ang) * impulso;
        n.vy = Math.sin(ang) * impulso;
        n.sAlvo = 1;
        acorda();
      }, 120 + i * 85);
    });

    setTimeout(() => raiz.classList.remove('is-explodindo'), 1600);
  }

  if (REDUZIDO) {
    pinta();
    raiz.classList.add('is-pronto');
  } else {
    arma();
    const obs = new IntersectionObserver((entradas) => {
      entradas.forEach((e) => {
        if (e.isIntersecting) { explode(); obs.disconnect(); }
      });
    }, { threshold: 0.25 });
    obs.observe(raiz);
    /* rede de segurança: se o observer não disparar, solta depois de 2,5s */
    setTimeout(explode, 2500);
  }

  /* ---------------- arraste ---------------- */
  const ponto = svg.createSVGPoint();
  function paraViewBox(ev) {
    ponto.x = ev.clientX; ponto.y = ev.clientY;
    const m = svg.getScreenCTM();
    return m ? ponto.matrixTransform(m.inverse()) : { x: 0, y: 0 };
  }

  todos.forEach((n) => {
    let idPonteiro = null, andou = 0, ox = 0, oy = 0;

    n.el.addEventListener('pointerdown', (e) => {
      if (REDUZIDO || !explodiu) return;
      if (e.button !== undefined && e.button !== 0) return;
      const p = paraViewBox(e);
      idPonteiro = e.pointerId;
      andou = 0;
      ox = n.x - p.x; oy = n.y - p.y;
      arrastando = n;
      n.vx = n.vy = 0;
      n.el.classList.add('is-dragging');
      n.el.setPointerCapture(idPonteiro);
      acorda();
    });

    n.el.addEventListener('pointermove', (e) => {
      if (idPonteiro !== e.pointerId || arrastando !== n) return;
      const p = paraViewBox(e);
      const nx = p.x + ox, ny = p.y + oy;
      andou += Math.hypot(nx - n.x, ny - n.y);
      n.x = nx; n.y = ny;
      pinta();
    });

    const solta = (e) => {
      if (idPonteiro !== e.pointerId) return;
      idPonteiro = null;
      arrastando = null;
      n.el.classList.remove('is-dragging');
      acorda();
      if (andou > 6) {
        n.el.dataset.arrastou = '1';
        setTimeout(() => { delete n.el.dataset.arrastou; }, 60);
      }
    };
    n.el.addEventListener('pointerup', solta);
    n.el.addEventListener('pointercancel', solta);

    n.el.addEventListener('click', (e) => {
      if (n.el.dataset.arrastou) { e.preventDefault(); e.stopPropagation(); }
    });
  });

  /* ---------------- realce da ligação ---------------- */
  sats.forEach((n, i) => {
    const l = linkEls[i];
    if (!l) return;
    const liga = () => l.classList.add('is-hot');
    const desliga = () => l.classList.remove('is-hot');
    n.el.addEventListener('pointerenter', liga);
    n.el.addEventListener('pointerleave', desliga);
    n.el.addEventListener('focus', liga);
    n.el.addEventListener('blur', desliga);
  });
})();

/* ==========================================================================
   MÁQUINA DE ESCREVER
   Divide o texto em caracteres preservando a marcação interna (<em>, <br>)
   e revela um a um, com um cursor que acompanha.

   Acessibilidade: o texto completo entra como aria-label do elemento e os
   caracteres ficam aria-hidden, então o leitor de tela anuncia a frase
   inteira de uma vez. Sem JavaScript, o texto aparece normal.
   ========================================================================== */
window.EvolveEscrever = (function () {
  'use strict';
  const REDUZIDO = matchMedia('(prefers-reduced-motion: reduce)').matches;

  function fatia(el) {
    /* troca cada caractere por um span, sem destruir <em>, <strong>, <br> */
    const chars = [];
    (function anda(no) {
      Array.from(no.childNodes).forEach((filho) => {
        if (filho.nodeType === 3) {
          const frag = document.createDocumentFragment();
          Array.from(filho.textContent).forEach((ch) => {
            const s = document.createElement('span');
            s.className = 'tw__c';
            s.textContent = ch;
            frag.appendChild(s);
            chars.push(s);
          });
          no.replaceChild(frag, filho);
        } else if (filho.nodeType === 1) {
          if (filho.tagName === 'BR') { chars.push(filho); return; }
          anda(filho);
        }
      });
    })(el);
    return chars;
  }

  function escrever(el, opcoes) {
    const o = Object.assign({ velocidade: 30, atraso: 0, aoTerminar: null }, opcoes || {});
    /* o <br> precisa virar espaço, senão o leitor de tela lê as duas
       linhas coladas ("serviçospartem") */
    const textoCheio = Array.from(el.childNodes)
      .map(function lerNo(n) {
        if (n.nodeType === 3) return n.textContent;
        if (n.nodeType === 1) return n.tagName === 'BR' ? ' ' : Array.from(n.childNodes).map(lerNo).join('');
        return '';
      })
      .join('')
      .replace(/\s+/g, ' ')
      .trim();

    if (REDUZIDO) {
      el.classList.add('tw', 'tw--pronto');
      if (o.aoTerminar) o.aoTerminar();
      return;
    }

    el.setAttribute('aria-label', textoCheio);
    const chars = fatia(el);
    chars.forEach((c) => { if (c.classList) c.setAttribute('aria-hidden', 'true'); });
    el.classList.add('tw');

    const cursor = document.createElement('span');
    cursor.className = 'tw__cursor';
    cursor.setAttribute('aria-hidden', 'true');

    let i = 0;
    const tique = () => {
      /* pula vários de uma vez quando o intervalo do navegador atrasa */
      let passos = 1;
      while (passos-- > 0 && i < chars.length) {
        const c = chars[i++];
        if (c.classList) c.classList.add('is-on');
        if (c.parentNode) c.parentNode.insertBefore(cursor, c.nextSibling);
      }
      if (i < chars.length) {
        const ch = chars[i - 1];
        const txt = ch && ch.textContent;
        /* respira nas pontuações, como quem digita de verdade */
        const pausa = /[.,;:—]/.test(txt || '') ? o.velocidade * 7 : o.velocidade;
        setTimeout(tique, pausa);
      } else {
        el.classList.add('tw--pronto');
        setTimeout(() => cursor.remove(), 620);
        if (o.aoTerminar) o.aoTerminar();
      }
    };
    setTimeout(tique, o.atraso);
  }

  return { escrever, reduzido: REDUZIDO };
})();

/* ==========================================================================
   ABERTURA DE NOSSOS SERVIÇOS
   Encadeia a entrada: marca de seção → título escrito → dica.
   A explosão do grafo é disparada pelo próprio módulo do grafo, pelo
   observer da seção, então as duas coisas correm juntas.
   ========================================================================== */
(() => {
  'use strict';
  const sec = document.querySelector('.grafo-secao');
  if (!sec || !window.EvolveEscrever) return;

  const eyebrow = sec.querySelector('.no-secao');
  const titulo  = sec.querySelector('[data-escrever]');
  const dica    = sec.querySelector('.grafo__dica');
  if (!titulo) return;

  const { escrever, reduzido } = window.EvolveEscrever;

  if (reduzido) {
    sec.classList.add('is-escrito');
    return;
  }

  /* esconde o que vai entrar, para não piscar antes da animação */
  sec.classList.add('is-aguardando');

  let comecou = false;
  function comeca() {
    if (comecou) return;
    comecou = true;
    sec.classList.remove('is-aguardando');
    if (eyebrow) eyebrow.classList.add('is-on');

    escrever(titulo, {
      velocidade: 26,
      atraso: 420,
      aoTerminar: () => { if (dica) dica.classList.add('is-on'); }
    });
  }

  const obs = new IntersectionObserver((entradas) => {
    entradas.forEach((e) => { if (e.isIntersecting) { comeca(); obs.disconnect(); } });
  }, { threshold: 0.2 });
  obs.observe(sec);
  setTimeout(comeca, 2500);   /* rede de segurança */
})();
