/* ==========================================================================
   EVOLVE — RECEPTOR DE LEADS DO SITE (Google Apps Script)
   --------------------------------------------------------------------------
   Projeto avulso em script.google.com ("Leads Site Evolve - receptor"),
   publicado como App da Web (Executar como: Eu · Acesso: Qualquer pessoa).
   A URL /exec vai em LEAD_ENDPOINT, no topo de assets/js/app.js.

   Trocar de planilha: mude PLANILHA_ID e publique em Implantar → Gerenciar
   implantações → editar → Nova versão. A URL /exec continua a mesma. A conta
   dona deste script precisa ser editora da planilha nova.

   O site manda um JSON com "tipo":
     contato     → aba "Contato"     (modal "Conversar com a Evolve")
     diagnostico → aba "Diagnóstico" (teste das páginas de serviço)
   Cada aba lista [chave do JSON, cabeçalho]; a ordem é a das colunas. Se a aba
   sumir, é recriada com o cabeçalho.
   ========================================================================== */
const PLANILHA_ID = '1UgY7J6mFr5wIBQotPCeLq6uXcMBfeFaCAd3OlO7G7A4';

const ABAS = {
  diagnostico: {
    nome: 'Diagnóstico',
    colunas: [
      ['data', 'Data/hora'], ['bloco', 'Bloco do teste'], ['pagina', 'Página'],
      ['empresa', 'Empresa'], ['responsavel', 'Responsável'], ['cidade_uf', 'Cidade/UF'],
      ['segmento', 'Segmento'], ['colaboradores', 'Colaboradores'], ['rh_interno', 'RH interno'],
      ['contato_email', 'E-mail'], ['contato_telefone', 'Telefone'],
      ['dificuldade', 'Principal dificuldade'], ['pontuacao_bloco', 'Pontuação do bloco (%)'],
      ['faixa', 'Faixa'], ['indice_geral', 'Índice geral'], ['alertas_criticos', 'Alertas críticos'],
      ['respostas', 'Respostas'], ['origem', 'Origem (URL)']
    ]
  },
  contato: {
    nome: 'Contato',
    colunas: [
      ['data', 'Data/hora'], ['nome', 'Nome'], ['empresa', 'Empresa'], ['email', 'E-mail'],
      ['telefone', 'Telefone/WhatsApp'], ['frente', 'Frente de interesse'],
      ['desafio', 'Principal desafio'], ['pagina', 'Página'], ['origem', 'Origem (URL)']
    ]
  }
};

/* Defesas: o endpoint é público (o visitante não tem login), então qualquer
   um pode postar. Descarta corpo grande, tipo desconhecido e lead sem os
   campos mínimos; corta cada campo; limita o volume por minuto. */
const LIMITE = { corpo: 20000, campo: 2000, porMinuto: 30 };
const OBRIGATORIOS = {
  contato: (d) => d.nome && (d.email || d.telefone),
  diagnostico: (d) => d.empresa && (d.contato_email || d.contato_telefone)
};

function doPost(e) {
  const corpo = (e && e.postData && e.postData.contents) || '';
  if (corpo.length > LIMITE.corpo) return resposta('descartado');
  let dados;
  try { dados = JSON.parse(corpo); } catch (_) { return resposta('descartado'); }
  const cfg = dados && ABAS[dados.tipo];
  if (!cfg || !OBRIGATORIOS[dados.tipo](dados)) return resposta('descartado');

  const lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    const cache = CacheService.getScriptCache();
    const minuto = 'n' + Math.floor(Date.now() / 60000);
    const n = Number(cache.get(minuto) || 0);
    if (n >= LIMITE.porMinuto) return resposta('limite');
    cache.put(minuto, String(n + 1), 120);

    const planilha = SpreadsheetApp.openById(PLANILHA_ID);
    let aba = planilha.getSheetByName(cfg.nome);
    if (!aba) {
      aba = planilha.insertSheet(cfg.nome);
      aba.appendRow(cfg.colunas.map((c) => c[1]));
      aba.setFrozenRows(1);
    }
    dados.data = new Date(); // hora do servidor, no fuso da planilha
    aba.appendRow(cfg.colunas.map(([chave]) => {
      let v = dados[chave] == null ? '' : dados[chave];
      if (typeof v !== 'string' && typeof v !== 'number' && !(v instanceof Date)) v = String(v);
      if (typeof v === 'string') {
        v = v.slice(0, LIMITE.campo);
        // o apóstrofo impede o Sheets de ler telefone/texto como fórmula
        if (/^[=+\-@\t\r]/.test(v)) v = "'" + v;
      }
      return v;
    }));
    return resposta('ok');
  } finally {
    lock.releaseLock();
  }
}

function resposta(t) {
  return ContentService.createTextOutput(t);
}

function doGet() {
  return ContentService.createTextOutput('Endpoint de leads da Evolve ativo.');
}
