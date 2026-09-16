---
version: 1.0.0
name: Evolve-Capital-Humano-Design-System
description: "A high-end, editorial boutique organizational transformation design system for Evolve Capital Humano. Fuses the structural clarity and asymmetric typography of 'The Ready' with Evolve's official brand manual identity — Off-white (#EFEFED) editorial surfaces, Azul Petróleo (#02173B) authority containers, Terracota (#9B512F) warmth highlights, high-contrast display typography set in Palash / Playfair Display style, crisp Montserrat body text, and a continuous S-curve line graphic narrative."

colors:
  canvas-editorial: "#EFEFED"          # Off-white base canvas (65% presence)
  canvas-card: "#F5F5F3"               # Soft neutral card surface
  canvas-card-pure: "#FFFFFF"          # High-contrast spotlight card
  canvas-dark: "#02173B"               # Azul Petróleo Profundo (55% authority dark background)
  canvas-dark-deep: "#010E27"          # Midnight dark split background
  
  primary-authority: "#02173B"         # Azul Petróleo (Sage archetype authority)
  accent-terracota: "#9B512F"          # Terracota Queimado (15% warmth CTA & focus)
  accent-terracota-hover: "#B85D36"    # Warm Terracota hover state
  accent-terracota-subtle: "rgba(155, 81, 47, 0.12)" # Terracota soft tag tint
  
  text-primary-dark: "#02173B"         # Deep Navy primary text on light canvas
  text-body-dark: "#475E69"            # Azul Cinza Profundo body text (35% presence)
  text-muted: "#7E7161"                # Verde Acinzentado secondary text & metadata (10%)
  text-light-pure: "#FFFFFF"           # White text on dark section
  text-light-subtle: "#D9DFE5"         # Subtle gray text on dark section
  
  point-of-light: "#698784"            # Verde Azulado Claro digital highlight (15%)
  point-of-light-subtle: "rgba(105, 135, 132, 0.15)" # Digital badge background
  
  border-soft: "rgba(2, 23, 59, 0.1)"  # Hairline border on light canvas
  border-dark: "rgba(239, 239, 237, 0.15)" # Hairline border on dark canvas

typography:
  font-display: "'Playfair Display', 'Cormorant Garamond', Georgia, serif" # Palash luxury optical weight
  font-body: "'Montserrat', 'Onest', -apple-system, BlinkMacSystemFont, sans-serif" # Maleah functional stack
  
  display-hero:
    fontFamily: var(--font-display)
    fontSize: "clamp(3rem, 6.5vw, 6rem)"
    fontWeight: "700"
    lineHeight: "1.05"
    letterSpacing: "-0.02em"
    
  headline-section:
    fontFamily: var(--font-display)
    fontSize: "clamp(2.25rem, 4vw, 3.75rem)"
    fontWeight: "700"
    lineHeight: "1.12"
    letterSpacing: "-0.015em"
    
  title-card:
    fontFamily: var(--font-body)
    fontSize: "1.5rem"
    fontWeight: "700"
    lineHeight: "1.3"
    letterSpacing: "-0.01em"

  body-lead:
    fontFamily: var(--font-body)
    fontSize: "1.25rem"
    fontWeight: "400"
    lineHeight: "1.65"
    
  body-standard:
    fontFamily: var(--font-body)
    fontSize: "1rem"
    fontWeight: "400"
    lineHeight: "1.6"

graphical-system:
  s-curve-line:
    description: "Continuous S-curve line (linha contínua em curva S) serving as a connecting vector along the scroll trajectory: CAOS → DIAGNÓSTICO → ESTRUTURA → IMPLANTAÇÃO → AUTONOMIA."
    stroke: "var(--accent-terracota)"
    strokeWidth: "2px"
    fill: "none"
    motion: "Scroll-driven SVG strokeDashoffset reveal with smooth easing."

layout-principles:
  grid: "Asymmetrical 12-column editorial grid with generous whitespace and clear hierarchy."
  container-max: "1380px"
  padding-section: "clamp(5rem, 10vw, 8.5rem)"
  card-radius: "1.25rem"

tone-of-voice:
  style: "Direct, intelligent, strategic, practical, human."
  guidelines: "Talk directly to the SMB owner/founder facing operational overload and growth ceilings. Avoid HR buzzwords, clinical psychology jargon, or generic corporate clichés."
---

---

# Sistema de Movimento Evolve — v2.0

> Referências estudadas: **The Ready** (arquivo local: efeitos fluid image da
> Squarespace — parallax, film grain, liquid, refracted lines; faixa de texto
> deslizante "A Work Design Company ✳︎" a 0.5 de velocidade), **SYPartners**,
> **Google Antigravity** (`smooth-scroll-wrapper`, sistemas de partículas WebGL
> com morphing por scroll, `data-typed-header`, cursor customizado, `data-bouncer`
> de palavras, feature explorer com autoplay, slider com controle de índice,
> cabeçalho `data-scroll-reactive`, transições curtas de 0.15–0.3s) e **Apple**
> (seções fixadas com narrativa em tempos, revelação de títulos linha por linha,
> escala sutil de fotografia, cabeçalho com desfoque, inversão de tema por seção).
>
> **Nada foi copiado.** Para cada mecanismo aprendido, foi construído um
> equivalente próprio, ancorado na identidade da Evolve: a linha contínua em
> curva S, a paleta do manual e a tese de que estrutura é o que transforma
> esforço em resultado.

## O princípio

Um único laço `requestAnimationFrame` lê o scroll uma vez por quadro e distribui
para os módulos inscritos (`assets/js/app.js`). Não há listeners de scroll
espalhados. Todo movimento tem função narrativa: se um efeito não ajuda o
empresário a entender ou a sentir algo, ele não entra.

## As doze assinaturas

| # | Nome | O que faz | Equivalente na referência | Como é diferente |
|---|------|-----------|---------------------------|------------------|
| 01 | **Fio de progresso** | Linha de 1px na borda esquerda que se desenha conforme a leitura avança, com um nó que desliza | — | Materializa a linha contínua da marca como barra de progresso; a jornada de leitura *é* a curva S |
| 02 | **Foto puxada** (`.pull-frame` + `data-pull`) | A moldura abre por `clip-path` de baixo para cima e a imagem, escalada em 1.12, desloca em contra-scroll dentro dela | Parallax de imagem do The Ready | Não é fundo deslizando: a moldura *revela* e a foto é arrancada de dentro do papel. Dois movimentos combinados, não um |
| 03 | **Linha que sobe** (`.rise`) | Cada linha de título sobe de dentro de uma máscara, com escalonamento de 90ms | Revelação de títulos da Apple | Curva `cubic-bezier(0.16,1,0.30,1)` própria e sem fade: o texto *assume a posição*, não aparece |
| 04 | **Cena fixada em três tempos** | Palco fixo por 3 alturas de tela: chegada em casa → mensagem que chega às 18:57 → reconhecimento. Zoom lento e véu que fecha | Seções fixadas da Apple | Narrativa em primeira pessoa com uma notificação real chegando por `cubic-bezier` de encaixe. Conta uma história, não demonstra um produto |
| 05 | **Ordem a partir do ruído** (canvas 2D) | ~200 traços em ângulos aleatórios giram até se alinharem numa malha, e a cor esquenta de verde acinzentado para terracota | Partículas WebGL com morphing do Antigravity | Canvas 2D leve (sem WebGL, sem biblioteca) e semanticamente literal: caos → estrutura, a tese da marca desenhada |
| 06 | **Antes → Depois com scrub** | Cada linha tem progresso 0→1: o scroll o move, o ponteiro sobre a linha assume o controle. O "antes" desfoca e recua, o "depois" ganha nitidez | Slider com setas do Antigravity | O leitor *opera* a transformação com a mão em vez de navegar entre slides. A curva S em miniatura se preenche como eixo |
| 07 | **Contadores com inércia** | Sobem, passam levemente do alvo e assentam no valor exato | — | Easing com ultrapassagem que imita ponteiro físico, não interpolação linear |
| 08 | **Territórios (ticker vertical)** | Os cinco territórios de comunicação do posicionamento giram dentro da frase-âncora | Faixa horizontal do The Ready | Vertical e dentro da frase: a leitura não é interrompida, e o conteúdo são os pilares reais da marca |
| 09 | **Faixa que inverte** | Faixa deslizante cujo sentido segue o sentido do scroll; pausa no hover | Marquee do The Ready | Reage à leitura em vez de correr indiferente |
| 10 | **Hairline magnética** (`.mag`) | Um segmento terracota de 6rem corre pela borda superior do card seguindo o ponteiro; o número sobe | Hover de cards com tilt/glow | Sem tilt 3D, sem sombra colorida. O que se move é o *fio* — coerente com uma marca feita de linha |
| 11 | **Cursor de campo** | Anel fino de 1px que segue o ponteiro com inércia; sobre elementos com `data-verb` abre e mostra o verbo ("responder", "abrir", "arrastar") | Cursor customizado do Antigravity | Traço de 1px em vez de disco preenchido, e carrega o *verbo* da ação — ensina a interface enquanto se move |
| 12 | **Medidor em curva S** | A nota 0–5 do diagnóstico preenche uma curva S; o traço esfria em terracota quando a nota é baixa e esquenta em verde azulado quando sobe | — | O gráfico é o próprio símbolo da marca funcionando como instrumento de medição |

## Nós de seção

`.no-secao` marca a entrada de cada seção com um ponto que **encaixa**
(`cubic-bezier(0.34,1.42,0.44,1)`) e emite um pulso único. É a curva S passando
por um marco da jornada: `CAOS → DIAGNÓSTICO → ESTRUTURA → IMPLANTAÇÃO → AUTONOMIA`.

## Tokens de movimento

```
--ease-rise    cubic-bezier(0.16, 1, 0.30, 1)     subida editorial
--ease-settle  cubic-bezier(0.22, 1.02, 0.30, 1)  assenta com sobra
--ease-line    cubic-bezier(0.65, 0, 0.35, 1)     traço da linha
--ease-snap    cubic-bezier(0.34, 1.42, 0.44, 1)  nó que encaixa
--dur-xs 180ms · --dur-sm 320ms · --dur-md 620ms · --dur-lg 980ms · --dur-xl 1500ms
--stagger 90ms
```

## Regras não negociáveis

1. **`prefers-reduced-motion: reduce`** desliga todo o movimento e mantém 100% do
   conteúdo visível. Cena fixada vira empilhada, canvas e cursor desaparecem.
2. **Toque** (`hover: none`, `pointer: coarse`) não recebe cursor de campo nem fio
   de progresso, e o scrub fica com ambos os lados legíveis.
3. **Sem bibliotecas de animação.** Só Lenis (25 KB) para o scroll suave.
   Nada de GSAP, Framer, Three.js ou Lottie.
4. **Nenhuma animação decorativa.** Cada uma das doze assinaturas carrega um
   argumento de venda.
