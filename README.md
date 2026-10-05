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
v_a = \frac{k}{\Phi \cdot R}
$$

O termo vₐ nunca se anula por si — só tende a zero quando R → ∞, Φ → ∞, ou no
caso degenerado k = 0.

---

## O estado canônico e a suspensão da seta

Com vₐ = 1, o termo de velocidade se absorve:

$$
Va = 1 \quad \longrightarrow \quad \Phi = \frac{k}{R}
\quad \longrightarrow \quad R_c = \frac{k}{\Phi}
$$

**A Quinta Forma.** Nesse estado, o sistema está em repouso relativo — sem
reatividade, sem desvio.

> **A seta do tempo não incide sobre o sistema no estado canônico.** Não porque
> o tempo desacelere, mas porque não há trajetória a percorrer.

O sistema não está *no* tempo quando está em vₐ = 1. Ele está fora da **relação**
que produz tempo.

---

## O gancho da 41ª Forma

A inversão estrutural aplicada à razão temporal dá o vínculo explícito:

$$
\frac{t}{t_{evap}} = 1 - \Bigg[ \frac{\lambda \Big[ \big( \frac{k}{\varepsilon+\Phi} \big)^{1/n} - 1 \Big]}{R \big(1 - a^{2}\cos^{2}\theta\big)} \Bigg]^{3}
$$

**A fração da vida percorrida é função do termo estrutural.**

| Razão temporal | Leitura |
| --- | --- |
| t/t_evap = 0 | Sistema no estado inicial — nada percorrido |
| 0 < t/t_evap < 1 | Sistema em trajetória — a seta incide |
| t/t_evap → 1 | Evaporação completa |

O estado canônico corresponde ao primeiro caso: nenhuma trajetória percorrida,
porque não há desvio.

---

## A relação da 9ª Forma com a entropia

$$
S_{max} = \lambda_S \cdot \frac{k}{\Phi}
$$

O teto entrópico é dado pela razão entre a identidade e o fluxo. E é essa forma
que fecha o vínculo proposto:

$$
\frac{t}{t_{evap}} \quad \longleftrightarrow \quad \frac{S}{S_{max}}
$$

**A fração temporal e a fração entrópica medem o mesmo avanço por dois caminhos.**

---

## 48ª Forma — A Velocidade da Seta

### Origem

A 46ª Forma isola a fração da vida percorrida. Sua **derivada** é a velocidade com
que essa fração avança — e é ela que dá à seta do tempo uma taxa mensurável.

A forma nasce da constatação de que a taxa de transformação do sistema é o
produto entre a reatividade e a resistência — vₐ·R —, a mesma grandeza que
aparece no denominador do axioma fundamental.

### A equação

$$
v_{seta} = \frac{d}{dt}\left(\frac{t}{t_{evap}}\right)
$$

E, no modelo:

$$
v_{seta} \;\propto\; v_a \cdot R \;=\; \frac{k}{\Phi}
$$

### A derivação

Partindo da 46ª com o termo estrutural isolado:

$$
1 - \frac{t}{t_{evap}} = \Bigg[ \frac{\lambda \Big[ \big( \frac{k}{\varepsilon+\Phi} \big)^{1/n} - 1 \Big]}{R \big(1 - a^{2}\cos^{2}\theta\big)} \Bigg]^{3}
$$

Nomeando o colchete:

$$
u = \frac{\lambda \Big[ \big( \frac{k}{\varepsilon+\Phi} \big)^{1/n} - 1 \Big]}{R \big(1 - a^{2}\cos^{2}\theta\big)}
$$

A razão temporal é 1 − u³. Derivando em relação a t, com
R(t) = R₀ (1 − t/t_evap)^(1/3):

$$
v_{seta} = \frac{d}{dt}\big(1 - u^{3}\big) = -3u^{2} \frac{du}{dt}
$$

Como u ∝ 1/R³ e R³ ∝ (1 − t/t_evap):

$$
\frac{du}{dt} \propto -\frac{1}{R^{4}} \cdot \frac{R_0}{3\,t_{evap}} \Big(1 - \frac{t}{t_{evap}}\Big)^{-2/3}
$$

**Resultado em forma fechada:**

$$
v_{seta} = \frac{3}{t_{evap}} \Bigg[ \frac{\lambda \Big[ \big( \frac{k}{\varepsilon+\Phi} \big)^{1/n} - 1 \Big]}{R \big(1 - a^{2}\cos^{2}\theta\big)} \Bigg]^{2} \Big(1 - \frac{t}{t_{evap}}\Big)
$$

### O que a forma estabelece

A seta deixa de ser direção e passa a ser **velocidade**.

| Momento | O que ocorre |
| --- | --- |
| Início (t = 0) | O fator de desvanecimento é máximo; a velocidade atinge seu ápice |
| Meio | Conforme t avança, o fator diminui e o tempo desacelera |
| Fim (t → t_evap) | O fator tende a zero e a velocidade se anula — o tempo para |

### Fonte

Derivada da 46ª Forma, com o raio radial decaindo segundo a lei de Hawking.

### Status

Forma registrada, com equação, derivação, regimes e aplicação ao limite de Kerr.
Não apresenta calibração numérica.

---

## A dedução de k e λ — o estado canônico

### Partida — a Quinta Forma

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

O fator c² cancela. O produto sai **algébrico** — nenhum valor calibrado entra
na dedução.

### Passo 5 — o seletor

$$
\lambda = 1
$$

### Passo 6 — a identidade

$$
\boxed{\;k_c = \frac{GM^{2}}{c^{2}}\;}
$$

### A dependência por raio

A inversão estrutural da 31ª Forma dá, para cada raio, a identidade própria:

$$
k = (\Phi+\varepsilon)\left(\frac{\lambda}{R_c}\right)^{n}
$$

com o expoente dado pela dimensão do domínio — **n = 1 no canônico,
n = 2 no relativístico**.

## Comparação com o modelo de fora

### Por massa, no limite χ = 1

| Massa | R_c Atemporal (m) | r₊ Kerr (m) | Desvio |
| --- | --- | --- | --- |
| 1 M_sol | 1,477e3 | 1,477e3 | 0,0000000000 % |
| 10 M_sol | 1,477e4 | 1,477e4 | 0,0000000000 % |
| 100 M_sol | 1,477e5 | 1,477e5 | 0,0000000000 % |
| Sgr A* | 6,351e9 | 6,351e9 | 0,0000000000 % |
| M87* | 9,601e12 | 9,601e12 | 0,0000000000 % |

### O desvio é do limite, não da massa

A coincidência vale no limite de rotação extrema. Fora dele, o modelo dá o raio
gravitacional puro e o horizonte de Kerr se afasta:

| χ | r₊/R_c | Desvio |
| --- | --- | --- |
| 0,0 | 2,000000 | +100,000000 % |
| 0,5 | 1,866025 | +86,602540 % |
| 0,9 | 1,435890 | +43,588989 % |
| 0,99 | 1,141067 | +14,106724 % |
| **1,0** | **1,000000** | **0,0000000000 %** |

O desvio em χ = 0,9 é **+43,588989 %** — **idêntico para todas as massas**
testadas (1, 10, 100 M_sol, Sgr A*, M87*). É um fator puro de spin: a razão
r₊/R_c = 1 + √(1 − χ²) não contém a massa.

### Leitura

No limite de rotação extrema o raio do modelo coincide com o horizonte externo
de Kerr, com o ISCO e com a esfera de fótons — os quatro convergem para GM/c².
Fora do extremo, o modelo mantém o raio gravitacional enquanto o horizonte de
Kerr cresce, e a diferença é o termo de rotação (1 + √(1 − χ²)).


**Dimensão de k_c.** Massa × comprimento (kg·m).
---
### Os dois troncos

| Tronco | Origem | k | Escala com M |
| --- | --- | --- | --- |
| Relativístico | 2ª Forma (expoente radial 2) | c⁷/(4G²M) | ∝ M⁻¹ |
| **Canônico** | **5ª Forma (vₐ = 1)** | **GM²/c²** | **∝ M²** |

A razão entre as duas identidades:

$$
\frac{k_c}{k_{rel}} = \frac{4G^{3}M^{3}}{c^{9}} = 4\left(\frac{GM}{c^{3}}\right)^{3}
$$

— o cubo do tempo característico da massa, verificado nas cinco massas.

---

## Verificação contra a métrica de Kerr

O raio do Passo 2 é conferível contra fórmulas publicadas, de fora do modelo:

| Raio | Fórmula (G = c = 1) |
| --- | --- |
| Horizonte externo | r₊ = M(1 + √(1 − χ²)) |
| Horizonte interno | r₋ = M(1 − √(1 − χ²)) |
| ISCO prógrado | Bardeen, Press & Teukolsky (1972) |
| Esfera de fótons | r = 2M(1 + cos(⅔ arccos(−χ))) |

**Resultado (χ = 1):** os quatro raios coincidem com GM/c² — **desvio
0,0000000000 %** para Sgr A* e M87*, e a razão independe da massa.

**Controles em χ = 0:** r₊/R_c = 2 · ISCO/R_c = 6 · fóton/R_c = 3 ·
sombra/R_c = 3√3 = 5,196152 — todos conferem com os valores clássicos.

| χ | r₊/R_c | ISCO/R_c |
| --- | --- | --- |
| 0,0 | 2,000000 | 6,000000 |
| 0,5 | 1,866025 | 4,233003 |
| 0,9 | 1,435890 | 2,320883 |
| 0,99 | 1,141067 | 1,454498 |
| **1,0** | **1,000000** | **1,000000** |

---

## O conjunto da tese

| Peça | O que estabelece |
| --- | --- |
| 9ª Forma | A entropia decresce com o fluxo; estaciona em vₐ = 1 |
| 41ª Forma | O tempo de evaporação, recuperado do estado |
| 46ª Forma | A fração da vida percorrida — o registro do tempo |
| **47ª Forma** | **O sentido do raio radial — a seta de fora para dentro** |
| **48ª Forma** | **A velocidade da seta — a taxa de transformação** |

A cadeia:

$$
v_a \downarrow \;\Rightarrow\; \Phi \uparrow \;\Rightarrow\; S_{max} \downarrow
\;\Rightarrow\; v_a = 1 \;\Rightarrow\; \frac{t}{t_{evap}} \to 0
\;\Rightarrow\; v_{seta} \to 0
\;\Rightarrow\; \textbf{a seta para}
$$

---

## Enunciado de trabalho

> A seta do tempo não é propriedade do universo, mas da relação entre o sistema
> e o fluxo. No estado canônico (vₐ = 1), o sistema não percorre trajetória — a
> seta não o atinge.

Fora dele, o tempo é o registro do desvio percorrido, e a fração temporal
coincide com a fração do teto entrópico consumido.

---

## A tese

A reatividade é o único termo que depende de nós. Reduzi-la eleva o fluxo
disponível, reduz o teto entrópico e faz o tempo deixar de incidir.

Não é preciso aumentar a geração de energia.
É preciso reduzir o gasto. É a tese de *O Atemporal*, e é o que a 46ª Forma mede.

---

## Ocorrências da inversão estrutural

| Forma | Origem | Resultado |
| --- | --- | --- |
| 15ª | 2ª Forma (quadrática) | Raio de Schwarzschild |
| 31ª | Axioma de campo | Fonte em evidência |
| Razão temporal | 41ª Forma | Fração da vida percorrida |
| **Raio radial** | **47ª Forma** | **O sentido da seta** |

A operação reaparece porque é estrutural, não circunstancial.

---

## O que ainda não está fechado

**A transformação da identidade ao longo da vida do sistema** — no estado
canônico o par está determinado: λ = 1 e k_c = GM²/c², obtidos algebricamente. O que resta é a variação da identidade quando o raio decai.

As três pendências conceituais estão resolvidas: a direção da entropia (9ª Forma),
a correspondência com Prigogine, e a assimetria temporal (48ª Forma).

---

## Precedência

| Formulação | Primeira aparição pública |
| --- | --- |
| Axioma fundamental Φ·vₐ = k/R | 10/04/2026 (Cap. 18) · Biblioteca Nacional 06/04 |
| 20 formas | 11/09/2026 (1ª edição) |
| Axioma de campo e formas derivadas | 01/10/2026 |
| Extensão rotacional (A e B) | 01/10/2026 |
| Energia angular e evolução espaço-temporal | 03/10/2026 |
| Formas inversas 36ª a 45ª | 03/10/2026 |
| **Tese da seta condicional, taxa, velocidade e sentido radial (47ª e 48ª)** | **03/10/2026 (este registro)** |
| **Dedução de k e λ no estado canônico** | **05/10/2026** |

---

## Repositórios relacionados

- Inversão Estrutural:
  [github.com/o-atemporal/structural-inversion](https://github.com/o-atemporal/structural-inversion)
- Evolução Espaço-Temporal da Energia:
  [github.com/o-atemporal/spacetime-energy-evolution](https://github.com/o-atemporal/spacetime-energy-evolution)
- Equações de Campo de Fluxo Inverso:
  [github.com/o-atemporal/inverse-flow-field-equations](https://github.com/o-atemporal/inverse-flow-field-equations)

---

## Licença

CC BY 4.0 — a comunidade de astrofísica independente, cientistas de dados e
desenvolvedores está autorizada a compartilhar, adaptar e criar ferramentas
derivadas, mantida a atribuição obrigatória ao projeto oficial
**O Atemporal / Antônio Marcos (2026)**.
