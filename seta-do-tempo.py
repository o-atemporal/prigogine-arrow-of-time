"""
O ATEMPORAL - Estado Canonico
O Atemporal / Antonio Marcos (2026) - CC BY 4.0
https://github.com/o-atemporal/prigogine-arrow-of-time

Equacao de Fluxo Inverso - Principio da Proporcionalidade Inversa
Phi . V_a = k / R     (Antonio Marcos, 2026)

Comparativo: 2 buracos negros.
  Lado A - Modelo O Atemporal   (R_c = G M / c^2)
  Lado B - Formulas reais       (metrica de Kerr)
"""

import math

G = 6.67430e-11
C = 299792458
HBAR = 1.054571817e-34
M_SUN = 1.989e30
SEG_ANO = 3.15576e7

OBJETOS = [
    ("Sgr A*", 4.3e6),
    ("M87*",   6.5e9),
]

CHI = 1.0   # rotacao extrema


def atemporal(M):
    """Lado A - modelo O Atemporal."""
    R_c = G * M / C ** 2                    # raio canonico
    k_c = G * M * M / C ** 2                # identidade canonica
    Phi = M * C ** 2                        # fluxo
    t_evap = 5120 * math.pi * G ** 2 * M ** 3 / (HBAR * C ** 4)
    return R_c, k_c, Phi, t_evap


def kerr(M, chi):
    """Lado B - formulas reais (metrica de Kerr)."""
    rg = G * M / C ** 2
    r_mais = rg * (1 + math.sqrt(1 - chi ** 2))

    z1 = 1 + (1 - chi ** 2) ** (1 / 3) * ((1 + chi) ** (1 / 3) + (1 - chi) ** (1 / 3))
    z2 = math.sqrt(3 * chi ** 2 + z1 ** 2)
    isco = rg * (3 + z2 - math.sqrt((3 - z1) * (3 + z1 + 2 * z2)))

    foton = 2 * rg * (1 + math.cos(2 / 3 * math.acos(-chi)))
    area = 8 * math.pi * rg * rg * (1 + math.sqrt(1 - chi ** 2))
    return r_mais, isco, foton, area


linha = "=" * 74

print(linha)
print("  O ATEMPORAL - Comparativo com a metrica de Kerr (chi = 1)")
print(linha)

for nome, m_solar in OBJETOS:
    M = m_solar * M_SUN
    R_c, k_c, Phi, t_evap = atemporal(M)
    r_mais, isco, foton, area = kerr(M, CHI)

    print(f"\n  {nome}   ({m_solar:.1e} M_sol)")
    print("  " + "-" * 70)
    print(f"  {'':<28}{'O ATEMPORAL':>20}{'KERR':>20}")
    print(f"  {'Raio (m)':<28}{R_c:>20.2f}{r_mais:>20.2f}")
    print(f"  {'ISCO (m)':<28}{'--':>20}{isco:>20.2f}")
    print(f"  {'Esfera de fotons (m)':<28}{'--':>20}{foton:>20.2f}")
    print(f"  {'Area do horizonte (m2)':<28}{'--':>20}{area:>20.4e}")
    print(f"  {'Desvio do modelo':<28}{abs(R_c - r_mais) / r_mais * 100:>19.10f}%")

    print(f"\n  Parametros do modelo")
    print(f"  {'k_c = G M^2/c^2':<28}{k_c:>20.4e}")
    print(f"  {'Phi = M c^2 (J)':<28}{Phi:>20.4e}")
    print(f"  {'k_c / Phi':<28}{k_c / Phi:>20.4e}")

    print(f"\n  Taxa de vida (48a Forma)")
    print(f"  {'t_evap (s)':<28}{t_evap:>20.4e}")
    print(f"  {'t_evap (anos)':<28}{t_evap / SEG_ANO:>20.4e}")
    print(f"  {'t_char = G M/c^3 (s)':<28}{G * M / C ** 3:>20.4e}")

print("\n" + linha)
print("  O Atemporal / Antonio Marcos (2026) - CC BY 4.0")
print(linha)
