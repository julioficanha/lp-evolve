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

function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    const dados = JSON.parse(e.postData.contents);
    const cfg = ABAS[dados.tipo] || ABAS.diagnostico;
    const planilha = SpreadsheetApp.openById(PLANILHA_ID);
    let aba = planilha.getSheetByName(cfg.nome);
    if (!aba) {
      aba = planilha.insertSheet(cfg.nome);
      aba.appendRow(cfg.colunas.map((c) => c[1]));
      aba.setFrozenRows(1);
    }
    dados.data = new Date(); // hora do servidor, no fuso da planilha
    aba.appendRow(cfg.colunas.map(([chave]) => {
      const v = dados[chave] == null ? '' : dados[chave];
      // o apóstrofo impede o Sheets de ler telefone/texto como fórmula
      return typeof v === 'string' && /^[=+\-@]/.test(v) ? "'" + v : v;
    }));
    return ContentService.createTextOutput('ok');
  } finally {
    lock.releaseLock();
  }
}

function doGet() {
  return ContentService.createTextOutput('Endpoint de leads da Evolve ativo.');
}
