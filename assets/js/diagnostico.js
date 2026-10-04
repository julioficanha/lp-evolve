/* ==========================================================================
   EVOLVE — DIAGNÓSTICO RÁPIDO DE RH DA SUA EMPRESA (teste por blocos)
   --------------------------------------------------------------------------
   Quatro blocos, um por página de serviço:
     dp  · Departamento Pessoal e conformidade trabalhista (10 perguntas)
     sst · Segurança e Saúde no Trabalho                    (9 perguntas)
     rh  · Estrutura de RH e Gestão de Pessoas             (15 perguntas)
     lid · Liderança e gestão                               (7 perguntas)

   RESPOSTAS   Sim = 2 · Parcialmente = 1 · Não = 0 · Não se aplica = fora
               da conta (sai do numerador e do denominador).
   PESOS       Cada pergunta tem peso 1 (maturidade), 2 (estrutural) ou
               3 (crítica: passivo, multa, risco à saúde ou risco legal).

   Bloco%      = Σ(peso × resposta) / Σ(peso × 2) × 100, só sobre as
                 perguntas respondidas e aplicáveis.
   Índice Geral= 0,30·DP + 0,30·SST + 0,20·Gestão de Pessoas + 0,20·Liderança
                 (só com os 4 blocos feitos; bloco 100% "Não se aplica" sai e
                 os pesos são redistribuídos proporcionalmente).
   Faixas      76–100 RH Estruturado · 51–75 RH em Desenvolvimento ·
               26–50 RH com Pontos de Atenção · 0–25 Necessidade de Estruturação.
   Alerta ⚠️   bloco abaixo de 40% OU qualquer pergunta de peso 3 respondida
               "Não" (mesmo com a média alta).
   Validade    o bloco só é calculado com pelo menos 70% das perguntas respondidas.

   Fluxo: dados da empresa (uma vez, reaproveitados) → perguntas → resultado
   parcial público → cadastro de e-mail e contato (lead) → resultado completo.
   Todas as constantes ficam em CONFIG; o conteúdo, em BLOCOS.
   ========================================================================== */
(function () {
  'use strict';

  /* ======================================================================
     CONFIGURAÇÃO — ajuste aqui, sem mexer na lógica
     ====================================================================== */
  const CONFIG = {
    /* URL do Web App do Google Apps Script (termina em /exec). Ver a nota
       "Tutorial - Planilha Google de leads (Evolve)". Vazio = os leads ficam
       guardados no navegador (localStorage) e o console avisa. */
    LEAD_ENDPOINT: '',

    VALORES: { sim: 2, parcial: 1, nao: 0, na: null },
    OPCOES: [
      { v: 'sim',     t: 'Sim' },
      { v: 'parcial', t: 'Parcialmente' },
      { v: 'nao',     t: 'Não' },
      { v: 'na',      t: 'Não se aplica' }
    ],

    PESO_BLOCO: { dp: 0.30, sst: 0.30, rh: 0.20, lid: 0.20 },
    ALERTA_ABAIXO_DE: 40,      // % do bloco
    PESO_CRITICO: 3,           // pergunta de peso 3 com "Não" gera alerta
    VALIDADE_MINIMA: 0.70,     // fração mínima de perguntas respondidas

    FAIXAS: [
      { min: 76, chave: 'estruturado', emoji: '🟢', rotulo: 'RH Estruturado',
        texto: 'Sua empresa demonstra possuir processos de RH bem estruturados. Ainda assim, alguns pontos podem ser aprimorados para aumentar a eficiência, segurança e qualidade da gestão.',
        complemento: 'Sua empresa demonstra possuir boas práticas de RH e gestão. O próximo passo é identificar oportunidades de melhoria, eficiência e desenvolvimento.' },
      { min: 51, chave: 'desenvolvimento', emoji: '🟡', rotulo: 'RH em Desenvolvimento',
        texto: 'Sua empresa já possui algumas práticas importantes, porém existem processos que precisam ser estruturados ou padronizados.',
        complemento: 'Sua empresa já possui processos importantes, porém existem pontos que podem ser estruturados e padronizados para aumentar a segurança e a eficiência da gestão.' },
      { min: 26, chave: 'atencao', emoji: '🟠', rotulo: 'RH com Pontos de Atenção',
        texto: 'Foram identificadas lacunas relevantes que podem impactar a gestão das pessoas, a produtividade e a segurança dos processos internos.',
        complemento: 'Existem lacunas importantes nos processos de RH e gestão que podem gerar retrabalho, dificuldades na gestão de pessoas e riscos para a empresa.' },
      { min: 0, chave: 'estruturacao', emoji: '🔴', rotulo: 'RH com Necessidade de Estruturação',
        texto: 'Sua empresa apresenta oportunidades importantes para estruturar processos básicos de RH, Departamento Pessoal, SST e Gestão de Pessoas.',
        complemento: 'Sua empresa possui oportunidades relevantes de estruturação. A implantação de processos básicos pode proporcionar maior segurança, organização e qualidade na gestão das pessoas.' }
    ],

    STORAGE: {
      empresa:    'evolve_teste_empresa',
      contato:    'evolve_teste_contato',
      resultados: 'evolve_teste_resultados',
      pendentes:  'evolve_leads_pendentes'
    }
  };

  /* ======================================================================
     CONTEÚDO — perguntas literais do documento; [texto, peso]
     ====================================================================== */
  const BLOCOS = {
    dp: {
      n: 1, nome: 'Departamento Pessoal e conformidade trabalhista', curto: 'Departamento Pessoal', servico: 'Blindagem de RH',
      pagina: 'servicos-operacional-dp.html',
      perguntas: [
        ['Todos os colaboradores possuem registro e documentação de admissão organizados e atualizados?', 3],
        ['A empresa possui contratos de trabalho adequados às funções e modalidades de contratação? Funcionários e terceiros.', 3],
        ['A jornada de trabalho e o controle de ponto são realizados corretamente, conforme previsão legal? É realizado análise e gestão das informações?', 3],
        ['A folha de pagamento é conferida antes do fechamento?', 2],
        ['Férias e períodos aquisitivos são acompanhados para evitar vencimentos e multas?', 2],
        ['A empresa mantém cargos, salários e funções dos colaboradores devidamente definidos e atualizados?', 1],
        ['As alterações de cargo, salário, horário e função são formalizadas?', 2],
        ['Os processos de admissão, férias, afastamentos e desligamentos possuem procedimentos definidos?', 2],
        ['A empresa possui documentos, políticas e controles para reduzir riscos de passivos trabalhistas?', 3],
        ['Existe acompanhamento periódico das práticas de Departamento Pessoal para verificar sua conformidade com a legislação?', 1]
      ]
    },
    sst: {
      n: 2, nome: 'Segurança e Saúde no Trabalho', curto: 'Segurança do Trabalho', servico: 'Riscos Psicossociais',
      pagina: 'servicos-riscos-saude.html',
      aviso: 'Estas perguntas indicam a necessidade de uma avaliação especializada. O teste não substitui a análise legal e técnica de Segurança e Saúde no Trabalho.',
      perguntas: [
        ['A empresa possui PGR – Programa de Gerenciamento de Riscos atualizado, quando aplicável, contemplando a NR1 – riscos psicossociais?', 3],
        ['Possui PCMSO – Programa de Controle Médico de Saúde Ocupacional atualizado, quando aplicável?', 3],
        ['Os exames ocupacionais (admissional, periódico, retorno, mudança de risco e demissional) são realizados e controlados conforme a necessidade?', 3],
        ['Os colaboradores recebem EPIs adequados às atividades, quando necessários?', 2],
        ['A entrega e orientação sobre utilização dos EPIs são registradas e assinadas?', 2],
        ['Os treinamentos obrigatórios de Segurança do Trabalho (NRs) aplicáveis às atividades são realizados e controlados?', 3],
        ['A empresa acompanha os vencimentos de treinamentos, exames e documentos de SST?', 2],
        ['As informações de SST exigidas pelo e-Social são acompanhadas e enviadas adequadamente?', 2],
        ['Acidentes e incidentes de trabalho possuem procedimento de registro, comunicação e análise?', 2]
      ]
    },
    rh: {
      n: 3, nome: 'Estrutura de RH e Gestão de Pessoas', curto: 'Gestão de Pessoas', servico: 'Recrutamento e Seleção',
      pagina: 'servicos-recrutamento-selecao.html',
      perguntas: [
        ['A empresa possui organograma atualizado?', 1],
        ['Cada cargo possui uma descrição clara de atividades, responsabilidades e requisitos?', 2],
        ['Existe um processo estruturado para abertura e aprovação de novas vagas?', 1],
        ['O recrutamento e seleção segue critérios definidos?', 2],
        ['A empresa realiza integração de novos colaboradores?', 2],
        ['Existe acompanhamento do colaborador durante o período de experiência?', 2],
        ['Os gestores realizam feedbacks periódicos?', 2],
        ['Existe avaliação de desempenho?', 1],
        ['A empresa possui indicadores de RH, como turnover, absenteísmo, tempo de contratação e treinamentos?', 2],
        ['A empresa possui um planejamento anual de treinamentos?', 1],
        ['Existem critérios claros para promoções, aumentos salariais e movimentações internas?', 2],
        ['A empresa realiza entrevistas de desligamento e analisa os motivos de geração de rotatividade?', 2],
        ['A empresa realiza ações para acompanhar clima organizacional e satisfação dos colaboradores?', 1],
        ['Existem políticas internas formalizadas e comunicadas aos colaboradores?', 2],
        ['A empresa possui código de conduta ou regras internas claramente estabelecidas?', 1]
      ]
    },
    lid: {
      n: 4, nome: 'Liderança e gestão', curto: 'Liderança e Gestão', servico: 'Cursos, Palestras e Treinamentos',
      pagina: 'servicos-lideranca-desenvolvimento.html',
      perguntas: [
        ['Os líderes conhecem claramente suas responsabilidades na gestão das equipes?', 3],
        ['Os gestores recebem treinamento para liderar pessoas?', 2],
        ['Os colaboradores sabem claramente o que é esperado deles?', 2],
        ['Os gestores realizam reuniões periódicas com suas equipes?', 1],
        ['A empresa possui procedimentos para tratamento de conflitos internos?', 2],
        ['Existem canais adequados para que colaboradores relatem problemas, sugestões ou situações inadequadas?', 3],
        ['A direção acompanha indicadores relacionados às pessoas e utiliza essas informações para tomar decisões?', 2]
      ]
    }
  };
  const ORDEM_BLOCOS = ['dp', 'sst', 'rh', 'lid'];

  /* ======================================================================
     CÁLCULO (funções puras)
     ====================================================================== */
  /* o ⚠️ não aparece quando a faixa é "Estruturado" (seria incongruente) */
  const mostraAlerta = (r) => !!(r && r.alerta && r.pct !== null && r.pct < CONFIG.FAIXAS[0].min);

  function faixaDe(pct) {
    return CONFIG.FAIXAS.find((f) => pct >= f.min) || CONFIG.FAIXAS[CONFIG.FAIXAS.length - 1];
  }

  /* respostas: array com 'sim' | 'parcial' | 'nao' | 'na' | null (não respondida) */
  function calculaBloco(chave, respostas) {
    const perguntas = BLOCOS[chave].perguntas;
    let num = 0, den = 0, respondidas = 0;
    const criticas = [], naoRespostas = [];
    perguntas.forEach(([, peso], i) => {
      const r = respostas[i];
      if (r === null || r === undefined) return;
      respondidas++;
      if (r === 'na') return;
      num += peso * CONFIG.VALORES[r];
      den += peso * 2;
      if (r === 'nao') (peso >= CONFIG.PESO_CRITICO ? criticas : naoRespostas).push(i);
    });
    const valido = respondidas / perguntas.length >= CONFIG.VALIDADE_MINIMA;
    const todosNA = valido && den === 0;
    const pct = valido && den > 0 ? Math.round((num / den) * 100) : null;
    const alerta = pct !== null && (pct < CONFIG.ALERTA_ABAIXO_DE || criticas.length > 0);
    return { chave, pct, valido, todosNA, respondidas, total: perguntas.length, criticas, naoRespostas, alerta,
             faixa: pct === null ? null : faixaDe(pct) };
  }

  /* resultados: { dp: {pct, todosNA}, ... } — exige os quatro blocos feitos */
  function indiceGeral(resultados) {
    if (!ORDEM_BLOCOS.every((k) => resultados[k] && (resultados[k].pct !== null || resultados[k].todosNA))) return null;
    let soma = 0, pesos = 0;
    ORDEM_BLOCOS.forEach((k) => {
      if (resultados[k].pct === null) return;           // 100% "Não se aplica": peso redistribuído
      soma += CONFIG.PESO_BLOCO[k] * resultados[k].pct;
      pesos += CONFIG.PESO_BLOCO[k];
    });
    return pesos ? Math.round(soma / pesos) : null;
  }

  const API = { CONFIG, BLOCOS, faixaDe, calculaBloco, indiceGeral };
  if (typeof module !== 'undefined' && module.exports) module.exports = API;
  if (typeof document === 'undefined') return;

  /* ======================================================================
     ARMAZENAMENTO (tolerante a navegador sem localStorage)
     ====================================================================== */
  const ler = (k, padrao) => { try { return JSON.parse(localStorage.getItem(k)) || padrao; } catch (_) { return padrao; } };
  const grava = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch (_) {} };
  const esc = (t) => String(t == null ? '' : t).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

  /* ======================================================================
     ENVIO DO LEAD — Google Apps Script (text/plain evita o preflight de CORS)
     ====================================================================== */
  function enviaLead(payload) {
    if (!CONFIG.LEAD_ENDPOINT) {
      const fila = ler(CONFIG.STORAGE.pendentes, []);
      fila.push(payload);
      grava(CONFIG.STORAGE.pendentes, fila);
      console.warn('[Evolve] LEAD_ENDPOINT vazio: lead guardado em localStorage ("' + CONFIG.STORAGE.pendentes + '").', payload);
      return Promise.resolve();
    }
    return fetch(CONFIG.LEAD_ENDPOINT, {
      method: 'POST', mode: 'no-cors',
      headers: { 'Content-Type': 'text/plain;charset=utf-8' },
      body: JSON.stringify(payload)
    }).catch((err) => {
      const fila = ler(CONFIG.STORAGE.pendentes, []);
      fila.push(payload);
      grava(CONFIG.STORAGE.pendentes, fila);
      console.warn('[Evolve] Falha ao enviar o lead; guardado em localStorage.', err);
    });
  }

  function montaPayload(chave, r, empresa, contato) {
    const b = BLOCOS[chave];
    const respostas = {};
    (r.respostas || []).forEach((v, i) => {
      if (v === null || v === undefined) return;
      respostas[`b${b.n}q${i + 1}`] = v === 'na' ? 'na' : CONFIG.VALORES[v];
    });
    const alertas = r.criticas.map((i) => `b${b.n}q${i + 1}`);
    if (r.pct !== null && r.pct < CONFIG.ALERTA_ABAIXO_DE) alertas.push(`bloco abaixo de ${CONFIG.ALERTA_ABAIXO_DE}%`);
    const ig = indiceGeral(ler(CONFIG.STORAGE.resultados, {}));
    return {
      data: new Date().toISOString(),
      bloco: b.nome,
      pagina: location.pathname.split('/').pop() || 'index.html',
      empresa: empresa.empresa || '',
      responsavel: empresa.responsavel || '',
      cidade_uf: empresa.cidade_uf || '',
      segmento: empresa.segmento || '',
      colaboradores: empresa.colaboradores || '',
      rh_interno: empresa.rh_interno || '',
      contato_email: contato.contato_email || '',
      contato_telefone: contato.contato_telefone || '',
      dificuldade: empresa.dificuldade || '',
      pontuacao_bloco: r.pct === null ? '' : r.pct,
      faixa: r.faixa ? r.faixa.rotulo : 'Não se aplica',
      indice_geral: ig === null ? '' : ig,
      alertas_criticos: alertas.join(', '),
      respostas: JSON.stringify(respostas),
      origem: location.href
    };
  }

  /* ======================================================================
     INTERFACE (estrutura funcional; o visual fino é do design system)
     ====================================================================== */
  function init(raiz) {
    const secao = raiz.closest('[data-bloco]');
    const chave = secao && secao.dataset.bloco;
    const bloco = BLOCOS[chave];
    if (!bloco) { console.warn('[Evolve] Bloco de teste não encontrado:', chave); return; }
    const uid = (secao.dataset.diag || chave) + '-' + Math.random().toString(36).slice(2, 7);
    const assunto = raiz.dataset.assunto || 'geral';

    let respostas = new Array(bloco.perguntas.length).fill(null);
    let atual = 0;
    let resultado = null;
    let enviando = false;

    const rola = () => {
      if (window.lenis) window.lenis.scrollTo(secao, { offset: -90, duration: 0.8 });
      else secao.scrollIntoView({ behavior: 'smooth', block: 'start' });
    };
    let interagiu = false;   // o foco só acompanha a tela depois que a pessoa começa a usar o teste
    raiz.addEventListener('click', () => { interagiu = true; }, true);
    raiz.addEventListener('submit', () => { interagiu = true; }, true);
    const REDUZIDO = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
    const espera = (ms) => new Promise((ok) => setTimeout(ok, REDUZIDO ? 0 : ms));
    let ultimaRespondida = -1;   // traço da barra de progresso que acabou de ser preenchido

    /* número crescendo e anel sendo preenchido */
    function animaPlacar() {
      raiz.querySelectorAll('.teste__anel[data-alvo]').forEach((anel) => {
        const alvo = Number(anel.dataset.alvo);
        const num = anel.querySelector('.teste__pct');
        if (REDUZIDO) { anel.style.setProperty('--nota', alvo); num.textContent = alvo + '%'; return; }
        const t0 = performance.now(), dur = 1500;
        const passo = (t) => {
          const p = Math.min(1, (t - t0) / dur);
          const e = 1 - Math.pow(1 - p, 3);          // desacelera no final
          anel.style.setProperty('--nota', (alvo * e).toFixed(2));
          num.textContent = Math.round(alvo * e) + '%';
          if (p < 1) requestAnimationFrame(passo);
          else anel.classList.add('is-cheio');
        };
        requestAnimationFrame(passo);
      });
    }

    /* botão mostra que está carregando antes de trocar de tela */
    function carregaBotao(btn) {
      btn.classList.add('is-carregando');
      btn.disabled = true;
      return espera(450);
    }

    const tela = (html) => {
      raiz.innerHTML = html;
      secao.classList.toggle('teste--amplo', !!raiz.querySelector('.diag__result'));
      animaPlacar();
      if (!interagiu) return;
      const heading = raiz.querySelector('h3, .diag__result-badge, .teste__passo');
      if (heading) { heading.tabIndex = -1; heading.focus({preventScroll: true}); }
    };

    /* ---------- 1. início / dados da empresa ---------- */
    function telaInicio() {
      const empresa = ler(CONFIG.STORAGE.empresa, null);
      const feito = ler(CONFIG.STORAGE.resultados, {})[chave];
      const cabeca = `
        <div class="teste__intro">
          <span class="diag__result-badge">Diagnóstico Rápido de RH da sua Empresa</span>
          <p class="diag__result-read">Descubra em poucos minutos como estão os principais processos de RH, Departamento Pessoal, Segurança do Trabalho e Gestão de Pessoas da sua empresa.</p>
          <p class="teste__regra">Responda cada pergunta com Sim, Parcialmente, Não ou Não se aplica.</p>
          ${bloco.aviso ? `<p class="teste__aviso">${bloco.aviso}</p>` : ''}
        </div>`;

      if (empresa) {
        tela(`${cabeca}
          ${feito ? `<div class="capta__ok teste__feito"><strong>Você já fez este teste: ${feito.pct === null ? 'não se aplica' : feito.pct + '%'}${feito.faixa ? ' · ' + feito.faixa.emoji + ' ' + feito.faixa.rotulo : ''}</strong>
            <p><button type="button" class="btn btn-link-light" data-ver-resultado><span>Ver o resultado</span></button></p></div>` : ''}
          <p class="teste__empresa">Empresa: <strong>${esc(empresa.empresa)}</strong> · ${esc(empresa.responsavel)}
            <button type="button" class="btn btn-link-light" data-trocar-dados><span>alterar dados</span></button></p>
          <div class="diag__result-actions"><button type="button" class="btn btn-terracota btn-lg" data-comecar><span>${feito ? 'Refazer o teste' : 'Começar o teste'}</span></button></div>`);
        raiz.querySelector('[data-comecar]').addEventListener('click', () => { respostas.fill(null); mostraPergunta(0); rola(); });
        raiz.querySelector('[data-trocar-dados]').addEventListener('click', () => telaDados(empresa));
        const ver = raiz.querySelector('[data-ver-resultado]');
        if (ver) ver.addEventListener('click', () => { resultado = feito; respostas = feito.respostas || respostas; ler(CONFIG.STORAGE.contato, null) ? telaCompleto() : telaParcial(); });
        return;
      }
      telaDados(null, cabeca);
    }

    function telaDados(dados, cabeca) {
      const d = dados || {};
      const sel = (v, atual) => (v === atual ? ' selected' : '');
      tela(`${cabeca || ''}
        <form class="capta teste__dados" novalidate>
          <p class="teste__passo">Antes de começar, conte quem é a sua empresa. Pedimos estes dados uma única vez.</p>
          <div class="capta__row">
            <div class="capta__field"><label for="t-empresa-${uid}">Nome da empresa</label>
              <input id="t-empresa-${uid}" name="empresa" required autocomplete="organization" value="${esc(d.empresa)}" placeholder="Razão social ou nome fantasia"></div>
            <div class="capta__field"><label for="t-resp-${uid}">Nome do responsável</label>
              <input id="t-resp-${uid}" name="responsavel" required autocomplete="name" value="${esc(d.responsavel)}" placeholder="Nome e sobrenome"></div>
          </div>
          <div class="capta__row">
            <div class="capta__field"><label for="t-cidade-${uid}">Cidade / UF</label>
              <input id="t-cidade-${uid}" name="cidade_uf" value="${esc(d.cidade_uf)}" placeholder="Ex.: Pato Branco / PR"></div>
            <div class="capta__field"><label for="t-seg-${uid}">Segmento</label>
              <input id="t-seg-${uid}" name="segmento" value="${esc(d.segmento)}" placeholder="Ex.: indústria metalúrgica"></div>
          </div>
          <div class="capta__row">
            <div class="capta__field"><label for="t-colab-${uid}">Quantidade de colaboradores</label>
              <select id="t-colab-${uid}" name="colaboradores">
                ${['Até 5', 'De 6 a 20', 'De 21 a 50', 'De 51 a 100', 'De 101 a 200', 'Mais de 200'].map((o) => `<option${sel(o, d.colaboradores)}>${o}</option>`).join('')}
              </select></div>
            <div class="capta__field"><label for="t-rhint-${uid}">A empresa tem RH interno?</label>
              <select id="t-rhint-${uid}" name="rh_interno">
                <option${sel('Sim', d.rh_interno)}>Sim</option><option${sel('Não', d.rh_interno)}>Não</option>
              </select></div>
          </div>
          <div class="capta__field"><label for="t-dif-${uid}">Qual é a principal dificuldade atual com pessoas/RH?</label>
            <textarea id="t-dif-${uid}" name="dificuldade" rows="2" placeholder="Escreva com as suas palavras.">${esc(d.dificuldade)}</textarea></div>
          <p class="teste__erro" hidden>Preencha o nome da empresa e o nome do responsável.</p>
          <div><button type="submit" class="btn btn-terracota btn-lg" data-verb="responder"><span>Começar o teste</span></button></div>
        </form>`);
      const form = raiz.querySelector('form');
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        const v = Object.fromEntries(new FormData(form).entries());
        if (!v.empresa.trim() || !v.responsavel.trim()) { form.querySelector('.teste__erro').hidden = false; return; }
        grava(CONFIG.STORAGE.empresa, v);
        respostas.fill(null);
        mostraPergunta(0);
        rola();
      });
    }

    /* ---------- 2. perguntas ---------- */
    function mostraPergunta(i, direcao = 'dir') {
      atual = i;
      const total = bloco.perguntas.length;
      const [texto] = bloco.perguntas[i];
      tela(`
        <div class="diag__track" role="progressbar" aria-label="Perguntas respondidas" aria-valuemin="0" aria-valuemax="${total}" aria-valuenow="${respostas.filter(x => x !== null).length}">${bloco.perguntas.map((_, k) => `<span class="${respostas[k] !== null ? 'is-done' : ''}${k === ultimaRespondida ? ' is-novo' : ''}"></span>`).join('')}</div>
        <div class="diag__stage">
          <div class="diag__q is-live entra-${direcao}">
            <span class="diag__q-index">${esc(bloco.nome)} · Pergunta ${i + 1} de ${total}</span>
            <h3 class="diag__q-text">${esc(texto)}</h3>
            <div class="diag__opts" role="group" aria-label="Respostas da pergunta ${i + 1}">
              ${CONFIG.OPCOES.map((o, k) => `
                <button type="button" class="diag__opt${respostas[i] === o.v ? ' is-picked' : ''}" data-v="${o.v}" data-verb="responder">
                  <span class="diag__opt-key" aria-hidden="true">${'ABCD'[k]}</span><span>${o.t}</span>
                </button>`).join('')}
            </div>
            <div class="teste__nav">
              <button type="button" class="diag__back"${i === 0 ? ' hidden' : ''} data-back>
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
                Voltar
              </button>
              <button type="button" class="diag__back" data-pular>Pular pergunta</button>
            </div>
          </div>
        </div>`);
      let avancando = false;
      raiz.querySelectorAll('.diag__opt').forEach((b) => b.addEventListener('click', () => {
        if (avancando) return;
        avancando = true;
        raiz.querySelectorAll('button').forEach(btn => { btn.disabled = true; });
        respostas[i] = b.dataset.v;
        ultimaRespondida = i;
        b.classList.add('is-picked');
        setTimeout(() => raiz.querySelector('.diag__q').classList.add('sai'), REDUZIDO ? 0 : 220);
        setTimeout(avanca, REDUZIDO ? 0 : 520);
      }));
      raiz.querySelector('[data-back]').addEventListener('click', () => { ultimaRespondida = -1; mostraPergunta(Math.max(0, i - 1), 'esq'); });
      raiz.querySelector('[data-pular]').addEventListener('click', () => { ultimaRespondida = -1; avanca(); });
    }

    function avanca() {
      if (atual < bloco.perguntas.length - 1) return mostraPergunta(atual + 1);
      finaliza();
    }

    /* ---------- 3. cálculo e resultado parcial ---------- */
    function finaliza() {
      const r = calculaBloco(chave, respostas);
      if (!r.valido) {
        const falta = respostas.findIndex((x) => x === null);
        const minimo = Math.ceil(bloco.perguntas.length * CONFIG.VALIDADE_MINIMA);
        tela(`<div class="capta__ok"><strong>Faltam respostas para calcular o resultado.</strong>
          <p>Você respondeu ${r.respondidas} de ${r.total} perguntas. Para um resultado confiável, responda pelo menos ${minimo} (use "Não se aplica" quando for o caso).</p></div>
          <div class="diag__result-actions"><button type="button" class="btn btn-terracota btn-lg" data-completar><span>Completar as respostas</span></button></div>`);
        raiz.querySelector('[data-completar]').addEventListener('click', () => mostraPergunta(falta < 0 ? 0 : falta));
        return;
      }
      resultado = Object.assign({}, r, { respostas: respostas.slice(), data: new Date().toISOString() });
      const todos = ler(CONFIG.STORAGE.resultados, {});
      todos[chave] = resultado;
      grava(CONFIG.STORAGE.resultados, todos);
      tela(`<div class="teste__calculando" role="status">
          <span class="teste__spinner" aria-hidden="true"></span>
          <p>Calculando o resultado da sua empresa…</p>
        </div>`);
      rola();
      espera(1300).then(telaParcial);
    }

    function numeroBloco(r) {
      if (r.pct === null) return '<span class="teste__pct">—</span><span class="teste__faixa">Não se aplica à sua empresa</span>';
      const cor = r.pct >= 76 ? '#9bbdb0' : r.pct >= 51 ? '#e0ca83' : r.pct >= 26 ? '#e3aa8b' : '#eea3a3';
      return `<span class="teste__anel" data-alvo="${r.pct}" style="--nota:0;--nota-cor:${cor}"><span class="teste__pct">0%</span></span><span class="teste__faixa">${r.faixa.emoji} ${r.faixa.rotulo}${mostraAlerta(r) ? ' · ⚠️' : ''}</span>`;
    }

    function telaParcial() {
      const r = resultado;
      const frase = r.faixa ? r.faixa.texto.split('. ')[0].replace(/\.$/, '') + '.' : 'As perguntas deste tema não se aplicam à sua empresa.';
      tela(`
        <div class="diag__result is-live teste__parcial">
          <span class="diag__result-badge">Sua pontuação · ${esc(bloco.nome)}</span>
          <div class="teste__placar">${numeroBloco(r)}</div>
          <p class="diag__result-read">${esc(frase)}</p>
          <div class="diag__result-actions">
            <button type="button" class="btn btn-terracota btn-lg" data-completo data-verb="abrir"><span>Acesse seu resultado completo</span></button>
            <button type="button" class="btn btn-outline-light" data-refazer data-verb="refazer"><span>Refazer o teste</span></button>
          </div>
        </div>`);
      raiz.querySelector('[data-completo]').addEventListener('click', (e) => {
        const contato = ler(CONFIG.STORAGE.contato, null);
        carregaBotao(e.currentTarget).then(() => {
          if (contato) { registraLead(contato); telaCompleto(); rola(); }
          else telaCaptura();
        });
      });
      raiz.querySelector('[data-refazer]').addEventListener('click', () => { respostas.fill(null); mostraPergunta(0); rola(); });
    }

    /* ---------- 4. captura do lead ---------- */
    function telaCaptura() {
      tela(`
        <div class="diag__result is-live">
          <span class="diag__result-badge">Resultado completo</span>
          <h3 class="diag__result-title">Acesse a leitura completa da sua empresa.</h3>
          <p class="diag__result-read">Cadastre seu e-mail e um contato. Você vê agora a leitura por tema, os pontos críticos e os próximos passos — e a equipe da Evolve pode falar com você sobre o seu caso.</p>
          <form class="capta" novalidate>
            <div class="capta__row">
              <div class="capta__field"><label for="t-email-${uid}">E-mail</label>
                <input id="t-email-${uid}" name="contato_email" type="email" required autocomplete="email" placeholder="nome@suaempresa.com.br"></div>
              <div class="capta__field"><label for="t-tel-${uid}">Telefone / WhatsApp</label>
                <input id="t-tel-${uid}" name="contato_telefone" type="tel" required autocomplete="tel" placeholder="(00) 00000-0000"></div>
            </div>
            <div class="teste__hp" aria-hidden="true"><label for="t-site-${uid}">Site</label><input id="t-site-${uid}" name="website" tabindex="-1" autocomplete="off"></div>
            <label class="capta__consent">
              <input type="checkbox" name="consentimento" required>
              <span>Autorizo a Evolve a entrar em contato sobre este teste e concordo com o uso dos meus dados exclusivamente para essa finalidade.</span>
            </label>
            <p class="teste__erro" hidden>Informe um e-mail válido, um telefone e marque a autorização.</p>
            <div><button type="submit" class="btn btn-terracota btn-lg" data-verb="enviar"><span>Ver meu resultado completo</span></button></div>
          </form>
        </div>`);
      const form = raiz.querySelector('form');
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        if (enviando) return;
        const v = Object.fromEntries(new FormData(form).entries());
        const okEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.contato_email || '');
        if (!okEmail || !(v.contato_telefone || '').trim() || !v.consentimento) { form.querySelector('.teste__erro').hidden = false; return; }
        const contato = { contato_email: v.contato_email.trim(), contato_telefone: v.contato_telefone.trim() };
        if (v.website) { telaCompleto(); return; }   // honeypot preenchido: robô, não envia
        enviando = true;
        const botao = form.querySelector('button[type="submit"]');
        grava(CONFIG.STORAGE.contato, contato);
        Promise.all([registraLead(contato), carregaBotao(botao)]).then(() => { enviando = false; telaCompleto(); rola(); });
      });
    }

    function registraLead(contato) {
      if (resultado.enviado) return Promise.resolve();
      resultado.enviado = true;
      const todos = ler(CONFIG.STORAGE.resultados, {});
      if (todos[chave]) { todos[chave].enviado = true; grava(CONFIG.STORAGE.resultados, todos); }
      return enviaLead(montaPayload(chave, resultado, ler(CONFIG.STORAGE.empresa, {}), contato));
    }

    /* ---------- 5. resultado completo ---------- */
    function telaCompleto() {
      const r = resultado;
      const todos = ler(CONFIG.STORAGE.resultados, {});
      const ig = indiceGeral(todos);
      const linhas = ORDEM_BLOCOS.map((k) => {
        const x = todos[k];
        const b = BLOCOS[k];
        const valor = x
          ? (x.pct === null ? 'Não se aplica' : `${x.pct}%${mostraAlerta(x) ? ' ⚠️' : ''}`)
          : `<a class="teste__link" href="${b.pagina}#diagnostico">Fazer o teste →</a>`;
        return `<li class="teste__linha${k === chave ? ' is-atual' : ''}"><span>${b.curto}<em class="teste__servico"> · ${b.servico}</em></span><strong>${valor}</strong></li>`;
      }).join('');
      const geral = ig === null
        ? `<li class="teste__linha teste__linha--geral"><span>Índice Geral de Estruturação</span><strong>Faça os outros testes e veja seu índice geral</strong></li>`
        : `<li class="teste__linha teste__linha--geral"><span>Índice Geral de Estruturação</span><strong>${ig}% · ${faixaDe(ig).emoji} ${faixaDe(ig).rotulo}</strong></li>`;
      const lista = (idx) => idx.map((i) => `<li>${esc(bloco.perguntas[i][0])}</li>`).join('');

      tela(`
        <div class="diag__result is-live teste__completo">
          <span class="diag__result-badge">Resultado completo · ${esc(bloco.nome)}</span>
          <div class="teste__placar">${numeroBloco(r)}</div>
          ${r.faixa ? `<p class="diag__result-read">${esc(r.faixa.texto)}</p>
          <div class="diag__result-next"><h4>O que isso significa</h4><p class="diag__result-read">${esc(r.faixa.complemento)}</p></div>` : ''}
          ${r.criticas.length ? `<div class="diag__result-next teste__criticas"><h4>${mostraAlerta(r) ? '⚠️ ' : ''}Lacunas críticas</h4><ol>${lista(r.criticas)}</ol></div>` : ''}
          ${r.naoRespostas.length ? `<div class="diag__result-next"><h4>Pontos de atenção</h4><ol>${lista(r.naoRespostas)}</ol></div>` : ''}
          <div class="diag__result-next"><h4>Visão por tema</h4><ul class="teste__temas">${linhas}${geral}</ul></div>
          <div class="diag__result-actions">
            <button type="button" class="btn btn-terracota btn-lg open-contact-trigger" data-subject="${esc(assunto)}" data-verb="conversar"><span>Falar com a Evolve sobre o resultado</span></button>
            <button type="button" class="btn btn-outline-light" data-refazer data-verb="refazer"><span>Refazer o teste</span></button>
          </div>
          <p class="diag__disclaimer">${bloco.aviso ? esc(bloco.aviso) + ' ' : ''}Este teste é uma leitura inicial baseada nas suas respostas. Não substitui avaliação clínica, jurídica, médica ou de engenharia de segurança.</p>
        </div>`);
      raiz.querySelector('[data-refazer]').addEventListener('click', () => { respostas.fill(null); mostraPergunta(0); rola(); });
    }

    const view = raiz.closest('.app-view');
    if (view) view.addEventListener('evolve:view-open', telaInicio);
    telaInicio();
  }

  function boot() { document.querySelectorAll('[data-teste-app]').forEach(init); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
