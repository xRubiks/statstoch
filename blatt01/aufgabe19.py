import numpy as np
from scipy.stats import binom


def tordifferenz_verteilung(n, p):
    # Berechne die Wahrscheinlichkeiten für X und Y
    x_wahrscheinlichkeiten = [binom.pmf(k, n, p) for k in range(n + 1)]
    y_wahrscheinlichkeiten = [binom.pmf(k, n, p) for k in range(n + 1)]

    # Wahrscheinlichkeiten für Z = X - Y
    z_verteilung = {}

    # Berechne die Wahrscheinlichkeiten von Z
    for x in range(n + 1):
        for y in range(n + 1):
            z = x - y
            if z not in z_verteilung:
                z_verteilung[z] = 0
            z_verteilung[z] += x_wahrscheinlichkeiten[x] * y_wahrscheinlichkeiten[y]

    return z_verteilung


# Setze n und p
n = 5
p = 3 / 4

# Berechne die Verteilung von Z
z_distribution = tordifferenz_verteilung(n, p)

# Ausgabe der Verteilung
for z, prob in sorted(z_distribution.items()):
    print(f"P(Z = {z}) = {prob:.4f}")
