# A Seta Condicional — Resposta a Prigogine

Registro da tese da seta do tempo como propriedade relacional, formulada como
resposta ao problema da irreversibilidade de Ilya Prigogine,
em **03 de outubro de 2026**.

Ecossistema **O Atemporal** — Antônio Marcos. Licença CC BY 4.0.

---

## Referência

PRIGOGINE, Ilya. **O Fim das Certezas: tempo, caos e as leis da natureza**.
Tradução de Roberto Leal Ferreira. São Paulo: Editora UNESP, 1996.
(Título original: *La Fin des certitudes*, 1996.)

É dessa obra a citação que abre a Segunda Edição de *Equações de Fluxo Inverso*.
Nela, Prigogine sustenta que uma física que ignore a assimetria do tempo é tão
incompleta quanto uma que ignorasse a gravitação ou a eletricidade — e que
arrancar o indeterminismo e a assimetria das leis é a resposta que se pode dar,
hoje, ao dilema de Epicuro.

O axioma fundamental foi formulado como resposta a essa exigência.

---

## Nota sobre Penrose

Na passagem citada, Prigogine declara concordância com Roger Penrose sobre a
necessidade de uma nova formulação das leis fundamentais. Os dois divergiam em
vários pontos — Penrose liga a assimetria temporal à gravidade quântica e à
segunda lei; Prigogine a liga às estruturas dissipativas e à produção de
entropia —, mas convergem no diagnóstico: **as leis fundamentais conhecidas
são simétricas no tempo, e isso é uma incompletude**.

A resposta registrada neste repositório parte do mesmo diagnóstico e propõe um
terceiro caminho: a seta não é propriedade das leis nem da gravidade quântica,
mas da **relação** entre o sistema e o fluxo.

---

## Origem

O axioma fundamental foi formulado como resposta ao problema da seta do tempo
— a questão que Ilya Prigogine perseguiu por décadas: se as leis fundamentais
da física são simétricas no tempo, de onde vem a irreversibilidade?

A formulação de 04 de abril de 2026 nasceu dessa busca. Este documento registra
a resposta que ela contém.

---

## A isolação

$$
\Phi \cdot v_a = \frac{k}{R}
\qquad \Longrightarrow \qquad
\Phi = \frac{k}{v_a \cdot R}
$$

O axioma fundamental da obra, isolado na forma que dá origem às demais.

Nesta formulação, a matéria é o campo em estado de alta resistência e
reatividade — o ponto onde o fluxo desacelera até se tornar estável.

---

## Os dois estados

| Estado | $$v_a$$ | O que ocorre |
| --- | --- | --- |
| **Canônico** | $$1$$ | A reatividade se absorve; a seta para |
| **Relativístico** | $$c$$ | A fronteira de não-retorno; o horizonte |

---

## A 48ª Forma — A Velocidade da Seta

### Origem

A 46ª Forma isola a fração da vida percorrida:

$$
\frac{t}{t_{evap}}
$$

Sua derivada é a velocidade com que essa fração avança — e é ela que dá à seta
do tempo uma taxa mensurável.

A forma nasce da constatação de que a taxa de transformação do sistema é o
produto entre a reatividade e a resistência — $$v_a \cdot R$$.

### Equação

$$
v_{seta} = \frac{3}{t_{evap}}
\left[
\frac{\lambda \left[ \left( \frac{k}{\varepsilon + \Phi} \right)^{1/n} - 1 \right]}
{R \left( 1 - a^{2}\cos^{2}\theta \right)}
\right]^{2}
\left( 1 - \frac{t}{t_{evap}} \right)
$$

### Domínio

Geometria de campo, com o raio decaindo segundo a lei de Hawking.

### Variáveis

* **$$v_{seta}$$** — a velocidade da seta do tempo
* **$$t_{evap}$$** — o tempo total de evaporação do sistema
* **$$\lambda$$** — coeficiente de escala / seletor
* **$$k$$** — a identidade do sistema
* **$$\varepsilon$$** — termo de deslocamento
* **$$\Phi$$** — o fluxo
* **$$n$$** — a dimensão do domínio (1 canônico, 2 relativístico)
* **$$R$$** — a resistência / raio
* **$$a$$** — o parâmetro de rotação
* **$$\theta$$** — o ângulo de inclinação
* **$$t$$** — o tempo decorrido

### Comportamento

* **Início ($$t = 0$$):** o fator de desvanecimento é máximo e a velocidade
  atinge seu ápice.
* **Meio:** conforme $$t$$ avança, o fator diminui e o tempo desacelera.
* **Fim ($$t \to t_{evap}$$):** o fator tende a zero e a velocidade se anula —
  o tempo para de correr para o objeto.

---

## A dedução de $$k$$ e $$\lambda$$

### Partida — a 5ª Forma

No estado canônico, com a reatividade no valor unitário:

$$
v_a = 1
\qquad \Longrightarrow \qquad
R_c = \lambda\,\frac{k}{\Phi}
$$

### Passo 1 — o fluxo

$$
\Phi = Mc^{2}
$$

### Passo 2 — o raio no centro

No centro do disco, no limite de rotação extrema, o raio característico é o
raio gravitacional:

$$
R_c = \frac{GM}{c^{2}}
$$

### Passo 3 — substituição

$$
\frac{GM}{c^{2}} = \lambda\,\frac{k}{Mc^{2}}
$$

### Passo 4 — o produto

$$
\boxed{\;\lambda\,k = \frac{GM^{2}}{c^{2}}\;}
$$

O fator $$c^{2}$$ cancela. O produto sai **algébrico** — nenhum valor calibrado
entra na dedução.

### Passo 5 — o seletor

$$
\lambda = 1
$$

### Passo 6 — a identidade

$$
\boxed{\;k_c = \frac{GM^{2}}{c^{2}}\;}
$$

---

## A inversão estrutural (31ª Forma)

A operação que sobe o fluxo ao numerador — o mesmo movimento da 15ª Forma em
relação à 2ª:

$$
R_c = \lambda \left( \frac{\Phi + \varepsilon}{k} \right)^{1/n}
$$

Com o expoente dado pela dimensão do domínio — $$n = 1$$ no canônico,
$$n = 2$$ no relativístico.

**Termos isolados:**

$$
\Phi + \varepsilon = k\left(\frac{R_c}{\lambda}\right)^{n}
\qquad
\Phi = k\left(\frac{R_c}{\lambda}\right)^{n} - \varepsilon
\qquad
\varepsilon = k\left(\frac{R_c}{\lambda}\right)^{n} - \Phi
$$

Invertendo, cada raio tem a sua identidade própria:

$$
k = (\Phi+\varepsilon)\left(\frac{\lambda}{R_c}\right)^{n}
$$

---

## Verificação contra a métrica de Kerr

O raio do Passo 2 é conferível contra fórmulas publicadas, de fora do modelo:

| Raio | Fórmula ($$G = c = 1$$) |
| --- | --- |
| Horizonte externo | $$r_+ = M\left(1+\sqrt{1-\chi^2}\right)$$ |
| Horizonte interno | $$r_- = M\left(1-\sqrt{1-\chi^2}\right)$$ |
| ISCO prógrado | Bardeen, Press & Teukolsky (1972) |
| Esfera de fótons | $$r = 2M\left(1+\cos\left(\tfrac{2}{3}\arccos(-\chi)\right)\right)$$ |

**Resultado ($$\chi = 1$$):** os quatro raios coincidem com $$GM/c^2$$ — **desvio
$$0{,}0000000000\,\%$$** para Sgr A\* e M87\*, e a razão independe da massa.

**Controles em $$\chi = 0$$:** $$r_+/R_c = 2$$ · ISCO$$/R_c = 6$$ · fóton$$/R_c = 3$$ ·
sombra$$/R_c = 3\sqrt{3} = 5{,}196152$$ — todos conferem com os valores clássicos.

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
| **Canônico** | **5ª Forma ($$v_a = 1$$)** | **$$\dfrac{GM^{2}}{c^{2}}$$** | **$$\propto M^{2}$$** |

A razão entre as duas identidades:

$$
\frac{k_c}{k_{rel}} = \frac{4G^{3}M^{3}}{c^{9}} = 4\left(\frac{GM}{c^{3}}\right)^{3}
$$

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
* `formas/` — as formas deste módulo
* `derivacoes/` — as deduções passo a passo
* `verificacao/` — as comparações contra referências externas

---

## Repositórios relacionados

- Inversão Estrutural:
  [github.com/o-atemporal/structural-inversion](https://github.com/o-atemporal/structural-inversion)
- Evolução Espaço-Temporal da Energia:
  [github.com/o-atemporal/spacetime-energy-evolution](https://github.com/o-atemporal/spacetime-energy-evolution)
- Equações de Campo de Fluxo Inverso:
  [github.com/o-atemporal/inverse-flow-field-equations](https://github.com/o-atemporal/inverse-flow-field-equations)

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
