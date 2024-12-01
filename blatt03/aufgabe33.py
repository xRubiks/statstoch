import itertools
import numpy as np
from collections import defaultdict

# Definiere den Grundraum Ω und die Elementarwahrscheinlichkeiten p(ω)
omega = list(itertools.permutations(range(1, 6)))
p_omega = {w: 1 / len(omega) for w in omega}

# Definiere die Zufallsvariablen X und Y
def X(w):
    return w[0]

def Y(w):
    return sum(1 for i in range(5) if w[i] == i + 1)

# Berechne die Bildmengen X(Ω) und Y(Ω)
X_image = {X(w) for w in omega}
Y_image = {Y(w) for w in omega}

# Berechne die gemeinsamen Wahrscheinlichkeiten P(X = xi, Y = yj)
joint_prob = defaultdict(float)
for w in omega:
    joint_prob[(X(w), Y(w))] += p_omega[w]

# Funktion zur Berechnung des Erwartungswerts E(g)
def expected_value(g):
    return sum(g(w) * p_omega[w] for w in omega)

# Berechne die Erwartungswerte E(X), E(Y) und E(X * Y)
E_X = expected_value(X)
E_Y = expected_value(Y)
E_XY = expected_value(lambda w: X(w) * Y(w))

# Berechne die Kovarianz C(X, Y)
cov_XY = E_XY - E_X * E_Y

# Ausgabe der Ergebnisse
print("a) Bildmengen:")
print(f"X(Ω) = {X_image}")
print(f"Y(Ω) = {Y_image}")

print("\nb) Gemeinsame Wahrscheinlichkeiten P(X = xi, Y = yj):")
for (xi, yj), prob in joint_prob.items():
    print(f"P(X = {xi}, Y = {yj}) = {prob:.4f}")

print("\nc) Erwartungswerte:")
print(f"E(X) = {E_X:.4f}")
print(f"E(Y) = {E_Y:.4f}")
print(f"E(X * Y) = {E_XY:.4f}")

print("\nd) Kovarianz C(X, Y):")
print(f"C(X, Y) = {cov_XY:.4f}")