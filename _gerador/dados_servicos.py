# -*- coding: utf-8 -*-
"""Conteúdo das quatro frentes. Fonte: Serviços Evolve, Posicionamento de Marca,
Manual da Cultura e Briefing de Mapeamento. Nada aqui foi inventado."""

FASES_PADRAO = {
    "fase1": ["Escuta do dono, da liderança e de quem executa",
              "Investigação das causas antes de recomendar",
              "Prioridades de intervenção com evidências"],
    "fase2": ["O que fazer, por quê, quem faz, quando e como",
              "Escopo, hipóteses e limites explícitos",
              "Critérios de conclusão combinados antes de começar"],
    "fase3": ["Solução desenhada com quem conhece a operação",
              "Capacitação, aplicação no trabalho e ajuste",
              "Acompanhamento próximo, com registro dos acordos"],
    "fase4": ["Responsáveis, indicadores e próximos ciclos definidos",
              "Materiais simples de usar e robustos para orientar",
              "A empresa segue sem depender da nossa presença"],
}

SERVICOS = [

    # ------------------------------------------------------------------ 01
    dict(
        arquivo="servicos-pessoas-relacionamento.html",
        slug="pessoas-relacoes",
        nome_curto="Pessoas e Relações de Trabalho",
        titulo="Pessoas e Relações de Trabalho — Evolve Capital Humano",
        descricao=("Contratar e administrar pessoas com segurança e organização: recrutamento, rotinas de "
                   "Departamento Pessoal, carreiras e remuneração para PMEs."),
        indice="Frente 01 de 04",
        h1a="Pessoas e Relações",
        h1b="de Trabalho.",
        pergunta=("A pergunta que esta frente responde: <strong>como contratar e administrar pessoas "
                  "com segurança e organização?</strong> Ajudamos a empresa a trazer as pessoas certas e "
                  "a sustentar relações de trabalho organizadas, claras e seguras."),
        variante="a",
        proporcao="1.757",
        legenda="Distribuidora cliente · a rotina de pessoal que sustenta o atendimento",
        imagem="assets/images/servicos/pessoas.jpg",
        imagem_alt="Equipe de uma distribuidora cliente reunida atrás do balcão de atendimento",
        resultado=("Mais qualidade nas contratações, menos improviso nas rotinas e maior segurança na "
                   "relação entre empresa, gestores e colaboradores."),
        titulo_diag="Quão organizada está a sua operação de pessoas?",
        assunto="servicos-pessoas-relacionamento",
        para_quem_titulo="Empresas em que a rotina de pessoal ainda depende de alguém específico.",
        para_quem=("Empresas sem RH estruturado, com dificuldade de contratação, rotatividade, processos "
                   "trabalhistas, admissões desorganizadas, falhas nas rotinas de pessoal ou dependência "
                   "excessiva de conhecimentos informais."),
        problemas=[
            "As vagas permanecem abertas ou recebem candidatos pouco aderentes.",
            "Baixa retenção e alta rotatividade.",
            "Admissões, jornadas, documentos e movimentações geram retrabalho ou risco.",
            "Reclamações e processos trabalhistas.",
            "Fragilidades nos processos de Departamento Pessoal.",
            "Ausência de um responsável experiente na área — a atuação é reativa, feita como se aprendeu.",
            "O dono faz a folha de pagamento e não consegue soltar, para não abrir a informação para a equipe — e isso consome o tempo dele em coisas mais importantes para o negócio.",
        ],
        solucoes=[
            ("Recrutamento e seleção",
             "Curadoria e estruturação de vagas: definição de perfil, divulgação, triagem, entrevistas, avaliação de evidências, parecer e apoio à decisão."),
            ("Terceirização do RH",
             "Organização ou terceirização das rotinas admissionais, jornada, benefícios, férias, desligamentos, documentos e controles."),
            ("Diagnóstico e organização do DP",
             "Levantamento de fluxos, responsabilidades, documentos e riscos operacionais, com plano de correção — feito junto ao RH ou ao próprio dono."),
            ("Carreiras e remuneração",
             "Plano de carreira, cargos e salários, políticas de remuneração e comissionamento."),
        ],
        entregas=[
            ("Mapa de fluxos e responsabilidades", "Quem faz o quê, em qual momento e com qual documento de suporte."),
            ("Plano de correção priorizado", "Separando urgência legal de organização de rotina, com responsáveis e prazos."),
            ("Rotinas de pessoal organizadas", "Admissão, jornada, benefícios, férias, desligamento e controles, com checklist."),
            ("Estrutura de cargos e salários", "Plano de carreira, políticas de remuneração e critérios de comissionamento."),
            ("Parecer de seleção com evidências", "Para que a decisão de contratação deixe de depender apenas de impressão."),
            ("Transferência de método", "O time interno assume a rotina com material utilizável e indicadores próprios."),
        ],
        formatos=["Vaga avulsa", "Pacote ou volume de vagas",
                  "Projeto de organização e assessoria do DP para o dono ou assistente",
                  "Terceirização recorrente do RH"],
        fortes=[
            "Retira o dono da execução diária da folha sem abrir informação sigilosa para toda a equipe.",
            "Reduz passivos e retrabalho em admissões, jornadas, documentos e desligamentos.",
            "Torna o processo treinável: quem sai não leva a rotina embora.",
            "Dá critério às decisões de cargo, salário e comissão, que hoje são caso a caso.",
        ],
        limites=[
            "Não substitui assessoria jurídica: questões legais especializadas são encaminhadas a profissionais habilitados.",
            "Não substitui a contabilidade nem a execução fiscal da empresa.",
            "Não resolve, por si, problema de clima ou de liderança — isso é objeto de outras duas frentes.",
            "Não funciona se a empresa quiser terceirizar o problema sem participar da construção.",
        ],
        conexao=("Pode conectar-se à gestão de talentos, à formação de gestores e à prevenção de riscos "
                 "psicossociais. Questões legais especializadas são encaminhadas para profissionais habilitados."),
        depoimento=("“A combinação entre o conhecimento técnico de Departamento Pessoal e a sensibilidade em "
                    "Psicologia Organizacional foi o diferencial. De uma forma geral, percebemos uma empresa "
                    "mais organizada, humana e alinhada.”"),
        depoente="Simone Cantu",
        depoente_cargo="Gerente de Operações e Administrativo",
        depoente_empresa="Integração Gestão Empresarial",
        cta_titulo="A sua rotina de pessoal<br>não precisa depender de você.",
        cta_sub="Solicite um orçamento para o diagnóstico e a organização do Departamento Pessoal da sua empresa.",
        **FASES_PADRAO
    ),

    # ------------------------------------------------------------------ 02
    dict(
        arquivo="servicos-recrutamento-selecao.html",
        slug="recrutamento",
        nome_curto="Recrutamento e Seleção",
        titulo="Recrutamento e Seleção — Evolve Capital Humano",
        descricao=("Recrutamento e seleção com definição de perfil, avaliação por evidências, parecer e "
                   "apoio à decisão, para reduzir erro de contratação e rotatividade."),
        indice="Frente 02 de 04 · uma solução da área Pessoas e Relações de Trabalho",
        h1a="Recrutamento",
        h1b="e Seleção.",
        pergunta=("A pergunta que esta frente responde: <strong>como colocar as pessoas certas nos "
                  "lugares certos?</strong> Curadoria e estruturação de vagas para reduzir erros de "
                  "contratação, rotatividade e perda de desempenho."),
        variante="b",
        proporcao="1.775",
        legenda="Encontro empresarial · gente certa muda o resultado de uma operação",
        imagem="assets/images/servicos/recrutamento.jpg",
        imagem_alt="Grupo numeroso de profissionais reunido ao final de um encontro empresarial",
        resultado=("Colocamos as pessoas certas nos lugares certos para reduzir erros de contratação, "
                   "rotatividade e perda de desempenho."),
        titulo_diag="Suas contratações estão acertando?",
        assunto="servicos-recrutamento-selecao",
        para_quem_titulo="Empresas que perdem tempo e dinheiro contratando por impressão.",
        para_quem=("Empresas com vagas que permanecem abertas ou recebem candidatos pouco aderentes, "
                   "baixa retenção, alta rotatividade e decisão de contratação concentrada no dono."),
        problemas=[
            "As vagas permanecem abertas ou recebem candidatos pouco aderentes ao que a função exige.",
            "Baixa retenção e alta rotatividade nas posições recém-preenchidas.",
            "O dono conduz triagem, entrevista e decisão sozinho, sem parecer técnico de apoio.",
            "Contratações feitas por urgência de preencher a vaga, não por aderência ao perfil.",
            "O custo do erro aparece depois, como retrabalho, clima ruim e desligamento.",
            "Não há plano de integração: o novo colaborador aprende olhando os outros trabalharem.",
        ],
        solucoes=[
            ("Definição de perfil", "Requisitos técnicos e comportamentais indispensáveis, desenhados junto com quem decide."),
            ("Divulgação e triagem", "Anúncio da vaga com linguagem correta e triagem por critérios definidos, não por impressão."),
            ("Entrevistas e avaliação por evidências", "Entrevistas investigativas e instrumentos adequados, buscando evidência de comportamento e não discurso."),
            ("Parecer e apoio à decisão", "Documento com o que foi identificado, limites de interpretação e recomendação — a decisão continua sendo da empresa."),
            ("Integração acompanhada", "Plano de chegada com responsável, metas do período e conversas de acompanhamento."),
        ],
        entregas=[
            ("Perfil da vaga documentado", "Requisitos técnicos e comportamentais alinhados com a diretoria antes de abrir o processo."),
            ("Funil de candidatos triado", "Somente finalistas com aderência avaliada chegam à sua mesa."),
            ("Relatório de avaliação", "Evidências coletadas, pontos de atenção e limites explícitos de interpretação."),
            ("Parecer com recomendação", "Apoio à decisão, para que a escolha final tenha base e seja transferível."),
            ("Plano de integração", "Roteiro de chegada com responsável, metas e acompanhamento nos primeiros meses."),
            ("Critério transferível", "O padrão de seleção fica registrado e pode ser repetido pela sua equipe."),
        ],
        formatos=["Vaga avulsa", "Pacote ou volume de vagas",
                  "Projeto de estruturação do processo seletivo interno"],
        fortes=[
            "Move o filtro para o começo do processo: você para de entrevistar gente desalinhada.",
            "Substitui impressão pessoal por evidência, sem tirar de você a decisão final.",
            "Reduz o custo invisível do turnover em posições recém-preenchidas.",
            "Deixa o critério registrado, para que a seleção possa ser delegada depois.",
        ],
        limites=[
            "Não emitimos laudo clínico: avaliação psicológica com finalidade clínica é outro escopo, de profissional habilitado.",
            "Não garantimos permanência de nenhum profissional — nenhum processo sério garante isso.",
            "Não resolve rotatividade causada por liderança despreparada ou por condições de trabalho.",
            "Não substitui a estruturação das rotinas de DP que sustentam a admissão.",
        ],
        conexao=("Pode conectar-se à gestão de talentos, à formação de gestores e à prevenção de riscos "
                 "psicossociais. Quando a rotatividade persiste após boas contratações, a causa costuma "
                 "estar na liderança ou nas condições de trabalho — e não na seleção."),
        depoimento=("“Tivemos uma evolução muito significativa no desenvolvimento da nossa equipe, graças aos "
                    "treinamentos executados e bem pontuados. Acredito que o seu trabalho está sendo executado "
                    "de forma consistente, com direcionamento claro, e já apresenta resultados muito expressivos.”"),
        depoente="Vanessa Ghoe",
        depoente_cargo="Diretora de Operações Externas",
        depoente_empresa="Rede Delta",
        cta_titulo="Contratar bem custa menos<br>do que contratar duas vezes.",
        cta_sub="Solicite um orçamento para a estruturação do seu processo seletivo ou para uma vaga específica.",
        **FASES_PADRAO
    ),

    # ------------------------------------------------------------------ 03
    dict(
        arquivo="servicos-riscos-saude.html",
        slug="riscos-saude",
        nome_curto="Riscos Psicossociais e Saúde Organizacional",
        titulo="Riscos Psicossociais e Saúde Organizacional — Evolve Capital Humano",
        descricao=("Avaliação de fatores de risco psicossocial, integração ao GRO/PGR, plano 5W2H e gestão "
                   "contínua das condições de trabalho, conforme a NR-1."),
        indice="Frente 03 de 04",
        h1a="Riscos Psicossociais",
        h1b="e Saúde Organizacional.",
        pergunta=("A pergunta que esta frente responde: <strong>como reconhecer e controlar fatores do "
                  "trabalho que afetam a saúde e o desempenho profissional?</strong> Transformamos exigência "
                  "normativa e sinais de desgaste em diagnóstico, prioridade e ação organizacional responsável."),
        variante="c",
        proporcao="1.808",
        legenda="Indústria metalúrgica em campo · é no posto de trabalho que o risco aparece",
        imagem="assets/images/servicos/riscos.jpg",
        imagem_alt="Equipe de uma indústria metalúrgica no galpão de produção, junto ao posto de trabalho",
        resultado=("Mais clareza sobre os fatores do trabalho que precisam ser controlados, ações "
                   "rastreáveis e melhoria contínua das condições organizacionais."),
        titulo_diag="Você sabe quais fatores do trabalho estão custando saúde e desempenho?",
        assunto="servicos-riscos-saude",
        para_quem_titulo="Empresas que precisam sair da formalidade e chegar à gestão real.",
        para_quem=("Empresas que precisam avaliar fatores de risco psicossocial no trabalho, integrar o "
                   "tema ao GRO/PGR, responder a sinais de adoecimento ou implantar um processo contínuo "
                   "de prevenção."),
        problemas=[
            "A empresa não sabe como iniciar nem como documentar a avaliação psicossocial.",
            "Existem queixas de sobrecarga, conflito, assédio, baixa autonomia ou insegurança.",
            "Indicadores de afastamento, rotatividade, horas extras ou incidentes sugerem desgaste.",
            "As ações de saúde são pontuais e não enfrentam fatores da organização do trabalho.",
            "Gestores confundem risco psicossocial com diagnóstico clínico individual.",
        ],
        solucoes=[
            ("Diagnóstico de fatores psicossociais", "Planejamento, instrumentos adequados, entrevistas, observação e análise dos indicadores organizacionais."),
            ("Relatório com plano de ação", "Mapa de fatores, níveis de atenção, evidências, limites de interpretação e recomendações."),
            ("Integração ao GRO/PGR", "Medidas organizacionais, responsáveis, prazos, indicadores e articulação com SST e profissionais habilitados."),
            ("Acompanhamento e implantação", "Monitoramento do plano de ação, reavaliações, palestras, orientação de gestores e apoio à implantação."),
            ("Supervisão do processo interno", "Para empresas que querem construir o próprio processo de avaliação e gestão de riscos, com acompanhamento técnico."),
        ],
        entregas=[
            ("Plano metodológico", "Desenho da avaliação e comunicação transparente aos participantes."),
            ("Instrumentos e análise", "Aplicação dos instrumentos, entrevistas e análise documental e de indicadores."),
            ("Relatórios consolidados", "Com evidências, níveis de atenção e limites explícitos de interpretação."),
            ("Mapa de prioridades e plano 5W2H", "O que fazer primeiro, quem responde, quando e como será verificado."),
            ("Recomendações de prevenção", "Medidas organizacionais, não apenas orientações individuais."),
            ("Rituais de acompanhamento", "Implantação das ações, registros e reavaliação periódica."),
        ],
        formatos=["Diagnóstico completo", "Projeto por unidades", "Implantação do plano",
                  "Programa contínuo", "Palestras e sensibilização", "Supervisão do processo interno"],
        fortes=[
            "Transforma a exigência normativa em gestão real, com evidência e rastreabilidade.",
            "Ataca fatores da organização do trabalho, e não apenas sintomas individuais.",
            "Integra-se ao GRO/PGR com responsáveis, prazos e indicadores definidos.",
            "Separa com clareza risco psicossocial de diagnóstico clínico individual.",
        ],
        limites=[
            "Não substitui avaliação clínica, jurídica, médica ou de engenharia de segurança.",
            "Não emite diagnóstico de saúde individual nem conduz tratamento.",
            "Não resolve o que depende de decisão da diretoria sobre dimensionamento, jornada ou processo.",
            "Não funciona como formalidade de gaveta: sem plano com responsáveis, o relatório não muda condição.",
        ],
        conexao=("Pode demandar revisão de processos, papéis, dimensionamento, relações de trabalho e "
                 "desenvolvimento das lideranças. Não substitui avaliação clínica, jurídica, médica ou de "
                 "engenharia de segurança."),
        depoimento=("“De uma forma geral, percebemos uma empresa mais organizada, humana e alinhada. O "
                    "ambiente de trabalho melhorou, as pessoas se sentem mais ouvidas e o desempenho das "
                    "equipes evoluiu de maneira consistente.”"),
        depoente="Simone Cantu",
        depoente_cargo="Gerente de Operações e Administrativo",
        depoente_empresa="Integração Gestão Empresarial",
        cta_titulo="A NR-1 pede um documento.<br>A sua empresa precisa de gestão.",
        cta_sub="Solicite um orçamento para a avaliação dos fatores psicossociais e para a integração ao GRO/PGR.",
        **FASES_PADRAO
    ),

    # ------------------------------------------------------------------ 04
    dict(
        arquivo="servicos-lideranca-desenvolvimento.html",
        slug="lideranca",
        nome_curto="Liderança e Desenvolvimento Humano",
        titulo="Liderança e Desenvolvimento Humano Organizacional — Evolve Capital Humano",
        descricao=("Formação de lideranças, mentorias, trilhas e programas corporativos que transformam "
                   "conhecimento em comportamento, decisão e autonomia."),
        indice="Frente 04 de 04",
        h1a="Liderança e Desenvolvimento",
        h1b="Humano Organizacional.",
        pergunta=("A pergunta que esta frente responde: <strong>como desenvolver quem conduz e realiza o "
                  "trabalho?</strong> Desenvolvemos competências que transformam conhecimento em "
                  "comportamento, decisões e melhores relações de trabalho."),
        variante="d",
        proporcao="1.296",
        legenda="Equipe cliente com a consultora da Evolve · a camada que conduz pessoas",
        imagem="assets/images/servicos/lideranca.jpg",
        imagem_alt="Equipe uniformizada de uma empresa cliente reunida com a consultora da Evolve ao final de um encontro",
        resultado=("Lideranças e profissionais mais conscientes, preparados e capazes de transformar "
                   "conhecimento em práticas que sustentem pessoas e resultados."),
        titulo_diag="Sua empresa decide sem você no meio?",
        assunto="servicos-lideranca-desenvolvimento",
        para_quem_titulo="Empresas que promoveram bons técnicos e ganharam gestores inseguros.",
        para_quem=("Empresas que precisam formar lideranças, preparar sucessores, fortalecer equipes, "
                   "transformar diretrizes culturais em práticas reais e fortalecer a área de gestão de pessoas."),
        problemas=[
            "As lideranças foram promovidas pela competência técnica, mas não sabem gerir pessoas.",
            "Os treinamentos acontecem sem continuidade nem aplicação no trabalho.",
            "Feedback, delegação, conflitos e cobrança dependem do estilo individual de cada líder.",
            "A empresa precisa preparar novos líderes em escala e com linguagem comum.",
            "Falta estrutura de gestão de pessoas: feedback, PDI e capacitação.",
            "Problemas de clima organizacional que ninguém consegue nomear com precisão.",
        ],
        solucoes=[
            ("Formações corporativas", "Percursos estruturados por competência, com prática, aplicação e acompanhamento."),
            ("Mentorias", "Acompanhamento individual ou em grupo para decisões, PDI, liderança e desafios concretos de gestão."),
            ("Treinamentos e workshops", "Encontros aplicados sobre comunicação, feedback, conflitos, segurança psicológica, respeito, indicadores e gestão."),
            ("Palestras", "Sensibilização e orientação para públicos amplos, conectadas ao contexto da organização."),
            ("Trilha online de formação de líderes", "Percurso escalável com fundamentos, ferramentas, exercícios, aplicação no trabalho e acompanhamento da evolução."),
            ("Gente, cultura e resultado", "Estrutura de cargos, competências, desempenho, potencial, desenvolvimento e decisões sobre a capacidade do time."),
        ],
        entregas=[
            ("Diagnóstico de necessidades", "Objetivos de aprendizagem definidos a partir da operação real, não de catálogo."),
            ("Arquitetura da trilha", "Plano de desenvolvimento com sequência, competências e critérios."),
            ("Aulas, materiais e ferramentas", "Conteúdo aplicado, com exercícios utilizáveis no dia a dia."),
            ("PDI e desafios de aplicação", "Cada líder sai com plano individual e desafios de prática acompanhados."),
            ("Avaliação em quatro níveis", "Reação, aprendizagem, aplicação e resultados possíveis."),
            ("Certificação do programa", "Conforme os critérios do programa, sem promessas de habilitação além das normas profissionais."),
        ],
        formatos=["Palestra", "Workshop", "Treinamento presencial ou online",
                  "Mentoria individual ou em grupo", "Programa corporativo",
                  "Trilha online", "Formação profissional"],
        fortes=[
            "Transforma conhecimento em comportamento observável, com aplicação acompanhada no trabalho.",
            "Cria linguagem comum de gestão entre áreas, reduzindo o “cada um do seu jeito”.",
            "Prepara a decisão para acontecer sem você, dentro de alçadas definidas.",
            "Escala: forma a próxima camada de líderes sem depender da presença de um especialista.",
        ],
        limites=[
            "Não é treinamento motivacional nem palestra de impacto sem continuidade.",
            "Não promete habilitação profissional além do que as normas permitem.",
            "Não compensa estrutura ausente: sem papéis e alçadas definidos, o líder formado volta ao padrão.",
            "Não funciona sem participação de quem executa — implantação imposta é o que combatemos.",
        ],
        conexao=("Pode integrar planos de sucessão, gestão de talentos, planos de ação psicossociais e "
                 "implantação de processos de gestão."),
        depoimento=("“O acompanhamento contínuo da equipe fez toda a diferença. A presença da Amanda trouxe "
                    "segurança, apoio e orientação tanto para coordenadores quanto para colaboradores, "
                    "ajudando a lidar melhor com desafios, conflitos e mudanças. Problemas que antes se "
                    "prolongavam passaram a ser tratados com mais rapidez e maturidade.”"),
        depoente="Simone Cantu",
        depoente_cargo="Gerente de Operações e Administrativo",
        depoente_empresa="Integração Gestão Empresarial",
        cta_titulo="Sua empresa precisa de líderes,<br>não de mais um treinamento.",
        cta_sub="Solicite um orçamento para a formação das suas lideranças, com aplicação no trabalho e acompanhamento.",
        **FASES_PADRAO
    ),
]
