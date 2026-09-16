/* ==========================================================================
   EVOLVE — MOTOR DE DIAGNÓSTICO (QUIZ 0–5)
   --------------------------------------------------------------------------
   COMO A NOTA É CALCULADA
   Cada uma das 4 perguntas oferece 4 alternativas com pesos 0 · 1 · 3 · 5.
   A nota final é a MÉDIA ARITMÉTICA das 4 respostas, num intervalo de 0 a 5:

       nota = 5 - [(p1 + p2 + p3 + p4) / 4]

   Zero absoluto = situação grave (risco ativo, nada estruturado).
   Cinco        = situação muito boa (estrutura instalada e sustentada).

   Os pesos não são lineares de propósito (0-1-3-5 em vez de 0-1-2-3): a
   distância entre "não existe" e "existe no improviso" é pequena na prática,
   enquanto o salto para "existe formalizado" é grande. A escala reflete isso
   e evita que quatro respostas medianas produzam uma nota falsamente boa.

   FAIXAS DE LEITURA
       0,00 – 1,20  Risco ativo
       1,21 – 2,40  Dependência estrutural
       2,41 – 3,40  Organização iniciada
       3,41 – 4,40  Estrutura com lacunas
       4,41 – 5,00  Maturidade instalada

   O tom das devolutivas segue o Manual da Cultura Evolve: apresentar o que
   foi identificado sem rótulos, simplificações ou acusações, e sempre indicar
   o próximo movimento concreto.
   ========================================================================== */
(() => {
  'use strict';

  /* ======================================================================
     CONFIGURAÇÃO DE ENVIO  —  PREENCHER QUANDO O GOOGLE FORMS ESTIVER PRONTO
     ----------------------------------------------------------------------
     1. Crie o Google Forms com os campos abaixo (na mesma ordem).
     2. Em "Respostas", ative "Receber notificações por e-mail de novas
        respostas" para a Evolve ser avisada a cada preenchimento.
     3. Abra o formulário, clique com o botão direito > Inspecionar e copie o
        atributo name de cada campo (formato: entry.123456789).
     4. Cole os valores em FORM_CONFIG.entries e o ID do form em formId.
     Enquanto formId estiver vazio, o diagnóstico funciona normalmente e as
     respostas ficam registradas no console + localStorage para conferência.
     ====================================================================== */
  const FORM_CONFIG = {
    formId: '',                         // ex: '1FAIpQLSd...'  (sem /viewform)
    entries: {
      nome:        '',                  // ex: 'entry.111111111'
      empresa:     '',
      cargo:       '',
      email:       '',
      whatsapp:    '',
      colaboradores: '',
      segmento:    '',
      cidadeUf:    '',
      desafio:     '',
      servico:     '',                  // preenchido automaticamente
      nota:        '',                  // preenchido automaticamente
      faixa:       '',                  // preenchido automaticamente
      respostas:   ''                   // preenchido automaticamente
    }
  };

  const FAIXAS = [
    { max: 1.20, key: 'maturidade',   rotulo: 'Maturidade instalada' },
    { max: 2.40, key: 'lacunas',      rotulo: 'Estrutura com lacunas' },
    { max: 3.40, key: 'iniciada',     rotulo: 'Organização iniciada' },
    { max: 4.40, key: 'dependencia',  rotulo: 'Dependência estrutural' },
    { max: 5.01, key: 'risco',        rotulo: 'Risco ativo' }
  ];

  const faixaDe = (nota) => FAIXAS.find((f) => nota <= f.max) || FAIXAS[FAIXAS.length - 1];

  /* ======================================================================
     BANCO DE PERGUNTAS E DEVOLUTIVAS
     Todo o conteúdo abaixo deriva dos documentos oficiais da Evolve
     (Serviços Evolve, Posicionamento de Marca, Manual da Cultura e
     Briefing de Mapeamento). Nenhum dado, prazo, preço ou garantia foi
     inventado.
     ====================================================================== */
  const BANCO = {

    /* ---------------------------------------------------------------- */
    'pessoas-relacoes': {
      titulo: 'Pessoas e Relações de Trabalho',
      chamada: 'Quatro perguntas sobre como a sua empresa contrata e administra pessoas.',
      perguntas: [
        {
          texto: 'Quem executa hoje a folha de pagamento e as rotinas de pessoal?',
          opcoes: [
            { v: 0, t: 'O próprio dono ou sócio — porque não confia essa informação a mais ninguém.' },
            { v: 1, t: 'Alguém da equipe que aprendeu na prática, sem formação na área.' },
            { v: 3, t: 'Um contador externo, sem ninguém acompanhando internamente.' },
            { v: 5, t: 'Um responsável experiente, com rotinas definidas e conferência periódica.' }
          ]
        },
        {
          texto: 'Como estão documentadas admissões, jornadas, férias e desligamentos?',
          opcoes: [
            { v: 0, t: 'Não há padrão. Cada caso é resolvido no momento em que aparece.' },
            { v: 1, t: 'Existem arquivos, mas espalhados e sem um responsável claro.' },
            { v: 3, t: 'Existe um fluxo definido, mas ele falha quando o volume aumenta.' },
            { v: 5, t: 'Fluxo escrito, responsáveis definidos e conferência por checklist.' }
          ]
        },
        {
          texto: 'Nos últimos 24 meses, houve reclamações ou processos trabalhistas?',
          opcoes: [
            { v: 0, t: 'Mais de um — e não sabemos com precisão o que os originou.' },
            { v: 1, t: 'Um caso, e ele expôs falhas de registro que continuam abertas.' },
            { v: 3, t: 'Nenhum, mas sabemos que existem pontos frágeis não corrigidos.' },
            { v: 5, t: 'Nenhum, e já revisamos os processos preventivamente.' }
          ]
        },
        {
          texto: 'Quando alguém sai, o conhecimento da função sai junto com a pessoa?',
          opcoes: [
            { v: 0, t: 'Sim. Se essa pessoa sai, a rotina para.' },
            { v: 1, t: 'Em parte. Outra pessoa aprende no improviso, com retrabalho.' },
            { v: 3, t: 'Há registros, porém incompletos ou desatualizados.' },
            { v: 5, t: 'Não. O processo está descrito, é treinável e há substituto preparado.' }
          ]
        }
      ],
      devolutivas: {
        risco: {
          titulo: 'A rotina de pessoal está sustentada por confiança pessoal, não por processo.',
          leitura: 'O que as suas respostas mostram é uma operação de pessoas que funciona porque alguém específico segura — normalmente você. Isso concentra informação sigilosa, consome o seu tempo em tarefas que não decidem o futuro do negócio e deixa a empresa exposta a riscos que só aparecem depois, em forma de custo. Não é falta de cuidado: é ausência de estrutura para o cuidado se sustentar sem depender de uma pessoa.',
          passos: [
            'Levantamento dos fluxos, responsabilidades, documentos e riscos operacionais do Departamento Pessoal.',
            'Plano de correção priorizado, separando o que é urgência legal do que é organização de rotina.',
            'Organização das rotinas admissionais, de jornada, benefícios, férias, desligamentos e controles — com você saindo da execução.'
          ]
        },
        dependencia: {
          titulo: 'Existem rotinas, mas elas moram nas pessoas — não na empresa.',
          leitura: 'Há prática acumulada e boa vontade, e isso já resolve o dia a dia. O problema é que a prática não está descrita: quem faz, faz do jeito que aprendeu. Quando o volume cresce, quando alguém falta ou quando um caso sai do padrão, a rotina vira improviso e o improviso vira risco. É exatamente o ponto em que estruturar custa pouco e deixar como está começa a custar caro.',
          passos: [
            'Diagnóstico e organização do DP com quem já executa a rotina hoje — sem terceirizar o conhecimento para fora.',
            'Definição de fluxos, responsáveis e documentos, com checklist de conferência.',
            'Estruturação de cargos, salários e políticas de remuneração, para que as decisões deixem de ser caso a caso.'
          ]
        },
        iniciada: {
          titulo: 'A organização começou. O que falta é sustentação quando o volume aperta.',
          leitura: 'Suas respostas indicam uma base montada: existe fluxo, existe responsável, existe intenção de fazer certo. A fragilidade aparece nas bordas — no caso fora do padrão, no mês de pico, na pessoa que falta. É uma etapa boa de estar, e é também onde muitas empresas param, porque o problema deixou de doer todos os dias. Consolidar agora é mais barato do que reconstruir depois de um passivo.',
          passos: [
            'Revisão dos pontos de falha do fluxo atual e definição de contingência para os casos fora do padrão.',
            'Registro dos processos em material simples de usar e robusto o suficiente para orientar decisões.',
            'Rotina de conferência periódica com indicadores próprios da área de pessoal.'
          ]
        },
        lacunas: {
          titulo: 'A estrutura existe. As lacunas são específicas — e localizáveis.',
          leitura: 'Você já não está apagando incêndios nessa frente. O que resta são lacunas pontuais, do tipo que não interrompe a operação mas cobra em eficiência e em segurança jurídica. Nesse estágio o trabalho deixa de ser de reconstrução e passa a ser de precisão: identificar onde a estrutura ainda depende de memória e fechar esses pontos antes que o crescimento os transforme em gargalo.',
          passos: [
            'Auditoria de conformidade nas rotinas de pessoal, com evidências e responsáveis por cada correção.',
            'Plano de carreira, cargos e competências para dar previsibilidade às decisões sobre pessoas.',
            'Transferência de método para o time interno, com indicadores de acompanhamento.'
          ]
        },
        maturidade: {
          titulo: 'A base está instalada. O próximo ganho não está mais aqui.',
          leitura: 'Suas respostas descrevem uma operação de pessoas organizada, confiável e com segurança nas relações de trabalho. Isso é resultado de decisão, não de sorte. Nesse ponto, insistir nessa frente traz retorno decrescente: o gargalo do crescimento provavelmente está em outra camada — na maturidade das lideranças, na qualidade das contratações ou nas condições de trabalho que sustentam o desempenho.',
          passos: [
            'Manutenção da conformidade com reavaliações periódicas e indicadores já existentes.',
            'Diagnóstico organizacional mais amplo, para identificar onde está de fato o limite do crescimento.',
            'Avaliação das outras três frentes: liderança, seleção e riscos psicossociais.'
          ]
        }
      }
    },

    /* ---------------------------------------------------------------- */
    'recrutamento': {
      titulo: 'Recrutamento e Seleção',
      chamada: 'Quatro perguntas sobre como as pessoas certas chegam — ou não — até a sua empresa.',
      perguntas: [
        {
          texto: 'Como o perfil da vaga é definido antes de o processo começar?',
          opcoes: [
            { v: 0, t: 'Não definimos. Procuramos alguém parecido com quem saiu.' },
            { v: 1, t: 'Descrevemos apenas as exigências técnicas do cargo.' },
            { v: 3, t: 'Técnico e algumas competências, mas sem alinhar com quem decide.' },
            { v: 5, t: 'Perfil técnico e comportamental desenhado junto com a diretoria.' }
          ]
        },
        {
          texto: 'Das últimas cinco contratações, quantas continuam entregando o esperado?',
          opcoes: [
            { v: 0, t: 'Uma ou nenhuma.' },
            { v: 1, t: 'Duas.' },
            { v: 3, t: 'Três ou quatro.' },
            { v: 5, t: 'Todas as cinco.' }
          ]
        },
        {
          texto: 'Quanto do seu tempo um processo seletivo consome?',
          opcoes: [
            { v: 0, t: 'Muito. Eu faço a triagem, entrevisto e decido sozinho.' },
            { v: 1, t: 'Bastante. Entrevistamos muita gente desalinhada com a vaga.' },
            { v: 3, t: 'Razoável, mas sem parecer técnico para apoiar a decisão final.' },
            { v: 5, t: 'Pouco. Recebo finalistas avaliados e um parecer com evidências.' }
          ]
        },
        {
          texto: 'Como é a chegada de um novo colaborador nos primeiros 90 dias?',
          opcoes: [
            { v: 0, t: 'Ele começa e aprende olhando os outros trabalharem.' },
            { v: 1, t: 'Há uma apresentação inicial e nada além disso.' },
            { v: 3, t: 'Existe integração, mas sem acompanhamento nem metas do período.' },
            { v: 5, t: 'Plano de integração com responsável, metas e conversas de acompanhamento.' }
          ]
        }
      ],
      devolutivas: {
        risco: {
          titulo: 'A contratação está sendo decidida sem critério definido — e o custo aparece depois.',
          leitura: 'Suas respostas apontam um processo que começa sem perfil claro e termina sem parecer. Quando isso acontece, a decisão recai sobre impressão pessoal e urgência de preencher a vaga. O custo raramente é contabilizado como erro de contratação: ele aparece como rotatividade, retrabalho, clima ruim e tempo do dono gasto em algo que poderia ter sido resolvido antes da primeira entrevista.',
          passos: [
            'Definição do perfil da vaga com quem decide: requisitos técnicos e comportamentais indispensáveis.',
            'Estruturação do processo — divulgação, triagem, entrevistas e avaliação por evidências.',
            'Parecer técnico com apoio à decisão, para que a escolha final tenha base e não só intuição.'
          ]
        },
        dependencia: {
          titulo: 'O processo existe, mas ainda depende de você em todas as etapas.',
          leitura: 'Você está conduzindo o funil praticamente sozinho. Isso garante que ninguém entre sem o seu aval — e é justamente por isso que consome o tempo que deveria estar no negócio. O volume de candidatos desalinhados indica que o filtro está no lugar errado: no fim, com você, em vez de no início, no desenho do perfil.',
          passos: [
            'Curadoria e estruturação de vagas, movendo o filtro para o começo do processo.',
            'Triagem e entrevistas conduzidas com instrumentos e critérios definidos.',
            'Plano de integração para os primeiros 90 dias, com responsável e metas do período.'
          ]
        },
        iniciada: {
          titulo: 'Boa taxa de acerto. O que falta é previsibilidade e apoio à decisão.',
          leitura: 'A maioria das suas contratações permanece, o que indica leitura de pessoas afiada. O ponto frágil é a repetibilidade: sem perfil alinhado com a diretoria e sem parecer estruturado, o acerto depende de quem está conduzindo naquele momento. Quando você delegar a seleção, a taxa de acerto cai — não por falha da equipe, mas porque o critério não está fora da sua cabeça.',
          passos: [
            'Alinhamento formal do perfil ideal entre diretoria e quem conduz a seleção.',
            'Avaliação por evidências e parecer escrito, para tornar o critério transferível.',
            'Acompanhamento dos 90 dias com indicadores de aderência e permanência.'
          ]
        },
        lacunas: {
          titulo: 'A seleção está madura. A lacuna está na integração ou no parecer.',
          leitura: 'As pessoas certas estão chegando e permanecendo. As lacunas que aparecem nas suas respostas são de acabamento: um parecer que ainda não apoia formalmente a decisão, ou uma integração que não acompanha os primeiros 90 dias com a mesma qualidade da seleção. É um ajuste de precisão, com efeito direto na curva de aprendizado de cada novo colaborador.',
          passos: [
            'Padronização do parecer de seleção com evidências e recomendação.',
            'Onboarding acompanhado com metas de 30, 60 e 90 dias.',
            'Conexão do processo com plano de carreira e desenvolvimento, para retenção.'
          ]
        },
        maturidade: {
          titulo: 'Seleção estruturada. O gargalo do crescimento está em outro lugar.',
          leitura: 'Suas respostas descrevem um processo com perfil alinhado, avaliação por evidências, apoio à decisão e integração acompanhada. Contratar bem já não é o seu problema. Vale investigar se as pessoas certas que chegam estão encontrando lideranças preparadas para conduzi-las e condições de trabalho que sustentem o desempenho — é aí que boas contratações costumam se perder.',
          passos: [
            'Manutenção do processo com indicadores de aderência, permanência e desempenho.',
            'Avaliação da maturidade das lideranças que recebem esses profissionais.',
            'Leitura das condições de trabalho e dos fatores que afetam retenção.'
          ]
        }
      }
    },

    /* ---------------------------------------------------------------- */
    'riscos-saude': {
      titulo: 'Riscos Psicossociais e Saúde Organizacional',
      chamada: 'Quatro perguntas sobre os fatores do trabalho que afetam saúde e desempenho.',
      perguntas: [
        {
          texto: 'Sua empresa já avaliou fatores de risco psicossocial e integrou o resultado ao GRO/PGR?',
          opcoes: [
            { v: 0, t: 'Não sabemos como iniciar nem o que precisa ser documentado.' },
            { v: 1, t: 'Sabemos da exigência, mas nada foi feito até agora.' },
            { v: 3, t: 'Fizemos uma aplicação pontual, sem plano de ação nem responsáveis.' },
            { v: 5, t: 'Sim, com relatório, plano 5W2H e reavaliação prevista.' }
          ]
        },
        {
          texto: 'Existem queixas de sobrecarga, conflito, assédio, baixa autonomia ou insegurança?',
          opcoes: [
            { v: 0, t: 'Com frequência — e não há canal nem tratativa definida.' },
            { v: 1, t: 'Pontualmente, e resolvemos caso a caso quando chegam.' },
            { v: 3, t: 'Poucas. Existe canal, mas não analisamos os padrões que aparecem.' },
            { v: 5, t: 'Monitoramos, analisamos padrões e agimos sobre a causa organizacional.' }
          ]
        },
        {
          texto: 'O que os indicadores mostram — afastamentos, rotatividade, horas extras, incidentes?',
          opcoes: [
            { v: 0, t: 'Não acompanhamos esses indicadores.' },
            { v: 1, t: 'Acompanhamos alguns, sem cruzar com as condições de trabalho.' },
            { v: 3, t: 'Acompanhamos e vemos sinais de desgaste, sem explicação clara.' },
            { v: 5, t: 'Acompanhamos, cruzamos com fatores do trabalho e agimos de forma preventiva.' }
          ]
        },
        {
          texto: 'Como as ações de saúde são conduzidas hoje?',
          opcoes: [
            { v: 0, t: 'Não temos ações. Tratamos quando alguém adoece.' },
            { v: 1, t: 'Ações pontuais: campanhas e palestras isoladas.' },
            { v: 3, t: 'Ações recorrentes, mas que não mexem na organização do trabalho.' },
            { v: 5, t: 'Medidas organizacionais com responsáveis, prazos e acompanhamento.' }
          ]
        }
      ],
      devolutivas: {
        risco: {
          titulo: 'Há exigência normativa aberta e sinais do trabalho que ainda não foram lidos.',
          leitura: 'Suas respostas indicam duas frentes descobertas ao mesmo tempo: a avaliação dos fatores psicossociais não foi feita e as queixas do dia a dia não têm caminho definido. Isso não significa que sua empresa adoece as pessoas — significa que, hoje, você não tem como saber. Sem evidência, a decisão sobre o que priorizar fica no palpite, e a exigência da NR-1 continua em aberto.',
          passos: [
            'Plano metodológico da avaliação, com instrumentos adequados e comunicação aos participantes.',
            'Diagnóstico dos fatores psicossociais com entrevistas, observação e análise de indicadores organizacionais.',
            'Mapa de prioridades e plano 5W2H com responsáveis, prazos e integração ao GRO/PGR.'
          ]
        },
        dependencia: {
          titulo: 'O tema é reconhecido, mas a resposta ainda é reativa.',
          leitura: 'Você já enxerga o assunto e trata o que chega. O limite dessa abordagem é que ela age sobre episódios, não sobre os fatores que os produzem — então os mesmos casos voltam, com pessoas diferentes. É a diferença entre atender queixas e gerir condições de trabalho. A segunda exige evidência, e a evidência exige método.',
          passos: [
            'Diagnóstico com instrumentos adequados, evidências e limites de interpretação explícitos.',
            'Relatório consolidado com níveis de atenção e recomendações de prevenção.',
            'Integração ao GRO/PGR, articulada com SST e profissionais habilitados.'
          ]
        },
        iniciada: {
          titulo: 'A avaliação começou. O que falta é virar gestão, não relatório.',
          leitura: 'Sua empresa já aplicou algo e já acompanha parte dos indicadores. O ponto que suas respostas revelam é o mais comum nessa etapa: a avaliação existe, mas não se transformou em plano com responsáveis e prazos. Sem isso, o documento cumpre a formalidade e não muda a condição de trabalho — e a exigência normativa continua tecnicamente frágil numa fiscalização.',
          passos: [
            'Transformação do que já foi levantado em mapa de prioridades e plano 5W2H.',
            'Definição de responsáveis, prazos e indicadores para cada medida organizacional.',
            'Rituais de acompanhamento, registros e reavaliação periódica.'
          ]
        },
        lacunas: {
          titulo: 'Há processo. As lacunas estão na causa organizacional.',
          leitura: 'Você monitora, tem canal e conduz ações com recorrência. A lacuna que aparece é de profundidade: as ações acontecem ao lado do trabalho, sem mexer em como o trabalho está organizado — jornada, dimensionamento, autonomia, clareza de papéis. É aí que o ganho de saúde e o ganho de desempenho passam a ser o mesmo movimento.',
          passos: [
            'Análise dos fatores da organização do trabalho que sustentam os sinais observados.',
            'Revisão de processos, papéis e dimensionamento onde a evidência indicar.',
            'Programa contínuo com reavaliações, orientação de gestores e apoio à implantação.'
          ]
        },
        maturidade: {
          titulo: 'Gestão de riscos psicossociais instalada e rastreável.',
          leitura: 'Suas respostas descrevem exatamente o que a norma pede e o que a prática exige: avaliação com método, plano com responsáveis, indicadores cruzados com condições de trabalho e medidas organizacionais acompanhadas. Nesse estágio o valor está em sustentar o ciclo e em qualificar quem conduz — porque a maior parte dos fatores psicossociais é operada, no dia a dia, pela liderança imediata.',
          passos: [
            'Supervisão do ciclo interno de avaliação e gestão, para a equipe seguir com autonomia.',
            'Orientação e formação dos gestores nos fatores que eles controlam diretamente.',
            'Reavaliações programadas com comparação histórica dos indicadores.'
          ]
        }
      }
    },

    /* ---------------------------------------------------------------- */
    'lideranca': {
      titulo: 'Liderança e Desenvolvimento Humano Organizacional',
      chamada: 'Quatro perguntas sobre quem conduz as pessoas e as decisões na sua empresa.',
      perguntas: [
        {
          texto: 'Como seus líderes chegaram à posição que ocupam?',
          opcoes: [
            { v: 0, t: 'Por competência técnica ou tempo de casa, sem preparo para gerir pessoas.' },
            { v: 1, t: 'Por indicação, com orientação informal dada por mim.' },
            { v: 3, t: 'Com alguma formação, mas sem continuidade nem aplicação acompanhada.' },
            { v: 5, t: 'Por trilha de desenvolvimento com prática, PDI e acompanhamento.' }
          ]
        },
        {
          texto: 'Feedback, delegação, conflitos e cobrança acontecem de que forma?',
          opcoes: [
            { v: 0, t: 'Cada um faz do seu jeito — ou não faz, e o assunto chega até mim.' },
            { v: 1, t: 'Só quando o problema já explodiu.' },
            { v: 3, t: 'Existe orientação, mas sem ritmo definido nem registro.' },
            { v: 5, t: 'Ritos definidos, linguagem comum e registro dos acordos.' }
          ]
        },
        {
          texto: 'Se você se ausentar por quinze dias, o que acontece com as decisões do dia a dia?',
          opcoes: [
            { v: 0, t: 'Param, ou voltam para mim por telefone.' },
            { v: 1, t: 'Andam, com atraso e retrabalho.' },
            { v: 3, t: 'Andam, mas as decisões difíceis esperam o meu retorno.' },
            { v: 5, t: 'Andam com autonomia, dentro de alçadas definidas.' }
          ]
        },
        {
          texto: 'Como está o clima entre as equipes e a confiança nas lideranças?',
          opcoes: [
            { v: 0, t: 'Ruído constante, grupos fechados e desconfiança.' },
            { v: 1, t: 'Depende muito do setor e do líder de cada área.' },
            { v: 3, t: 'Estável, mas sem espaço seguro para trazer problemas.' },
            { v: 5, t: 'As pessoas dizem o que precisa ser dito e os líderes sustentam a conversa.' }
          ]
        }
      ],
      devolutivas: {
        risco: {
          titulo: 'Quem lidera não foi preparado para liderar — e o custo disso volta para você.',
          leitura: 'Suas respostas descrevem o padrão mais frequente nas PMEs: profissionais promovidos pela competência técnica, sem nunca terem recebido ferramentas para conduzir pessoas. O efeito é previsível. Sem feedback, delegação e mediação de conflito, tudo o que exige uma conversa difícil sobe um nível — e o nível acima é você. Não é falta de esforço da sua equipe. É falta de repertório, e repertório se constrói.',
          passos: [
            'Diagnóstico das necessidades de desenvolvimento e dos objetivos de aprendizagem reais da operação.',
            'Formação com prática e aplicação no trabalho — comunicação, feedback, delegação e conflitos.',
            'Encontros de acompanhamento para transformar conhecimento em comportamento observável.'
          ]
        },
        dependencia: {
          titulo: 'A liderança existe no organograma, mas a decisão ainda mora com você.',
          leitura: 'Suas lideranças conduzem o operacional, e isso já é terreno ganho. O que as respostas mostram é que a decisão difícil e a conversa desconfortável continuam retornando ao dono. Enquanto a alçada não estiver definida e o rito não existir, delegar vai parecer arriscado — e, honestamente, vai ser. Estrutura de decisão vem antes de confiança, não depois.',
          passos: [
            'Definição de alçadas, papéis e fóruns de decisão, para delegar sem perder controle.',
            'Ritos de gestão com cadência: feedback, acompanhamento e registro dos acordos.',
            'Mentoria de gestão para os líderes atuais, sobre desafios concretos e não sobre teoria.'
          ]
        },
        iniciada: {
          titulo: 'Há formação e há prática. O que falta é continuidade e linguagem comum.',
          leitura: 'Sua empresa já investiu em desenvolvimento, e dá para ver o efeito. A fragilidade está na continuidade: sem ritmo, registro e aplicação acompanhada, a formação vira evento e o comportamento volta ao padrão anterior em poucos meses. Quando cada líder resolve do seu jeito, a empresa passa a ter tantos modelos de gestão quantos líderes tiver.',
          passos: [
            'Arquitetura de trilha de desenvolvimento com aplicação no trabalho e evolução acompanhada.',
            'Linguagem comum de gestão: mesmos ritos, mesmos critérios, mesmos registros entre áreas.',
            'PDI por líder, com desafios de aplicação e encontros de acompanhamento.'
          ]
        },
        lacunas: {
          titulo: 'Liderança madura. A lacuna está na segurança para trazer problemas.',
          leitura: 'Suas respostas indicam líderes que conduzem, decidem e sustentam ritos. A lacuna que aparece é a mais silenciosa e a mais caras de todas: quando não há espaço seguro para trazer um problema, ele não desaparece — ele apenas chega mais tarde, maior e mais caro. Segurança psicológica não é conforto: é a condição para que o erro seja informado enquanto ainda é corrigível.',
          passos: [
            'Trabalho de segurança psicológica com as lideranças, ligado a indicadores e não a discurso.',
            'Workshops aplicados sobre conflito, respeito e conversas difíceis.',
            'Estrutura de desempenho e potencial, para decisões sobre o time deixarem de ser subjetivas.'
          ]
        },
        maturidade: {
          titulo: 'Lideranças preparadas e empresa que decide sem você no meio.',
          leitura: 'Suas respostas descrevem o cenário que a maior parte dos empresários está tentando construir: alçadas claras, ritos que funcionam, conversas que acontecem e decisões que andam na sua ausência. Nesse ponto o desenvolvimento deixa de ser correção e passa a ser escala — formar a próxima camada de líderes com a mesma linguagem, em volume, sem depender da presença de uma pessoa específica.',
          passos: [
            'Trilha escalável de formação de líderes, para preparar a próxima camada com linguagem comum.',
            'Plano de sucessão e gestão de talentos com critérios definidos.',
            'Estrutura de cargos, competências e desenvolvimento ligada à cultura e aos resultados.'
          ]
        }
      }
    }
  };

  /* ======================================================================
     MOTOR
     ====================================================================== */
  function init(root) {
    const slug = root.dataset.diag;
    const set = BANCO[slug];
    if (!set) { console.warn('[Evolve] Conjunto de diagnóstico não encontrado:', slug); return; }

    const stage    = root.querySelector('.diag__stage');
    const track    = root.querySelector('.diag__track');
    const result   = root.querySelector('.diag__result');
    const medidor  = root.querySelector('.medidor');
    const medFill  = root.querySelector('.medidor__fill');
    const medKnob  = root.querySelector('.medidor__knob');
    const medVal   = root.querySelector('.medidor__score .val');
    const medStage = root.querySelector('.medidor__stage');
    const scaleRows= Array.from(root.querySelectorAll('.medidor__scale-row'));
    if (!stage) return;

    const respostas = new Array(set.perguntas.length).fill(null);
    let atual = 0;

    /* ---------- monta a trilha de progresso ---------- */
    if (track) {
      track.innerHTML = set.perguntas.map(() => '<span></span>').join('');
    }

    /* ---------- monta as perguntas ---------- */
    const LETRAS = ['A', 'B', 'C', 'D'];
    stage.innerHTML = set.perguntas.map((q, qi) => `
      <div class="diag__q${qi === 0 ? ' is-live' : ''}" data-q="${qi}">
        <span class="diag__q-index">Pergunta ${qi + 1} de ${set.perguntas.length}</span>
        <h3 class="diag__q-text">${q.texto}</h3>
        <div class="diag__opts" role="group" aria-label="Alternativas da pergunta ${qi + 1}">
          ${q.opcoes.map((o, oi) => `
            <button type="button" class="diag__opt" data-v="${o.v}" data-oi="${oi}" data-verb="responder">
              <span class="diag__opt-key" aria-hidden="true">${LETRAS[oi]}</span>
              <span>${o.t}</span>
            </button>`).join('')}
        </div>
        <button type="button" class="diag__back"${qi === 0 ? ' hidden' : ''} data-back>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
          Voltar
        </button>
      </div>`).join('');

    const painels = Array.from(stage.querySelectorAll('.diag__q'));

    /* ---------- medidor ---------- */
    const railLen = medFill && medFill.getTotalLength ? medFill.getTotalLength() : 0;
    if (medFill && railLen) {
      medFill.style.strokeDasharray = railLen;
      medFill.style.strokeDashoffset = railLen;
    }

    function pintaMedidor(nota, parcial) {
      const p = Math.max(0, Math.min(1, nota / 5));
      if (medFill && railLen) medFill.style.strokeDashoffset = (railLen * (1 - p)).toFixed(2);
      if (medKnob && medFill && medFill.getPointAtLength) {
        const pt = medFill.getPointAtLength(railLen * p);
        medKnob.setAttribute('cx', pt.x);
        medKnob.setAttribute('cy', pt.y);
      }
      if (medVal) medVal.textContent = nota.toFixed(1).replace('.', ',');
      const f = faixaDe(nota);
      if (medStage) medStage.textContent = parcial ? `Parcial · ${f.rotulo}` : f.rotulo;
      scaleRows.forEach((row) => row.classList.toggle('is-current', !parcial && row.dataset.faixa === f.key));
      /* nota é risco: baixa esfria em verde, alta esquenta até vermelho vinho */
      if (medFill) {
        medFill.style.stroke =
          nota <= 1.20 ? '#698784' :   /* maturidade  — verde azulado */
          nota <= 2.40 ? '#8A7F53' :   /* lacunas     — oliva         */
          nota <= 3.40 ? '#B85D36' :   /* iniciada    — terracota     */
          nota <= 4.40 ? '#9B3520' :   /* dependência — terracota fechado */
                         '#722033';    /* risco ativo — VERMELHO VINHO */
      }
      if (medidor) medidor.dataset.faixa = f.key;
    }

    function notaAtual() {
      const dadas = respostas.filter((r) => r !== null);
      if (!dadas.length) return 0;
      /* escala invertida: peso alto = estrutura boa, e a nota exibida é o
         RISCO. Logo 0 = tudo em ordem, 5 = risco ativo. */
      return 5 - (dadas.reduce((a, b) => a + b, 0) / dadas.length);
    }

    function mostra(i) {
      painels.forEach((p, pi) => {
        p.classList.toggle('is-live', pi === i);
        p.classList.toggle('is-past', pi < i);
      });
      atual = i;
    }

    /* ---------- interação ---------- */
    stage.addEventListener('click', (e) => {
      const back = e.target.closest('[data-back]');
      if (back) {
        if (atual > 0) {
          respostas[atual] = null;
          respostas[atual - 1] = null;
          if (track) track.children[atual - 1]?.classList.remove('is-done');
          if (track) track.children[atual]?.classList.remove('is-done');
          mostra(atual - 1);
          pintaMedidor(notaAtual(), true);
          stage.querySelectorAll('.diag__opt.is-picked').forEach((b, idx) => {
            if (Number(b.closest('.diag__q').dataset.q) >= atual) b.classList.remove('is-picked');
          });
        }
        return;
      }

      const opt = e.target.closest('.diag__opt');
      if (!opt) return;
      const painel = opt.closest('.diag__q');
      const qi = Number(painel.dataset.q);

      painel.querySelectorAll('.diag__opt').forEach((b) => b.classList.remove('is-picked'));
      opt.classList.add('is-picked');
      respostas[qi] = Number(opt.dataset.v);
      if (track && track.children[qi]) track.children[qi].classList.add('is-done');

      const completo = respostas.every((r) => r !== null);
      pintaMedidor(notaAtual(), !completo);

      setTimeout(() => {
        if (qi < set.perguntas.length - 1) mostra(qi + 1);
        else finaliza();
      }, 340);
    });

    /* ---------- resultado ---------- */
    function finaliza() {
      const nota = notaAtual();
      const f = faixaDe(nota);
      const d = set.devolutivas[f.key];
      result.dataset.faixa = f.key;
      pintaMedidor(nota, false);

      painels.forEach((p) => { p.classList.remove('is-live'); p.classList.add('is-past'); });
      stage.style.display = 'none';

      result.querySelector('[data-result-badge]').textContent = `${f.rotulo} · nota ${nota.toFixed(1).replace('.', ',')} de 5`;
      result.querySelector('[data-result-title]').textContent = d.titulo;
      result.querySelector('[data-result-read]').textContent = d.leitura;
      result.querySelector('[data-result-steps]').innerHTML = d.passos.map((s) => `<li>${s}</li>`).join('');

      const hidden = result.querySelector('[data-payload]');
      const payload = {
        servico: set.titulo,
        nota: nota.toFixed(2),
        faixa: f.rotulo,
        respostas: respostas.map((v, i) => `Q${i + 1}=${v}`).join(' | ')
      };
      if (hidden) hidden.value = JSON.stringify(payload);
      result.dataset.payload = JSON.stringify(payload);

      result.hidden = false;
      requestAnimationFrame(() => result.classList.add('is-live'));
      if (window.lenis) window.lenis.scrollTo(result, { offset: -120, duration: 0.9 });
      else result.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    /* ---------- refazer ---------- */
    const restart = root.querySelector('[data-restart]');
    if (restart) restart.addEventListener('click', () => {
      respostas.fill(null);
      if (track) Array.from(track.children).forEach((s) => s.classList.remove('is-done'));
      stage.querySelectorAll('.diag__opt.is-picked').forEach((b) => b.classList.remove('is-picked'));
      stage.style.display = '';
      result.hidden = true;
      result.classList.remove('is-live');
      const ok = root.querySelector('.capta__ok');
      if (ok) ok.remove();
      const form = root.querySelector('.capta');
      if (form) form.hidden = false;
      mostra(0);
      pintaMedidor(0, true);
    });

    /* ---------- captação de dados ---------- */
    const form = root.querySelector('.capta');
    if (form) {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        const dados = Object.fromEntries(new FormData(form).entries());
        let payload = {};
        try { payload = JSON.parse(result.dataset.payload || '{}'); } catch (_) {}
        const registro = { ...dados, ...payload, quando: new Date().toISOString(), pagina: location.pathname };

        /* 1. registro local para conferência enquanto o Forms não estiver ligado */
        try {
          const chave = 'evolve_diagnosticos';
          const lista = JSON.parse(localStorage.getItem(chave) || '[]');
          lista.push(registro);
          localStorage.setItem(chave, JSON.stringify(lista));
        } catch (_) {}
        console.info('[Evolve · diagnóstico registrado]', registro);

        /* 2. envio para o Google Forms, quando configurado */
        if (FORM_CONFIG.formId && FORM_CONFIG.entries.nome) {
          const params = new URLSearchParams();
          Object.entries(FORM_CONFIG.entries).forEach(([campo, entry]) => {
            if (!entry) return;
            const valor = registro[campo];
            if (valor !== undefined && valor !== '') params.append(entry, valor);
          });
          /* envio silencioso: o Forms notifica a Evolve por e-mail */
          fetch(`https://docs.google.com/forms/d/e/${FORM_CONFIG.formId}/formResponse?${params.toString()}`,
                { method: 'POST', mode: 'no-cors' }).catch(() => {});
        }

        /* 3. confirmação */
        const ok = document.createElement('div');
        ok.className = 'capta__ok';
        ok.innerHTML = `
          <strong>Recebemos o seu diagnóstico, ${(registro.nome || '').split(' ')[0] || 'obrigado'}.</strong>
          <p>A equipe da Evolve vai analisar as suas respostas e retornar com uma leitura do cenário da ${registro.empresa || 'sua empresa'} e o próximo movimento recomendado. O retorno é feito por uma pessoa, não por um robô.</p>`;
        form.hidden = true;
        form.parentNode.insertBefore(ok, form);
        if (window.lenis) window.lenis.scrollTo(ok, { offset: -140, duration: 0.8 });
      });
    }

    pintaMedidor(0, true);
  }

  function boot() {
    document.querySelectorAll('[data-diag]').forEach(init);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
