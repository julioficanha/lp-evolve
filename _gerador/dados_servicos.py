# -*- coding: utf-8 -*-
"""Conteúdo das frentes. Fonte: Serviços Evolve, Posicionamento de Marca, Manual da
Cultura, Briefing de Mapeamento e o documento "Alterações - Evolve (página)" (out/2026).

Campos opcionais (o gabarito pula a seção quando faltam): bloco (teste), fases,
extras, entregas, formatos, fortes/limites, conexao, indicadores, depoimento."""

# Números de autoridade. Cada página escolhe os seus, para não repetir o mesmo bloco.
IND_NR1 = dict(valor="NR-1", label="Certificação Internacional em Segurança Psicológica do Trabalho.")
IND_PESSOAS = dict(count=10000, group=True, prefix="+", label="Pessoas impactadas direta e indiretamente, em atuação nacional.")
IND_ANOS = dict(count=20, suffix="anos+", label="De experiência no mercado.")
IND_NACIONAL = dict(valor="Nacional", label="Atuação em todo o território brasileiro.")

FASES_PADRAO = dict(
    titulo="Do diagnóstico à autonomia, em quatro fases.",
    lead=("A mesma metodologia sustenta as frentes da Evolve. Os prazos são definidos no alinhamento "
          "inicial, conforme o porte e o estágio da sua empresa."),
    passos=[
        ("Fase 01", "Diagnóstico", ["Escuta do dono, da liderança e de quem executa",
                                    "Investigação das causas antes de recomendar",
                                    "Prioridades de intervenção com evidências"]),
        ("Fase 02", "Plano de ação 5W2H", ["O que fazer, por quê, quem faz, quando e como",
                                           "Escopo, hipóteses e limites explícitos",
                                           "Critérios de conclusão combinados antes de começar"]),
        ("Fase 03", "Implantação acompanhada", ["Solução desenhada com quem conhece a operação",
                                                "Capacitação, aplicação no trabalho e ajuste",
                                                "Acompanhamento próximo, com registro dos acordos"]),
        ("Fase 04", "Transferência de método", ["Responsáveis, indicadores e próximos ciclos definidos",
                                                "Materiais simples de usar e robustos para orientar",
                                                "A empresa segue sem depender da nossa presença"]),
    ],
)

ACOMPANHAMENTO = "15, 30 e 60 dias (90, conforme o contrato de experiência)"

SERVICOS = [

    # ------------------------------------------------------------------ 01
    dict(
        arquivo="servicos-operacional-dp.html",
        slug="operacional-dp",
        bloco="dp",
        nome_curto="Blindagem de RH",
        titulo="Blindagem de RH · Departamento Pessoal e RH — Evolve Capital Humano",
        descricao=("Blindagem de RH: operação do Departamento Pessoal e estruturação dos principais processos "
                   "de RH para proteger a empresa de passivos trabalhistas."),
        indice="Frente 01 de 05 · Departamento Pessoal e RH",
        h1a="Blindagem de RH",
        h1b="Departamento Pessoal e RH.",
        pergunta=("A pergunta que esta frente responde: <strong>como proteger a empresa de passivos "
                  "trabalhistas sem que a rotina de pessoal dependa de você?</strong> Assumimos a operação do "
                  "Departamento Pessoal e estruturamos os principais processos de Recursos Humanos."),
        variante="a",
        proporcao="1.757",
        legenda="Operação de pessoal · organização que sustenta o crescimento seguro do negócio",
        imagem="assets/images/servicos/pessoas.jpg",
        imagem_width=1680, imagem_height=956,
        imagem_alt="Equipe de uma distribuidora cliente reunida atrás do balcão de atendimento",
        resultado=("Documentação em ordem, jornada e férias sob controle, folha conferida antes do fechamento "
                   "e processos de RH estruturados, com a empresa protegida de passivos trabalhistas."),
        teste_titulo=("Faça agora um teste e descubra o nível de segurança ou risco que o seu "
                      "Departamento Pessoal está correndo."),
        assunto="servicos-operacional-dp",
        para_quem_titulo=("Para empresas cuja rotina de DP depende dos sócios ou que têm dificuldade de encontrar "
                          "mão de obra altamente capacitada para blindar os processos e proteger a empresa de "
                          "possíveis passivos trabalhistas."),
        para_quem=("PMEs sem equipe de DP especializada, com retrabalho em admissões e desligamentos, atrasos "
                   "em férias e benefícios, ou receio de passivos trabalhistas."),
        para_quem_extra=("Quando a rotina do DP depende do dono, ou da ausência de um bom profissional que "
                         "domine informações tão importantes, cada folha, admissão e desligamento vira um risco "
                         "nas suas mãos. Ao terceirizar a operação com a Evolve, você não terceiriza só a "
                         "tarefa: <strong>terceiriza o problema inteiro</strong>, para quem faz disso a especialidade."),
        problemas=[
            "O dono ou o financeiro gastam horas com folha, documentos e cadastros.",
            "Contratos, termos e documentos sem assinatura ou fora da pasta do colaborador.",
            "Admissões, atestados e jornadas organizados de forma improvisada.",
            "Controle de férias e ponto defasado, gerando surpresas e riscos operacionais.",
            "Erros em rescisões, horas extras ou reajustes da convenção coletiva.",
            "Alta rotatividade, desengajamento e novos colaboradores sem integração.",
        ],
        fases=dict(
            titulo="Da auditoria inicial à rotina blindada.",
            lead=("Mapeamos as fragilidades, colocamos a documentação em ordem e assumimos a operação com "
                  "fluxos, prazos e responsáveis claros. O cálculo e a escrituração seguem com a sua "
                  "contabilidade; nós conferimos e fazemos a gestão."),
            passos=[
                ("Fase 01", "Auditoria & Diagnóstico", [
                    "Conferência documental da pasta de todos os colaboradores",
                    "Auditoria de cargos, salários, ponto e benefícios",
                    "Identificação de passivos e prioridades"]),
                ("Fase 02", "Saneamento & Padronização", [
                    "Regularização dos documentos faltantes",
                    "Checklists de admissão, férias, ponto, benefícios e rescisões",
                    "Controle de retorno e arquivamento dos documentos assinados"]),
                ("Fase 03", "Operação Acompanhada", [
                    "Lançamentos e conferência da folha antes do fechamento",
                    "Gestão de ponto, banco de horas, férias e benefícios",
                    "Suporte contínuo aos gestores"]),
                ("Fase 04", "Gestão de Pessoas & Autonomia", [
                    "Acompanhamento da experiência e dos desligamentos",
                    "Indicador de turnover e ações para reduzir a rotatividade",
                    "Equipe interna treinada para manter o padrão"]),
            ],
        ),
        solucoes_titulo="O que a Blindagem de RH coloca em pé.",
        solucoes=[
            ("Departamento Pessoal em conformidade",
             "Admissões, contratos de funcionários e de prestadores PJ, jornada e ponto, banco de horas, férias "
             "e desligamentos dentro da legislação, com documentação assinada e arquivada."),
            ("Folha conferida e benefícios geridos",
             "Lançamentos e conferência da folha antes do fechamento, em parceria com a sua contabilidade, e "
             "gestão de plano de saúde, odontológico, vale-refeição e demais benefícios."),
            ("Proteção contra passivos trabalhistas",
             "Auditoria de cargos, salários, ponto e benefícios, gestão das convenções coletivas e apoio à "
             "direção e ao jurídico em audiências trabalhistas, quando necessário."),
            ("Processos de gestão de pessoas",
             "Integração de novos colaboradores, acompanhamento da experiência e dos desligamentos, resolução "
             "de conflitos e suporte aos gestores, reduzindo turnover, desengajamento e rotatividade."),
        ],
        entregas=[
            ("Pastas funcionais em ordem", "Documentação de todos os colaboradores conferida, completa e arquivada."),
            ("Checklists e fluxo documental", "Admissão, férias, ponto, benefícios e rescisões com padrão e controle de retorno."),
            ("Calendário de férias", "Controle dos períodos aquisitivos para evitar vencimentos, pagamentos em dobro e multas."),
            ("Relatório de passivos", "Riscos trabalhistas apontados à direção, com as adequações priorizadas."),
            ("Indicador de turnover", "Rotatividade acompanhada mês a mês, com os motivos levantados nas entrevistas de desligamento."),
            ("Acompanhamento da experiência", f"Feedbacks estruturados com o gestor em {ACOMPANHAMENTO}."),
        ],
        formatos=["Terceirização completa do DP", "Assessoria e supervisão de DP interno",
                  "Projeto de auditoria e saneamento"],
        formatos_lead=("Escolhemos o formato conforme o tamanho da empresa e o volume de colaboradores. "
                       "Valores e prazos são definidos no alinhamento inicial."),
        limites_titulo="O que a Blindagem de RH resolve — e o que ela não substitui.",
        limites_lead="",
        fortes_titulo="Pontos fortes da Blindagem de RH",
        fortes=[
            "Tira dos sócios a operação e a conferência mensal do Departamento Pessoal.",
            "Mantém documentos, prazos e obrigações trabalhistas sob controle.",
            "Cria processos padronizados para que a saída de um funcionário não pare a operação.",
        ],
        limites=[
            "Não substitui assessoria jurídica contenciosa em audiências trabalhistas.",
            "Não substitui a escrituração contábil/fiscal da empresa: o cálculo segue com a sua contabilidade.",
            "Não faz seleção de pessoal (esta demanda é atendida na frente de Recrutamento e Seleção).",
        ],
        indicadores=[
            dict(count=20, suffix="anos+", label="De experiência prática em Departamento Pessoal."),
            dict(valor="5", suffix="a 200", label="Faixa de colaboradores das empresas que atendemos no DP."),
            IND_PESSOAS,
            IND_NACIONAL,
        ],
        cta_titulo="A sua rotina de DP<br>sem erros e sem dor de cabeça.",
        cta_sub="Solicite um orçamento para a Blindagem de RH: terceirização e organização do Departamento Pessoal da sua empresa.",
        cta_botao="Solicitar orçamento",
    ),

    # ------------------------------------------------------------------ 02
    dict(
        arquivo="servicos-recrutamento-selecao.html",
        slug="recrutamento",
        bloco="rh",
        nome_curto="Recrutamento e Seleção",
        titulo="Recrutamento e Seleção — Evolve Capital Humano",
        descricao=("Recrutamento e seleção com curadoria da vaga, análise técnica, comportamental e psicossocial, "
                   "parecer ao gestor, garantia de reposição e acompanhamento da experiência."),
        indice="Frente 02 de 05 · Recrutamento e Seleção",
        h1a="Recrutamento",
        h1b="e Seleção.",
        pergunta=("A pergunta que esta frente responde: <strong>como colocar as pessoas certas nos "
                  "lugares certos?</strong> Curadoria e estruturação de vagas para reduzir erros de "
                  "contratação, rotatividade e perda de desempenho."),
        variante="b",
        proporcao="1.775",
        legenda="Encontro empresarial · gente certa muda o resultado de uma operação",
        imagem="assets/images/servicos/recrutamento.jpg",
        imagem_width=1736, imagem_height=978,
        imagem_alt="Grupo numeroso de profissionais reunido ao final de um encontro empresarial",
        resultado=("Colocamos as pessoas certas nos lugares certos para reduzir erros de contratação, "
                   "rotatividade e perda de desempenho."),
        teste_titulo=("Faça agora um teste e descubra o nível de segurança ou risco que a estrutura de RH e de "
                      "gestão de pessoas da sua empresa está correndo."),
        assunto="servicos-recrutamento-selecao",
        para_quem_titulo=("Empresas com vagas que permanecem abertas ou recebem candidatos pouco aderentes, "
                          "baixa retenção e alta rotatividade."),
        para_quem="",
        problemas=[
            "As vagas permanecem abertas ou recebem candidatos pouco aderentes ao que a função exige.",
            "Baixa retenção e alta rotatividade nas posições recém-preenchidas.",
            "O dono conduz triagem, entrevista e decisão sozinho, sem parecer técnico de apoio.",
            "Contratações feitas por urgência de preencher a vaga, não por aderência ao perfil.",
            "O custo do erro aparece depois, como retrabalho, clima ruim e desligamento.",
            "Não há plano de integração: o novo colaborador aprende olhando os outros trabalharem.",
        ],
        solucoes_eyebrow="Como funciona",
        solucoes_titulo="Da abertura da vaga ao fim da experiência, em oito etapas.",
        solucoes=[
            ("Abertura da vaga",
             "Você nos procura e abre a vaga: a função, o momento da empresa e as dificuldades para preenchê-la."),
            ("Curadoria da vaga",
             "O que a empresa precisa, quanto quer pagar e para quando. Expectativa e realidade alinhadas antes de buscar candidatos."),
            ("Curadoria organizacional",
             "Empresa, função e atividades analisadas para confirmar se o que se pede é o que a empresa realmente precisa."),
            ("Busca em base ampla",
             "Uma base grande de currículos, com acesso aos sites de vagas que existem na internet."),
            ("Triagem e entrevista",
             "Triagem dos currículos por critérios definidos e entrevistas investigativas, buscando evidência e não discurso."),
            ("Análise técnica, comportamental e psicossocial",
             "Os candidatos são avaliados nas três dimensões, com instrumentos adequados e testes de perfil validados."),
            ("Parecer técnico ao gestor",
             "Quem passa no processo segue com parecer técnico ao gestor. Acompanhamos a agenda da visita à empresa e, se preciso, a conversa com o gestor."),
            ("Integração e acompanhamento da experiência",
             f"Acompanhamento do processo de integração e da experiência: {ACOMPANHAMENTO}."),
        ],
        extras=[
            dict(
                eyebrow="Diferenciais do nosso método",
                titulo="Recrutamento e seleção de alta performance.",
                lead=("Do operacional à gestão: buscamos profissionais para as posições operacionais, para o "
                      "front tático e técnico, para especialistas e para cargos de gestão."),
                cards=[
                    ("Seleção por competências",
                     "Analisamos muito além do currículo técnico. Mapeamos o perfil comportamental do candidato "
                     "para garantir que ele tenha compatibilidade real com a cultura da sua empresa."),
                    ("Uso de ciência comportamental",
                     "Utilizamos testes de perfil validados para reduzir a margem de erro na contratação."),
                    ("Garantia de reposição",
                     "Se o profissional contratado não se adaptar ou deixar a empresa dentro do prazo de garantia, "
                     "realizamos um novo processo seletivo sem custo adicional de honorários."),
                ],
            ),
            dict(
                eyebrow="Prazos e garantias técnicas",
                titulo="Prazo claro e garantia por escrito.",
                colunas=[
                    ("Técnicas e especialistas", [
                        "Tempo de processo de até 60 dias para apresentação dos candidatos finalistas.",
                        "Garantia de reposição de 60 dias corridos após a contratação."]),
                    ("Gestão e liderança", [
                        "Tempo de processo de até 90 dias para apresentação dos candidatos finalistas.",
                        "Garantia de reposição de 60 dias corridos após a contratação."]),
                ],
            ),
        ],
        entregas=[
            ("Perfil da vaga documentado", "Requisitos técnicos e comportamentais alinhados com a diretoria antes de abrir o processo."),
            ("Funil de candidatos triado", "Somente finalistas com aderência avaliada chegam à sua mesa."),
            ("Relatório de avaliação", "Evidências coletadas, pontos de atenção e limites explícitos de interpretação."),
            ("Parecer com recomendação", "Apoio à decisão, para que a escolha final tenha base e seja transferível."),
            ("Plano de integração", f"Roteiro de chegada com responsável, metas e acompanhamento em {ACOMPANHAMENTO}."),
            ("Critério transferível", "O padrão de seleção fica registrado e pode ser repetido pela sua equipe."),
        ],
        formatos=["Vaga avulsa", "Pacote ou volume de vagas",
                  "Projeto de estruturação do processo seletivo interno"],
        indicadores=[
            dict(count=60, suffix="dias", label="De garantia de reposição após a contratação."),
            dict(count=90, suffix="dias", label="No máximo, para apresentar finalistas de gestão e liderança."),
            IND_PESSOAS,
            IND_ANOS,
        ],
        depoimento=("“A Evolve já nos ajudou em vários processos seletivos aqui, sempre com muita assertividade. "
                    "Eu digo assim, nada na vida da gente é 100%, né? Mas eu tô quase que apostando minhas fichas "
                    "que tá sendo quase que 100% essa questão que a gente fez esse recrutamento, dessas últimas "
                    "pessoas que foram entrando, mas foi dito e feito como a Evolve falou, foi, como ela desenhou "
                    "o mapa da pessoa, ele foi acontecendo, sabe? Então, eu vejo que a chance de dar certo é muito "
                    "grande já por esse norte que a gente está tendo agora.”"),
        depoente="Cati Bock",
        depoente_cargo="CEO",
        depoente_empresa="",
        cta_titulo="Contratar bem custa menos do que contratar duas vezes.",
        cta_sub="Solicite um orçamento para a estruturação do seu processo seletivo ou para uma vaga específica.",
    ),

    # ------------------------------------------------------------------ 03
    dict(
        arquivo="servicos-riscos-saude.html",
        slug="riscos-saude",
        bloco="sst",
        nome_curto="Riscos Psicossociais e Saúde Organizacional",
        titulo="Riscos Psicossociais e Saúde Organizacional — Evolve Capital Humano",
        descricao=("Avaliação de fatores de risco psicossocial, integração ao GRO/PGR, plano 5W2H e gestão "
                   "contínua das condições de trabalho, conforme a NR-1."),
        indice="Frente 03 de 05 · Riscos Psicossociais e Saúde Organizacional",
        h1a="Riscos Psicossociais",
        h1b="e Saúde Organizacional.",
        pergunta=("A pergunta que esta frente responde: <strong>como reconhecer e controlar fatores do "
                  "trabalho que afetam a saúde e o desempenho profissional?</strong> Transformamos exigência "
                  "normativa e sinais de desgaste em diagnóstico, prioridade e ação organizacional responsável."),
        variante="c",
        proporcao="1.808",
        legenda="Indústria metalúrgica em campo · é no posto de trabalho que o risco aparece",
        imagem="assets/images/servicos/riscos.jpg",
        imagem_width=1728, imagem_height=956,
        imagem_alt="Equipe de uma indústria metalúrgica no galpão de produção, junto ao posto de trabalho",
        resultado=("Mais clareza sobre os fatores do trabalho que precisam ser controlados, ações "
                   "rastreáveis e melhoria contínua das condições organizacionais."),
        teste_titulo=("Faça agora um teste e descubra o nível de segurança ou risco que a sua empresa está "
                      "correndo em Segurança e Saúde no Trabalho."),
        assunto="servicos-riscos-saude",
        para_quem_titulo="Empresas que precisam sair da formalidade e chegar à gestão real.",
        para_quem=("Empresas que precisam avaliar fatores de risco psicossocial no trabalho, integrar o "
                   "tema ao GRO/PGR, responder a sinais de adoecimento ou implantar um processo contínuo "
                   "de prevenção."),
        problemas=[
            "A empresa não sabe como iniciar nem como documentar a avaliação psicossocial.",
            "Temos a avaliação pronta com os riscos identificados, mas precisamos de apoio para a execução e implantação do plano de ação.",
            "Fizemos uma aplicação da avaliação dos riscos psicossociais, temos um plano de ação, mas temos dúvidas sobre os próximos passos.",
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
        indicadores=[
            IND_NR1,
            dict(valor="5W2H", label="Plano de ação com responsável, prazo e verificação para cada fator priorizado."),
            IND_PESSOAS,
            IND_ANOS,
        ],
        depoimento=("“De uma forma geral, percebemos uma empresa mais organizada, humana e alinhada. O "
                    "ambiente de trabalho melhorou, as pessoas se sentem mais ouvidas e o desempenho das "
                    "equipes evoluiu de maneira consistente.”"),
        depoente="Simone Cantu",
        depoente_cargo="Gerente de Operações e Administrativo",
        depoente_empresa="Integração Gestão Empresarial",
        cta_titulo="A NR-1 pede um documento.<br>A sua empresa precisa de gestão.",
        cta_sub="Solicite um orçamento para a avaliação dos fatores psicossociais.",
    ),

    # ------------------------------------------------------------------ 04
    dict(
        arquivo="servicos-lideranca-desenvolvimento.html",
        slug="lideranca",
        bloco="lid",
        nome_curto="Cursos, Palestras e Treinamentos",
        titulo="Cursos, Palestras e Treinamentos — Evolve Capital Humano",
        descricao=("Cursos, palestras, treinamentos, mentorias e formação de lideranças feitos para a sua "
                   "empresa, com aplicação no trabalho, acompanhamento e certificado de formação."),
        indice="Frente 04 de 05 · Liderança e Desenvolvimento Humano",
        h1a="Cursos, Palestras",
        h1b="e Treinamentos.",
        pergunta=("A pergunta que esta frente responde: <strong>como desenvolver quem conduz e realiza o "
                  "trabalho?</strong> Desenvolvemos competências que transformam conhecimento em "
                  "comportamento, decisões e melhores relações de trabalho."),
        variante="d",
        proporcao="1.296",
        legenda="Equipe cliente com a especialista da Evolve · a camada que conduz pessoas",
        imagem="assets/images/servicos/lideranca.jpg",
        imagem_width=1400, imagem_height=1080,
        imagem_alt="Equipe uniformizada de uma empresa cliente reunida com a especialista da Evolve ao final de um encontro",
        resultado=("Lideranças e profissionais mais conscientes, preparados e capazes de transformar "
                   "conhecimento em práticas que sustentem pessoas e resultados."),
        teste_titulo=("Faça agora um teste e descubra o nível de segurança ou risco que a liderança e a gestão "
                      "da sua empresa estão correndo."),
        assunto="servicos-lideranca-desenvolvimento",
        para_quem_titulo="Empresas que promoveram bons técnicos e ganharam gestores inseguros.",
        para_quem=("Empresas que precisam formar lideranças, preparar sucessores, fortalecer equipes, "
                   "transformar diretrizes em comportamentos reais no dia a dia e fortalecer a área de gestão de pessoas."),
        problemas=[
            "As lideranças foram promovidas pela competência técnica, mas não sabem gerir pessoas.",
            "Os treinamentos acontecem sem continuidade nem aplicação no trabalho.",
            "Feedback, delegação, conflitos e cobrança dependem do estilo individual de cada líder.",
            "A empresa precisa preparar novos líderes em escala e com linguagem comum.",
            "Falta estrutura de gestão de pessoas: feedback, PDI e capacitação.",
            "Problemas de clima organizacional que ninguém consegue nomear com precisão.",
        ],
        solucoes_eyebrow="Formatos de desenvolvimento",
        solucoes_titulo="Seis formas de desenvolver a sua equipe.",
        solucoes=[
            ("Formações corporativas", "Percursos estruturados por competência, com prática, aplicação e acompanhamento."),
            ("Mentorias", "Acompanhamento individual ou em grupo para decisões, PDI, liderança e desafios concretos de gestão."),
            ("Treinamentos e workshops", "Encontros aplicados sobre comunicação, feedback, conflitos, segurança psicológica, respeito, indicadores e gestão."),
            ("Palestras", "Sensibilização e orientação para públicos amplos, conectadas ao contexto da organização."),
            ("Trilha online de formação de líderes", "Percurso escalável com fundamentos, ferramentas, exercícios, aplicação no trabalho e acompanhamento da evolução."),
            ("Gente, cultura e resultado", "Estrutura de cargos, competências, desempenho, potencial, desenvolvimento e decisões sobre a capacidade do time."),
        ],
        entregas_eyebrow="Entregáveis · antes, durante e depois",
        entregas_titulo="Do primeiro encontro ao certificado: o que fica na sua empresa.",
        entregas=[
            ("Antes · Diagnóstico de necessidades", "Objetivos de aprendizagem definidos a partir da operação real, não de catálogo."),
            ("Antes · Arquitetura da trilha", "Sequência, competências e critérios desenhados para a sua empresa."),
            ("Durante · Aulas, materiais e ferramentas", "Conteúdo aplicado, com exercícios utilizáveis no dia a dia."),
            ("Durante · Desafios de aplicação", "Cada participante leva a prática para o trabalho, com acompanhamento."),
            ("Depois · PDI e avaliação em quatro níveis", "Plano individual por líder e avaliação de reação, aprendizagem, aplicação e resultados possíveis."),
            ("Depois · Certificados de formação", "Cada participante recebe o certificado da formação concluída."),
        ],
        formatos=["Palestra", "Workshop", "Treinamento presencial ou online",
                  "Mentoria individual ou em grupo", "Programa corporativo", "Trilha online"],
        fortes=[
            "Transforma conhecimento em comportamento observável, com aplicação acompanhada no trabalho.",
            "Cria linguagem comum de gestão entre áreas, reduzindo o “cada um do seu jeito”.",
            "Prepara a decisão para acontecer sem você, dentro de alçadas definidas.",
            "Escala: forma a próxima camada de líderes sem depender do dono.",
        ],
        limites=[
            "Não é treinamento motivacional nem palestra de prateleira. Fazemos específico para a sua empresa.",
            "Não compensa estrutura ausente: sem papéis e alçadas definidos, o líder formado volta ao padrão.",
            "Não funciona sem participação de quem executa.",
        ],
        conexao=("Pode integrar planos de sucessão, gestão de talentos, planos de ação psicossociais e "
                 "implantação de processos de gestão."),
        indicadores=[
            IND_PESSOAS,
            dict(count=6, suffix="formatos", label="Formações, mentorias, treinamentos, palestras, trilha online e programas de cultura."),
            IND_ANOS,
            IND_NR1,
        ],
        depoimento=("“O acompanhamento contínuo da equipe fez toda a diferença. A presença da empresa Evolve trouxe "
                    "segurança, apoio e orientação tanto para coordenadores quanto para colaboradores, "
                    "ajudando a lidar melhor com desafios, conflitos e mudanças. Problemas que antes se "
                    "prolongavam passaram a ser tratados com mais rapidez e maturidade.”"),
        depoente="Simone Cantu",
        depoente_cargo="Gerente de Operações e Administrativo",
        depoente_empresa="Integração Gestão Empresarial",
        cta_titulo="Sua empresa precisa de gente comprometida e autorresponsável<br>e não de um treinamento motivacional.",
        cta_sub="Solicite um orçamento para cursos, palestras e treinamentos feitos para a sua empresa, com aplicação no trabalho e acompanhamento.",
    ),

    # ------------------------------------------------------------------ 05
    dict(
        arquivo="servicos-estruturacao-negocios.html",
        slug="estruturacao",
        nome_curto="Negócio, Governança e Gestão",
        titulo="Negócio, Governança e Gestão · Estruturação de Negócios — Evolve Capital Humano",
        descricao=("Estruturação de Negócios: governança, sucessão, remodelagem de negócio, indicadores, processos, "
                   "cultura organizacional e gestão de talentos para empresas que querem crescer sem depender do dono."),
        indice="Frente 05 de 05 · Estruturação de Negócios",
        h1a="Negócio, Governança",
        h1b="e Gestão.",
        pergunta=("A pergunta que esta frente responde: <strong>como estruturar a empresa para crescer sem "
                  "depender exclusivamente do dono?</strong> É a frente mais estratégica da Evolve: construímos "
                  "modelos de gestão que tornam a empresa mais organizada, eficiente, segura e preparada para crescer."),
        variante="c",
        proporcao="1.778",
        legenda="Estruturação de Negócios · a empresa que funciona sem depender de você",
        imagem="assets/images/servicos/estrutura-negocios.svg",
        imagem_width=960, imagem_height=680,
        imagem_alt="Estratégia conectada a governança, processos, pessoas e indicadores",
        resultado=("Uma empresa que funciona melhor, com estratégia, pessoas, processos, segurança jurídica e "
                   "saúde organizacional integrados no mesmo movimento."),
        assunto="servicos-estruturacao-negocios",
        para_quem_titulo="Empresas que cresceram no esforço e agora precisam de estrutura para continuar crescendo.",
        para_quem=("Negócios em expansão, profissionalização, reorganização ou sucessão, ainda dependentes "
                   "dos donos ou de poucas pessoas-chave."),
        problemas=[
            "Você participa de quase todas as decisões e não consegue se afastar.",
            "As áreas trabalham muito, mas sem direção nem indicadores comuns.",
            "Os processos dependem de pessoas específicas e não estão claramente definidos.",
            "Há bom faturamento, mas pouca clareza sobre margem, prioridades ou sustentabilidade.",
            "A sucessão e a continuidade do negócio ainda não foram planejadas.",
            "Você não dá mais conta sozinho, e se tornou refém do próprio negócio.",
        ],
        solucoes_titulo="O que a Estruturação de Negócios coloca em pé.",
        solucoes=[
            ("Governança e sucessão", "Papéis, alçadas e ritos de decisão definidos, e a continuidade do negócio preparada."),
            ("Remodelagem de negócio e planejamento", "Revisão do modelo de negócio e planejamento estratégico, com prioridades claras e sustentáveis."),
            ("Indicadores, OKRs e KPIs", "Metas e indicadores comuns entre as áreas, acompanhados em rituais de gestão."),
            ("Processos macro e micro", "Fluxos, responsáveis e critérios descritos, para que a operação não dependa de pessoas específicas."),
            ("Cultura e transformação organizacional", "Pilares da cultura construídos com a direção, código de ética e conduta e a mudança conduzida com quem executa."),
            ("Gestão de talentos e carreira", "Organograma, cargos e salários, avaliação de desempenho e plano de carreira estratégico."),
            ("Desenvolvimento de gestores e direção", "Treinamento e desenvolvimento de liderança para que as decisões aconteçam sem você no meio."),
            ("DHO e adequação à NR-1", "Desenvolvimento humano e organizacional integrado à gestão dos riscos psicossociais exigida pela NR-1."),
        ],
        indicadores=[
            IND_NACIONAL,
            IND_PESSOAS,
            IND_ANOS,
            dict(valor="5", suffix="frentes", label="Pessoas, processos, saúde organizacional, liderança e estratégia no mesmo movimento."),
        ],
        depoimento=("“A parceria com a Evolve foi um marco muito positivo para a nossa empresa. No decorrer do "
                    "tempo elaboramos vários projetos e muito desenvolvimento pessoal e profissional na equipe interna.”"),
        depoente="Simone Cantu",
        depoente_cargo="Gerente de Operações e Administrativo",
        depoente_empresa="Integração Gestão Empresarial",
        cta_titulo="Uma empresa que funciona<br>sem depender exclusivamente de você.",
        cta_sub="Converse com a equipe da Evolve sobre a estruturação do seu negócio.",
        cta_botao="Conversar sobre minha empresa",
    ),

    # ------------------------------------------------- fora do menu desde set/2026
    dict(
        arquivo="servicos-pessoas-relacionamento.html",
        slug="pessoas-relacoes",
        bloco="rh",
        nome_curto="Pessoas e Relações de Trabalho",
        titulo="Pessoas e Relações de Trabalho — Evolve Capital Humano",
        descricao=("Contratar e administrar pessoas com segurança e organização: recrutamento, rotinas de "
                   "Departamento Pessoal, carreiras e remuneração para PMEs."),
        indice="Pessoas e Relações de Trabalho",
        h1a="Pessoas e Relações",
        h1b="de Trabalho.",
        pergunta=("A pergunta que esta frente responde: <strong>como contratar e administrar pessoas "
                  "com segurança e organização?</strong> Ajudamos a empresa a trazer as pessoas certas e "
                  "a sustentar relações de trabalho organizadas, claras e seguras."),
        variante="a",
        proporcao="1.757",
        legenda="Distribuidora cliente · a rotina de pessoal que sustenta o atendimento",
        imagem="assets/images/servicos/pessoas.jpg",
        imagem_width=1680, imagem_height=956,
        imagem_alt="Equipe de uma distribuidora cliente reunida atrás do balcão de atendimento",
        resultado=("Mais qualidade nas contratações, menos improviso nas rotinas e maior segurança na "
                   "relação entre empresa, gestores e colaboradores."),
        teste_titulo=("Faça agora um teste e descubra o nível de segurança ou risco que a estrutura de RH e de "
                      "gestão de pessoas da sua empresa está correndo."),
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
        fases=FASES_PADRAO,
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
        indicadores=[IND_NR1, IND_PESSOAS, IND_ANOS, IND_NACIONAL],
        depoimento=("“A combinação entre o conhecimento técnico de Departamento Pessoal e a sensibilidade em "
                    "Psicologia Organizacional foi o diferencial. De uma forma geral, percebemos uma empresa "
                    "mais organizada, humana e alinhada.”"),
        depoente="Simone Cantu",
        depoente_cargo="Gerente de Operações e Administrativo",
        depoente_empresa="Integração Gestão Empresarial",
        cta_titulo="A sua rotina de pessoal<br>não precisa depender de você.",
        cta_sub="Solicite um orçamento para a organização do Departamento Pessoal da sua empresa.",
    ),
]
