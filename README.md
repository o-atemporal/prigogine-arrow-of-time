# A Seta do Tempo Condicional — O Princípio da Proporcionalidade Inversa

Este é o repositório técnico de desenvolvimento do princípio introduzido na obra
*O Atemporal*, de autoria de **Antônio Marcos**, sob a Licença Creative Commons
Attribution 4.0 International (CC BY 4.0).

O projeto apresenta uma formulação algébrica para o problema da flecha do tempo
levantado por Ilya Prigogine: a ideia de que a passagem do tempo não é uma
constante universal, mas uma taxa governada pelas condições físicas locais do
sistema.

---

## O axioma

$$
\Phi \cdot V_a = \frac{k}{R}
$$

* **$\Phi$** — Fluxo
* **$V_a$** — Reatividade (força ou tração)
* **$k$** — Identidade do sistema
* **$R$** — Resistência ao fluxo

Daqui abre-se a perspectiva de que a matéria seja o campo em estado de alta
resistência e reatividade — o ponto onde o fluxo desacelera até se tornar estável.

---

## Os dois estados

| Estado | $$V_a$$ | O que ocorre |
| --- | --- | --- |
| Canônico | $$1$$ | A reatividade se absorve; a seta para |
| Relativístico | $$c$$ | A fronteira de não-retorno; o horizonte |

---

## Formas deste repositório

### 46ª Forma — A Fração de Vida Percorrida

$$\frac{t}{t_{evap}}$$

Isola a fração da vida já percorrida pelo sistema.

### 47ª Forma — A Direção Radial da Seta

A direção do avanço temporal no estado do sistema.

### 48ª Forma — A Velocidade da Seta

$$v_{seta} = \frac{3}{t_{evap}} \left[ \frac{\lambda\left[\left(\frac{k}{\varepsilon+\Phi}\right)^{1/n}-1\right]}{R\left(1-a^{2}\cos^{2}\theta\right)} \right]^{2} \left(1-\frac{t}{t_{evap}}\right)$$

A taxa com que a fração avança. Daqui decorre a leitura de que a passagem do
tempo decai ao longo da vida do sistema e se anula na evaporação.

---

## A dedução de $$k$$ e $$\lambda$$

### Partida — a 5ª Forma

No estado canônico, com a reatividade no valor unitário:

$$V_a = 1 \qquad \Longrightarrow \qquad R_c = \lambda\,\frac{k}{\Phi}$$

### Passo 1 — o fluxo

$$\Phi = Mc^{2}$$

### Passo 2 — o raio no centro

No centro do disco, no limite de rotação extrema, o raio característico é o
raio gravitacional:

$$R_c = \frac{GM}{c^{2}}$$

### Passo 3 — substituição

$$\frac{GM}{c^{2}} = \lambda\,\frac{k}{Mc^{2}}$$

### Passo 4 — o produto

$$\boxed{\;\lambda\,k = \frac{GM^{2}}{c^{2}}\;}$$

O fator $$c^{2}$$ cancela. O produto sai **algébrico** — nenhum valor calibrado
entra na dedução.

### Passo 5 — o seletor

$$\lambda = 1$$

### Passo 6 — a identidade

$$\boxed{\;k_c = \frac{GM^{2}}{c^{2}}\;}$$

---

## O estado canônico

No estado canônico, com a reatividade no valor unitário, a 5ª Forma se reduz a:

$$R_c = \frac{k}{\Phi}$$

e o raio característico do centro do disco, no limite de rotação extrema, é o
raio gravitacional:

$$R_c = \frac{GM}{c^{2}}$$

Disso resulta a identidade do estado canônico:

$$k_c = \frac{GM^{2}}{c^{2}}$$

Verificada contra os raios característicos da métrica de Kerr — horizonte
externo, horizonte interno, ISCO e esfera de fótons — que coincidem com
$$GM/c^{2}$$ no limite $$\chi \to 1$$, para as massas de 1, 10 e 100 massas
solares, Sgr A\* e M87\*.

---

## A inversão estrutural

A 31ª Forma registra a operação que sobe o fluxo ao numerador:

$$R_c = \lambda \left( \frac{\Phi + \varepsilon}{k} \right)^{1/n}$$

com o expoente $$1/n$$ dado pela dimensão do domínio — $$n = 1$$ no canônico,
$$n = 2$$ no relativístico.

Invertendo, cada raio tem a sua identidade própria:

$$k = (\Phi+\varepsilon)\left(\frac{\lambda}{R_c}\right)^{n}$$

---

## Verificação contra a métrica de Kerr

| Raio | Fórmula ($$G = c = 1$$) |
| --- | --- |
| Horizonte externo | $$r_+ = M\left(1+\sqrt{1-\chi^2}\right)$$ |
| Horizonte interno | $$r_- = M\left(1-\sqrt{1-\chi^2}\right)$$ |
| ISCO prógrado | Bardeen, Press & Teukolsky (1972) |
| Esfera de fótons | $$r = 2M\left(1+\cos\left(\tfrac{2}{3}\arccos(-\chi)\right)\right)$$ |

**Desvio: $$0{,}0000000000\,\%$$** para Sgr A\* e M87\*. Controles em
$$\chi = 0$$: $$r_+/R_c = 2$$ · ISCO$$/R_c = 6$$ · fóton$$/R_c = 3$$ ·
sombra$$/R_c = 3\sqrt{3} = 5{,}196152$$.

| $$\chi$$ | $$r_+/R_c$$ | ISCO$$/R_c$$ |
| --- | --- | --- |
| 0,0 | 2,000000 | 6,000000 |
| 0,5 | 1,866025 | 4,233003 |
| 0,9 | 1,435890 | 2,320883 |
| 0,99 | 1,141067 | 1,454498 |
| **1,0** | **1,000000** | **1,000000** |

---

## Termos de verificação

| Massa | $$R_c$$ (m) | $$\Phi$$ (J) | $$k_c = \dfrac{GM^{2}}{c^{2}}$$ |
| --- | --- | --- | --- |
| 1 $$M_\odot$$ | 1,477e3 | 1,788e47 | 2,938e33 |
| 10 $$M_\odot$$ | 1,477e4 | 1,788e48 | 2,938e35 |
| 100 $$M_\odot$$ | 1,477e5 | 1,788e49 | 2,938e37 |
| Sgr A\* | 6,351e9 | 7,687e53 | 5,432e46 |
| M87\* | 9,601e12 | 1,162e57 | 1,241e53 |

**Escala com a massa.** $$\dfrac{k(2M)}{k(M)} = 4{,}000000$$ ·
$$\dfrac{k(3M)}{k(M)} = 9{,}000000$$ — verificado.

**Dimensão de $$k_c$$.** Massa × comprimento (kg·m).

---

## Os dois troncos

| Tronco | Origem | $$k$$ | Escala com $$M$$ |
| --- | --- | --- | --- |
| Relativístico | 2ª Forma (expoente radial 2) | $$\dfrac{c^{7}}{4G^{2}M}$$ | $$\propto M^{-1}$$ |
| **Canônico** | **5ª Forma ($$V_a = 1$$)** | **$$\dfrac{GM^{2}}{c^{2}}$$** | **$$\propto M^{2}$$** |

A razão entre as duas identidades:

$$\frac{k_c}{k_{rel}} = \frac{4G^{3}M^{3}}{c^{9}} = 4\left(\frac{GM}{c^{3}}\right)^{3}$$

— o cubo do tempo característico da massa, verificado nas cinco massas.

---

## Relação com a Relatividade

A Relatividade Geral atribui a dilatação temporal à curvatura gravitacional.
Esta formulação propõe que o tempo desacelere pela perda da capacidade de
transformação do sistema. No limite de rotação extrema, o tempo se anula — o
estado onde a reatividade cessa.

---

## Estrutura do projeto

* `README.md` — este documento
* `seta-do-tempo.py` — implementação do estado canônico, o comparativo contra a
  métrica de Kerr e a dedução de $$\lambda$$ e $$k$$
* `formas/` — as formas deste módulo, uma por arquivo
* `derivacoes/` — as deduções passo a passo
* `verificacao/` — as comparações contra referências externas

---

## Status

$$k$$ e $$\lambda$$ são **consequência algébrica** da forma canônica e do raio
característico de Kerr. Nenhum dos dois exige calibração para ser obtido.

> **Em aberto.** A calibração do par $$(\lambda,\varepsilon)$$ no domínio onde
> $$z = 1$$, e a transformação da identidade ao longo da vida do sistema.

---

## Licença

CC BY 4.0 — a comunidade de astrofísica independente, cientistas de dados e
desenvolvedores está autorizada a compartilhar, adaptar e criar ferramentas
derivadas, mantida a atribuição obrigatória ao projeto oficial
**O Atemporal / Antônio Marcos (2026)**.

<!--
tags: o atemporal, antonio marcos, seta do tempo, prigogine, flecha do tempo,
entropia, estruturas dissipativas, equacoes de fluxo inverso, metrica de kerr,
estado canonico, proporcionalidade inversa, astrofisica independente 2026.
-->
