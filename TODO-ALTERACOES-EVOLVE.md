# TODO — Alterações Evolve (ledger)

Prints: 36/36 cobertos · Itens totais: 117 · CLAUDE: 108 · GPT: 9 · Dúvidas: 1 (X-006)

**Placar após rodada 3 (Claude → GPT/Codex → Claude, 2026-10-03):** Feitos 112/117 · Pendentes 0 · Dúvidas 1 (X-006) · Não feitos (substituídos por instrução posterior) 3 · Do outro agente 0 (todos os itens de design foram feitos pelo GPT e conferidos)

Fonte: `jcbrain/Trabalho/Alterações - Evolve (página).md` · Backup: `../backup-pre-alteracoes-2026-10-03` · git limpo em `adfadab` antes de começar (alterações ainda **não comitadas**, ver X-006).

**Achados da Fase 0**
1. Os prints são do protótipo publicado (`Evolve_Prototipo_Interativo.html`, GitHub Pages), gerado por `build_interactive_prototype.py` a partir dos `.html`.
2. O gerador `_gerador/` estava desatualizado em relação aos `.html` (o commit `adfadab` editou os HTMLs à mão e criou `servicos-operacional-dp.html` sem gerador) → X-001.
3. Os prints 3, 4, 8 e 11 ("continuação"/"página começa com o DP") tinham **uma causa só**: em `servicos-operacional-dp.html` a seção Entregáveis fechava com `</div>` em vez de `</section>`. No protótipo isso fechava a aba do DP antes da hora e o resto da página (Escopo com honestidade, CTA, rodapé) aparecia solto embaixo de **todas** as abas.

**Onde aparece "Estruturação de Negócios" (decisão 7.3):** página nova `servicos-estruturacao-negocios.html` (title, índice "Frente 05 de 05 · Estruturação de Negócios", legenda da foto, título "O que a Estruturação de Negócios coloca em pé.", meta description) · `servicos.html` (card Frente 05; eixo: "a Evolve não se limita a RH: somos Estruturação de Negócios.") · `index.html` e `index-alternativo.html` (kicker "ESTRUTURAÇÃO DE NEGÓCIOS PARA PEQUENAS E MÉDIAS EMPRESAS"; meta description; title da alternativa) · `evolve.html` (meta description) · `carta-aberta.html` (card 05 das frentes) · **todas as páginas**: subtítulo do item "Negócio, Governança e Gestão" no menu e a opção "Estruturação de Negócios (visão geral)" no formulário de contato.

| ID | Origem | Página/arquivo alvo | Ação exata | Tipo | Resp. | Status | Evidência / motivo |
|---|---|---|---|---|---|---|---|
| A-001 | 202041 | evolve | Remover a seção "Pilares & Habilidades da Equipe" | REMOVER | CLAUDE | ✅ | `pagina_evolve.py`: bloco removido; `grep Pilares evolve.html` vazio |
| A-002 | 202222 | evolve | Remover bloco "Nacional · +10.000 · 20 anos+ · NR-1" | REMOVER | CLAUDE | ⛔ | Substituído por A-035…A-038 (instrução posterior, l.86: "não quero mais que você somente as exclua… pode manter mas alterando o design"). Bloco mantido com copy genérica |
| A-003 | 202344 | protótipo | Corrigir a causa da "continuação" depois do rodapé | CÓDIGO | CLAUDE | ✅ | DP agora vem do gerador (seções bem fechadas); `evolve.html` tinha `</main>` duplicado (X-007). Protótipo novo: no `<body>` só existem as 9 abas + script (verificado por parser) |
| A-004 | 202450 | protótipo | Remover a continuação ("Escopo com honestidade" do DP após o rodapé) | REMOVER | CLAUDE | ✅ | Some com A-003. O bloco "Escopo" continua só dentro da página do DP, no lugar certo |
| A-005 | 202520 | servicos + menu/rodapé/modal + página nova | Criar o tópico "Negócio, governança e gestão" | COPY | CLAUDE | ✅ | 5º nó do grafo e card Frente 05 (`pagina_servicos.py`), item no menu/rodapé/modal (`partes.py`), página `servicos-estruturacao-negocios.html` (`dados_servicos.py` #05), card na carta |
| A-006 | 202520 | servicos + página nova | Visual do novo tópico (nó do grafo, card, foto da página) | DESIGN | GPT | ✅ | GPT: ilustração `assets/images/servicos/estrutura-negocios.svg`; 5º nó do grafo com destaque; card 05 em grade 3+2 (Claude, `mag-grid--cinco`) |
| A-007 | 202520 | site inteiro | Renomear "Liderança e Desenvolvimento" | COPY | CLAUDE | ✅ | → **"Cursos, Palestras e Treinamentos"** (menu, rodapé, modal, grafo, cards, h1, title). Índice da página mantém o contexto: "Frente 04 de 05 · Liderança e Desenvolvimento Humano" |
| A-008 | 202604 | servicos | Excluir bloco "NR-1 · 4 fases · +10.000 · 5 a 200" | REMOVER | CLAUDE | ⛔ | Substituído por A-035…A-038; "5 a 200" trocado por "20 anos+ de experiência no mercado" |
| A-009 | 202653 | servicos (CTA final) | Trocar o "diagnóstico" por chamada de teste | COPY | CLAUDE | ✅ | "Faça agora um teste e descubra o nível de segurança ou risco que o seu setor de RH/DP está correndo. Ou converse…"; links "Ver a frente e fazer o teste" |
| A-010 | 202746 | protótipo (aba Serviços) | Remover a apresentação que continua após a página | CÓDIGO | CLAUDE | ✅ | Mesma causa de A-003 |
| A-011 | 202822 | DP | Novo título "Para quem é" | COPY | CLAUDE | ✅ | "Para empresas cuja rotina de DP depende dos sócios ou que têm dificuldade de encontrar mão de obra altamente capacitada para blindar os processos e proteger a empresa de possíveis passivos trabalhistas." Correções: "empreas"→"empresas", "cuja a"→"cuja", "tem"→"que têm", "possíveis trabalhistas"→"possíveis **passivos** trabalhistas" |
| A-012 | 202945 | DP | Retirar o que remete à parte contábil | COPY | CLAUDE | ✅ | Saíram "Processamento mensal de folha e encargos", "Painéis com custos de pessoal", "Previsibilidade de encargos", guias INSS/FGTS, DCTFWeb. Ficou: "Lançamentos e conferência da folha antes do fechamento… O cálculo e a escrituração seguem com a sua contabilidade" |
| A-013 | 203132 | protótipo (aba R&S) | R&S começava com bloco do DP | CÓDIGO | CLAUDE | ✅ | Mesma causa de A-003 (era o bloco vazado do DP, não a foto do topo) |
| A-014 | 203214 | R&S (`assets/images/servicos/recrutamento.jpg`) | Melhorar a resolução da imagem | IMAGEM | GPT | ✅ | GPT: o protótipo comprimia a foto para 900 px; agora mantém 1736×978 (conferido no arquivo gerado). Largura/altura reais no `<img>` |
| A-015 | 203237 | site inteiro | "vendido/vendemos" → "entregue/entregamos" | COPY | CLAUDE | ✅ | Rótulo "Resultado entregue" (todas as frentes); hub e carta "Não entregamos tudo para todos. Entregamos o próximo movimento"; carta "O que realmente entregamos". Restam só id/classe CSS `vendemos` (invisíveis) |
| A-016 | 203315 | R&S | Título riscado sai; trecho pequeno vira título; sem "concentrada no dono" | COPY | CLAUDE | ✅ | h2: "Empresas com vagas que permanecem abertas ou recebem candidatos pouco aderentes, baixa retenção e alta rotatividade." |
| A-017 | 203315 | R&S | Esse trecho fica grande | CÓDIGO | CLAUDE | ✅ | Virou o `h2.bloco__title`; o parágrafo pequeno saiu |
| A-018 | 203338 | R&S | "Como funciona" solto: remover | REMOVER | CLAUDE | ✅ | Sem `id="como-funciona"` na página. O processo próprio de R&S entrou no lugar das "Soluções" (A-030) |
| A-019 | 203356 | R&S | Etapas sem buraco; "… e acompanhamento da experiência, 15, 30 e 60 dias" | COPY | CLAUDE | ✅ | 8 etapas (2 linhas de 4, sem buraco); etapa 08 "Integração e acompanhamento da experiência: 15, 30 e 60 dias (90, conforme o contrato de experiência)" |
| A-020 | 203356 | R&S | Ergonomia visual da grade de etapas | DESIGN | GPT | ✅ | GPT: grade de 8 etapas em 4 colunas (2 linhas cheias) |
| A-021 | 203431 | Cursos/Liderança | Diferenciar "Soluções" e "Entregáveis" no conteúdo | COPY | CLAUDE | ✅ | Soluções = "Formatos de desenvolvimento · Seis formas de desenvolver a sua equipe."; Entregáveis = linha do tempo "antes, durante e depois" ("Do primeiro encontro ao certificado: o que fica na sua empresa.") |
| A-022 | 203431 | Cursos/Liderança | Diferenciar visualmente os dois blocos | DESIGN | GPT | ✅ | GPT: Entregáveis viraram linha do tempo Antes/Durante/Depois (`trilha-formacao`) |
| A-023 | 203456 | R&S | Excluir "Escopo com honestidade" | REMOVER | CLAUDE | ✅ | `grep` vazio em `servicos-recrutamento-selecao.html` |
| A-024 | 203507 | R&S | Excluir "Conexão com o portfólio" | REMOVER | CLAUDE | ✅ | `grep` vazio |
| A-025 | 203518 | R&S | Remover bloco de números | REMOVER | CLAUDE | ⛔ | Substituído por A-035…A-038; R&S agora mostra 60 dias de garantia · até 90 dias para finalistas de gestão · +10.000 · 20 anos |
| A-026 | 203547 | R&S | Depoimento da Cati Bock | COPY | CLAUDE | ✅ | Texto do documento; assinatura "Cati Bock · CEO" (P1). Correções: "evolve"→"Evolve" (2×), "muito assertividade"→"muita assertividade" |
| A-027 | 203620 | R&S | Diferenciais: competências, ciência comportamental, garantia de reposição | COPY | CLAUDE | ✅ | Seção "Diferenciais do nosso método · Recrutamento e seleção de alta performance." |
| A-028 | 203620 | R&S | Não dizer que não fazem vagas operacionais | COPY | CLAUDE | ✅ | "Do operacional à gestão: buscamos profissionais para as posições operacionais, para o front tático e técnico, para especialistas e para cargos de gestão." |
| A-029 | 203626 | R&S | Prazos e garantias | COPY | CLAUDE | ✅ | Seção "Prazos e garantias técnicas": Técnicas e especialistas 60 dias / garantia 60 dias; Gestão e liderança 90 dias / garantia 60 dias |
| A-030 | doc l.60–74 | R&S | Processo novo em etapas | COPY | CLAUDE | ✅ | Abertura · Curadoria da vaga · Curadoria organizacional · Busca em base ampla · Triagem e entrevista · Análise técnica, comportamental e psicossocial · Parecer técnico ao gestor (+ agenda e apoio na conversa) · Integração e acompanhamento |
| A-031 | 204033 | R&S (CTA) | Título "quebrado" | DESIGN | GPT | ✅ | GPT: título do CTA sem `<br>` forçado, com `text-wrap:balance` |
| A-032 | 204044 | Riscos | 2º problema novo | COPY | CLAUDE | ✅ | "Temos a avaliação pronta com os riscos identificados, mas precisamos de apoio para a execução e implantação do plano de ação." Correções: acentos, "identificamos"→"identificados", vírgula |
| A-033 | 204054 | Riscos (quiz antigo) | 3ª opção: "Fizemos uma aplicação…" | QUIZ | CLAUDE | ✅ | Aprovado pelo usuário (via GPT): substituiu o 3º problema do Psicossocial pela frase "Fizemos uma aplicação da avaliação dos riscos psicossociais, temos um plano de ação, mas temos dúvidas sobre os próximos passos." |
| A-034 | 204104 | Riscos | Tirar "Como funciona" | REMOVER | CLAUDE | ✅ | Sem `id="como-funciona"` |
| A-035 | 204139 + l.86 | todas as páginas com números | Design dinâmico e não repetitivo dos números | DESIGN | GPT | ✅ | GPT: cada página tem um layout próprio para os números (`indicadores--<frente>`, institucional, portfólio, carta) |
| A-036 | l.86 | idem | "20 anos de experiência no mercado" | COPY | CLAUDE | ✅ | Evolve, hub, carta, R&S, Riscos, Cursos, Negócio, Pessoas: "De experiência no mercado." Só o DP mantém "em Departamento Pessoal" (é o tema da página) |
| A-037 | l.87 | idem | Tirar o tamanho de empresa, exceto DP | COPY | CLAUDE | ✅ | "5 a 200" só no bloco de números do DP. Fora dos blocos de números, ver X-005 |
| A-038 | l.86 | idem | Números variados por página | COPY | CLAUDE | ✅ | DP: 20 anos em DP · 5 a 200 · +10.000 · Nacional. R&S: 60 dias · 90 dias · +10.000 · 20 anos. Riscos: NR-1 · 5W2H · +10.000 · 20 anos. Cursos: +10.000 · 6 formatos · 20 anos · NR-1. Negócio: Nacional · +10.000 · 20 anos · 5 frentes |
| A-039 | 204242 | Riscos (CTA) | Retirar "e para a integração ao GRO/PGR" | COPY | CLAUDE | ✅ | "Solicite um orçamento para a avaliação dos fatores psicossociais." |
| A-040 | 204257 | Cursos/Liderança | "diretrizes em comportamentos reais no dia a dia" | COPY | CLAUDE | ✅ | |
| A-041 | 204307 | Cursos/Liderança | Tirar "Como funciona" | REMOVER | CLAUDE | ✅ | |
| A-042 | 204321 | Cursos/Liderança | Remover "Formação profissional" | REMOVER | CLAUDE | ✅ | |
| A-043 | 204334 | Cursos/Liderança | "sem depender do dono" | COPY | CLAUDE | ✅ | "Escala: forma a próxima camada de líderes sem depender do dono." |
| A-044 | 204355 | Cursos/Liderança | Remover "Não promete habilitação…" | REMOVER | CLAUDE | ✅ | |
| A-045 | 204355 | Cursos/Liderança | Remover "— implantação imposta é o que combatemos" | REMOVER | CLAUDE | ✅ | Ficou "Não funciona sem participação de quem executa." |
| A-046 | 204355 | Cursos/Liderança | Adicionar "não é treinamento motivacional nem palestra de prateleira…" | COPY | CLAUDE | ✅ | Substituiu o item quase igual "Não é treinamento motivacional nem palestra de impacto sem continuidade" (para não repetir) |
| A-047 | 204355 | Cursos/Liderança | Incluir "certificados de formação" | COPY | CLAUDE | ✅ | Entregável "Depois · Certificados de formação" (substitui "Certificação do programa") |
| A-048 | 204428 | Cursos/Liderança | "a presença da empresa Evolve" | COPY | CLAUDE | ✅ | Doc diz "de empresa Evolve"; aplicado "da empresa Evolve" (concordância) |
| A-049 | 204451 | Cursos/Liderança (CTA) | Novo título | COPY | CLAUDE | ✅ | "Sua empresa precisa de gente comprometida e autorresponsável<br>e não de um treinamento motivacional." |
| C-001 | Carta | carta-aberta | "O nome da empresa ficou maior" | COPY | CLAUDE | ✅ | |
| C-002 | Carta | carta-aberta | "do lado de fora da sua pele" | COPY | CLAUDE | ✅ | |
| C-003 | Carta | carta-aberta | "…que funcione, que possa expandir, sem depender exclusivamente de você." | COPY | CLAUDE | ✅ | |
| C-004 | Carta | carta-aberta | Conferir os seis sinais | COPY | CLAUDE | ✅ | Idênticos, sem mudança |
| C-005 | Carta | carta-aberta | Grifar a frase | COPY | CLAUDE | ✅ | `<mark>` em "Eles se resolvem quando alguém entra junto com você, no problema concreto, e constrói o como." |
| C-006 | Carta | carta-aberta | "uma empresa que apoia outras empresas a crescerem" sem "consultoria" | COPY | CLAUDE | ✅ | |
| C-007 | Carta + 7.2 | carta-aberta | "Não entregamos somente treinamentos…" | COPY | CLAUDE | ✅ | "Não vendemos treinamentos" → "Não entregamos somente treinamentos" (o doc acrescenta "somente") |
| C-008 | Carta | carta-aberta | Conferir os demais parágrafos | COPY | CLAUDE | ✅ | "Por que com a gente…", "E, sim…", assinatura e "Vozes de quem viveu" já batiam |
| C-009 | A-015 | carta-aberta | "O que realmente entregamos" | COPY | CLAUDE | ✅ | |
| C-010 | A-015 | carta-aberta | "Não entregamos tudo para todos. Entregamos…" | COPY | CLAUDE | ✅ | Também no FAQ: "A Evolve substitui o meu RH interno?"; "parceiro externo" no lugar de "consultor" |
| D-001 | l.166 | DP | "Departamento Pessoal e RH" | COPY | CLAUDE | ✅ | h1 "Blindagem de RH / Departamento Pessoal e RH."; índice "Frente 01 de 05 · Departamento Pessoal e RH" |
| D-002 | l.170–171 | DP | Acompanhamento da experiência | COPY | CLAUDE | ✅ | Solução 04, Fase 04 e entregável "Acompanhamento da experiência" (15/30/60/90) |
| D-003 | l.172 | DP | Acompanhamento dos desligamentos | COPY | CLAUDE | ✅ | Solução 04 e Fase 04 |
| D-004 | l.173 | DP | Resolução de conflitos | COPY | CLAUDE | ✅ | Solução 04 |
| D-005 | l.174 | DP | Copy "ao terceirizar, terceiriza o problema" | COPY | CLAUDE | ✅ | Parágrafo em "Para quem é": "…Ao terceirizar a operação com a Evolve, você não terceiriza só a tarefa: terceiriza o problema inteiro…" |
| D-006 | l.175 | DP | Turnover, desengajamento, rotatividade, integração | COPY | CLAUDE | ✅ | Solução 04, 6º problema, entregável "Indicador de turnover" |
| D-007 | l.329 | DP + site | Nome "Blindagem de RH" e narrativa | COPY | CLAUDE | ✅ | Nome em todo o site (antes "Operacional de DP"); arquivo continua `servicos-operacional-dp.html` para não quebrar links |
| D-008 | Tudo Agrícola | DP | Escopo genérico | COPY | CLAUDE | ✅ | Fases, soluções e entregáveis reescritos (conferência documental, checklists, ponto/banco de horas, férias, folha conferida, benefícios, convenção coletiva, audiências, integração, experiência, desligamento, turnover, gestores) |
| D-009 | 7.4 | site inteiro | Nenhum nome da proposta | COPY | CLAUDE | ✅ | `grep -i "Tudo Agr\|Aline\|Onfly"` vazio |
| Q-001 | 7.1 | 5 páginas + JS + README | Excluir o quiz antigo | QUIZ | CLAUDE | ✅ | `diagnostico.js` reescrito (sem medidor nem pesos 0·1·3·5); README: seção do algoritmo trocada |
| Q-002 | Quiz | quiz | Título e subtítulo literais | QUIZ | CLAUDE | ✅ | Primeira tela do teste |
| Q-003 | Quiz + §8 | quiz | Sim 2 · Parcialmente 1 · Não 0 · Não se aplica | QUIZ | CLAUDE | ✅ | `CONFIG.VALORES` / `CONFIG.OPCOES` |
| Q-004 | Quiz | quiz | Bloco 1 (10) | QUIZ | CLAUDE | ✅ | `BLOCOS.dp` |
| Q-005 | Quiz | quiz | Bloco 2 (9) | QUIZ | CLAUDE | ✅ | `BLOCOS.sst`; "NRS" → "NRs" |
| Q-006 | Quiz | quiz | Bloco 3 (15) | QUIZ | CLAUDE | ✅ | `BLOCOS.rh` |
| Q-007 | Quiz | quiz | Bloco 4 (7) | QUIZ | CLAUDE | ✅ | `BLOCOS.lid` |
| Q-008 | Quiz | quiz SST | Não substitui análise legal/técnica | QUIZ | CLAUDE | ✅ | `BLOCOS.sst.aviso` na abertura e no rodapé do resultado |
| Q-009 | §8 | quiz | Pesos por pergunta | QUIZ | CLAUDE | ✅ | Somas 22/22/24/15 conferidas |
| Q-010 | §8 | quiz | Bloco% e Índice Geral | QUIZ | CLAUDE | ✅ | `calculaBloco` / `indiceGeral` |
| Q-011 | Quiz + §8 | quiz | Faixas % com textos exatos | QUIZ | CLAUDE | ✅ | `CONFIG.FAIXAS[].texto` |
| Q-012 | Quiz + §8 | quiz | Textos da versão em pontos como complemento | QUIZ | CLAUDE | ✅ | `CONFIG.FAIXAS[].complemento` em "O que isso significa" |
| Q-013 | §8 | quiz | Alerta ⚠️ | QUIZ | CLAUDE | ✅ | Teste: DP tudo Sim e q1=Não → 86% 🟢 com ⚠️ |
| Q-014 | §8 | quiz | Validade ≥ 70% | QUIZ | CLAUDE | ✅ | 2 de 10 → inválido, pede para completar; 7 de 10 → válido |
| Q-015 | §8 | quiz | Constantes no topo | QUIZ | CLAUDE | ✅ | Objeto `CONFIG` |
| Q-016 | Quiz + P4/P5 | quiz | Campos pedidos uma vez | QUIZ | CLAUDE | ✅ | Empresa, responsável, cidade/UF, segmento, colaboradores, RH interno, dificuldade antes; e-mail e telefone na captura. Reaproveitados entre as páginas (testado) |
| Q-017 | Quiz | quiz | Resultado parcial público | QUIZ | CLAUDE | ✅ | % + faixa + frase curta + botão "Acesse seu resultado completo" |
| Q-018 | Quiz | quiz | Captura de e-mail e contato antes do completo | QUIZ | CLAUDE | ✅ | Com consentimento LGPD |
| Q-019 | §8 | quiz | Resultado completo | QUIZ | CLAUDE | ✅ | Faixa, complemento, "⚠️ Lacunas críticas", "Pontos de atenção", visão por tema, CTA "Falar com a Evolve sobre o resultado" |
| Q-020 | Quiz + P4/P5 | quiz | Visão por bloco + Índice Geral só com os 4 | QUIZ | CLAUDE | ✅ | Teste: DP 76, SST 0, RH 50, Lid 100 → Índice 53% 🟡 (0,3·76+0,3·0+0,2·50+0,2·100=52,8) |
| Q-021 | §8 + P3 | quiz | Envio do lead | QUIZ | CLAUDE | ✅ | `CONFIG.LEAD_ENDPOINT` vazio → `localStorage` "evolve_leads_pendentes" + `console.warn`; payload com as 18 colunas do tutorial (incl. `origem`) |
| Q-022 | P3 | quiz | Honeypot e envio único | QUIZ | CLAUDE | ✅ | Campo `website` oculto; botão desabilitado; `resultado.enviado` impede reenvio |
| Q-023 | P4/P5 | 5 páginas | Quiz no mesmo lugar; bloco→página | QUIZ | CLAUDE | ✅ | `#diagnostico` em DP(dp), Riscos(sst), R&S e Pessoas(rh), Cursos(lid); progresso no `localStorage` |
| Q-024 | P4/P5 | 5 páginas | CTA de cada seção | COPY | CLAUDE | ✅ | "Faça agora um teste e descubra o nível de segurança ou risco que [o seu Departamento Pessoal / a sua empresa… em Segurança e Saúde no Trabalho / a estrutura de RH… / a liderança e a gestão…] está correndo." Botões do topo: "Fazer o teste · N perguntas" |
| Q-025 | §8 | quiz | "Faça os outros testes e veja seu índice geral" | QUIZ | CLAUDE | ✅ | |
| Q-026 | §8 | quiz | Testes dos cenários | QUIZ | CLAUDE | ✅ | Node: tudo Sim = 100% 🟢 (4 blocos); tudo Não = 0% 🔴 ⚠️; misto DP = 59% 🟡 ⚠️ (26/44); peso 3 em Não com bloco alto = 86% 🟢 ⚠️ (DP) e 80% 🟢 ⚠️ (Lid); SST 100% "Não se aplica" redistribui (86). Navegador: fluxo completo DP→SST→RH→Lid ok |
| Q-027 | §3 | quiz | UI do quiz | DESIGN | GPT | ✅ | GPT: layout em duas colunas, opções em grade 2×2, anel de pontuação colorido por faixa, foco e progresso acessíveis. Claude: foco só após interação, sem moldura no título |
| O-001 | l.397 | DP | Blindagem = operacional e processos básicos | COPY | CLAUDE | ✅ | Ver D-007/D-008 |
| O-002 | l.399 + 7.3 | site inteiro | "Estruturação de Negócios" no lugar de "consultoria" | COPY | CLAUDE | ✅ | Lista no topo deste arquivo. Mantido de propósito: FAQ "Já contratei consultoria antes… / Muita consultoria aponta falhas" (fala de **outras** consultorias, não da Evolve) |
| O-003 | l.400–408 | página nova | Escopo estratégico | COPY | CLAUDE | ✅ | 8 soluções em `servicos-estruturacao-negocios.html` |
| O-004 | l.395 | página nova | Projetos à parte → frente estratégica | COPY | CLAUDE | ✅ | Código de ética, liderança de gestores e direção, NR-1/DHO, organograma/cargos e salários, avaliação de desempenho, rituais de gestão, planejamento, OKRs/KPIs |
| X-001 | Fase 0 | `_gerador/` | Ressincronizar o gerador com os `.html` | CÓDIGO | CLAUDE | ✅ | Menu com 5 frentes; DP gerado a partir de `dados_servicos.py` (antes só existia o `.html` à mão). Gabarito com seções opcionais por página |
| X-002 | Fase 0 | protótipo | Regenerar `Evolve_Prototipo_Interativo.html` | CÓDIGO | CLAUDE | ✅ | `build_interactive_prototype.py`: página nova incluída; links `#âncora` agora rolam dentro da aba ativa (antes iam para a 1ª aba com aquele id) |
| X-003 | Fase 0 | servicos-pessoas-relacionamento | Página fora do menu desde `adfadab` | CÓDIGO | CLAUDE | ✅ | Continua gerada (com quiz do bloco 3) e sem link no menu. Vale decidir se ela deve sair do site |
| X-004 | revisão | carta-aberta (depoimento Simone Cantu) | Mesmo texto do depoimento de A-048 | COPY | CLAUDE | ✅ | Aprovado pelo usuário (via GPT): "Hoje temos a Evolve como uma ‘parte’ da nossa empresa" |
| X-005 | revisão | rodapé, FAQ e "Encaixe" da carta, home | "5 a 200 / 10 a 200 colaboradores" fora dos blocos de números | COPY | CLAUDE | ✅ | Aprovado pelo usuário (via GPT): rodapé "Atendimento a empresas de diferentes portes"; home "Empresas de diferentes portes"; carta e FAQ sem faixa. "5 a 200" só no bloco de números do DP |
| X-006 | Fase 3 | git / GitHub Pages | Commit e publicação | CÓDIGO | CLAUDE | ❓ | Nada comitado nem publicado no projeto principal. Aguardando autorização |
| X-007 | revisão | evolve | `</main>` duplicado (bug anterior) | CÓDIGO | CLAUDE | ✅ | `pagina_evolve.py`; 1 `</main>` por página |
| X-008 | revisão | servicos-* | Cache das páginas | CÓDIGO | CLAUDE | ✅ | `system.css?v=20261003-teste`, `diagnostico.js?v=20261003` |


## Rodada integrada — Codex, 2026-10-03
Usuário autorizou os dois papéis e aprovou A-033, X-004 e X-005 em conversa. Trabalho preparado em cópia isolada; estado recebido preservado no commit local 5aae389. As 36 imagens reais do documento foram inspecionadas. A contagem anterior do cabeçalho será reconciliada com as linhas reais.

| X-009 | A-014 / X-002 | build_interactive_prototype.py | Preservar 1736 px da foto de R&S no protótipo e permitir build no diretório atual | CÓDIGO | CLAUDE | ✅ | Conferido: protótipo com a foto de R&S em 1736×978; `WORKSPACE_DIR` relativo ao script |
| X-010 | Q-027 | diagnostico.js | Foco e progresso acessíveis, impedir avanço duplo, atualizar estado compartilhado entre abas | CÓDIGO | CLAUDE | ✅ | Conferido: barra de progresso com `role=progressbar`, bloqueio de clique duplo, teste atualizado ao reabrir a aba no protótipo |

## Rodada 3 — Claude, 2026-10-03 (auditoria do trabalho do GPT)
O GPT/Codex trabalhou numa cópia (`~/Documents/Codex/2026-10-03/ace/work/evolve`). O diff dele foi aplicado no projeto principal e o gerador reproduz exatamente os HTMLs dele (nenhuma edição manual em HTML).

| ID | Origem | Página/arquivo alvo | Ação exata | Tipo | Resp. | Status | Evidência / motivo |
|---|---|---|---|---|---|---|---|
| X-011 | auditoria | carta-aberta | `id="autoridade"` duplicado (seção e grade) | CÓDIGO | CLAUDE | ✅ | Removido da grade em `pagina_carta_aberta.py`; nenhum id duplicado nas páginas da LP |
| X-012 | auditoria | quiz | O foco saltava para o meio da página no carregamento | CÓDIGO | CLAUDE | ✅ | `diagnostico.js`: foco só depois do primeiro clique/envio no teste |
| X-013 | auditoria | todas as frentes | Grade de Entregáveis 5+1 com buraco | DESIGN | CLAUDE | ✅ | `system.css`: 3 colunas (2 no tablet, 1 no celular) |
| X-014 | auditoria | Riscos / hub / carta | 5 soluções e 5 frentes deixavam um cartão sozinho | DESIGN | CLAUDE | ✅ | Riscos em 5 colunas; hub e carta em 3+2 (`mag-grid--cinco`) |
| X-015 | pedido do usuário | quiz | Não expor o sistema de pontuação | QUIZ | CLAUDE | ✅ | Linha "Sim = 2 pontos…" substituída por "Responda cada pergunta com Sim, Parcialmente, Não ou Não se aplica." `grep "2 pontos"` vazio em páginas e protótipo |
| X-016 | auditoria | servidor local | A porta 8765 está sendo usada por um servidor deixado pelo Codex (serve a cópia dele) | CÓDIGO | CLAUDE | ✅ | Preview do Claude passou para a porta 8790 |

## Rodada 4 — ajustes pedidos pelo usuário (2026-10-04)

| ID | Origem | Página/arquivo alvo | Ação exata | Tipo | Resp. | Status | Evidência / motivo |
|---|---|---|---|---|---|---|---|
| R4-01 | usuário | Comece Aqui (+ home alternativa, meta da Evolve) | "Estruturação de Negócios para pequenas e médias empresas" → "para empresas" | COPY | CLAUDE | ✅ | Kicker "ESTRUTURAÇÃO DE NEGÓCIOS PARA EMPRESAS"; descrições sem "pequenas e médias" |
| R4-02 | usuário | Carta aberta | Verificar se há alteração pendente | COPY | CLAUDE | ✅ | Texto do site comparado frase a frase com a revisão do documento: nada pendente |
| R4-03 | usuário | Evolve | Verificar | COPY | CLAUDE | ✅ | Sem pendências (A-001, A-002/A-036 ok) |
| R4-04 | usuário | quiz | Conferir as perguntas com o documento | QUIZ | CLAUDE | ✅ | 41/41 iguais ao documento (única diferença proposital: "NRS" → "NRs"); textos das 4 faixas e complementos idênticos |
| R4-05 | usuário | quiz | Animação na troca de perguntas | DESIGN | CLAUDE | ✅ | Pergunta sai para a esquerda e a próxima entra pela direita (Voltar: ao contrário); traço da barra de progresso se preenche; opção escolhida pulsa |
| R4-06 | usuário | quiz | Transição da última resposta para o resultado | DESIGN | CLAUDE | ✅ | Tela "Calculando o resultado da sua empresa…" com indicador girando (1,3 s), depois o resultado entra em cascata |
| R4-07 | usuário | quiz | Número crescendo e anel sendo preenchido | DESIGN | CLAUDE | ✅ | 0% → nota em 1,5 s (resultado parcial e completo); brilho ao completar; faixa aparece no fim |
| R4-08 | usuário | quiz | Animação nos botões "Acesse seu resultado completo" / "Ver meu resultado completo" | DESIGN | CLAUDE | ✅ | Estado "carregando" com indicador girando antes da troca de tela. Tudo desligado para quem pede menos movimento no sistema |
| R4-09 | usuário | quiz | Sem ⚠️ quando a faixa é "Estruturado" (placar, visão por tema e título das lacunas) | QUIZ | CLAUDE | ✅ | `mostraAlerta()`: o alerta só aparece abaixo de 76%. A lista de lacunas críticas continua aparecendo, sem o emoji |
| R4-10 | usuário | quiz | Resultado sem coluna vazia à esquerda | DESIGN | CLAUDE | ✅ | No resultado a seção vira uma coluna (`teste--amplo`): título compacto em cima, anel e leitura lado a lado |
| R4-11 | usuário | quiz | "Fazer o teste" em branco e numa linha só; visão por tema organizada | DESIGN | CLAUDE | ✅ | Temas em 2 colunas, nome e valor na mesma linha, sem a numeração herdada; links em branco |
| R4-12 | usuário | quiz | Visão por tema com os dois nomes (tema · serviço) | QUIZ | CLAUDE | ✅ | "Departamento Pessoal · Blindagem de RH", "Segurança do Trabalho · Riscos Psicossociais", "Gestão de Pessoas · Recrutamento e Seleção", "Liderança e Gestão · Cursos, Palestras e Treinamentos" (aguardando feedback) |
