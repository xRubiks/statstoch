import itertools
import numpy as np
from collections import defaultdict

# Define the sample space Ω and the elementary probabilities p(ω)
omega = list(itertools.permutations(range(1, 6)))
p_omega = {w: 1 / len(omega) for w in omega}

# Define the random variables X and Y
def X(w):
    return w[0]

def Y(w):
    return sum(1 for i in range(5) if w[i] == i + 1)

# Calculate the image sets X(Ω) and Y(Ω)
X_image = {X(w) for w in omega}
Y_image = {Y(w) for w in omega}

# Compute the joint probabilities P(X = xi, Y = yj)
joint_prob = defaultdict(float)
for w in omega:
    joint_prob[(X(w), Y(w))] += p_omega[w]

# Calculate the expected values E(X), E(Y), and E(X * Y)
def expected_value(g):
    return sum(g(w) * p_omega[w] for w in omega)

E_X = expected_value(X)
E_Y = expected_value(Y)
E_XY = expected_value(lambda w: X(w) * Y(w))

# Compute the covariance C(X, Y)
cov_XY = E_XY - E_X * E_Y

# Output the results
print("a) Image sets:")
print(f"X(Ω) = {X_image}")
print(f"Y(Ω) = {Y_image}")

print("\nb) Joint probabilities P(X = xi, Y = yj):")
for (xi, yj), prob in joint_prob.items():
    print(f"P(X = {xi}, Y = {yj}) = {prob:.4f}")

print("\nc) Expected values:")
print(f"E(X) = {E_X:.4f}")
print(f"E(Y) = {E_Y:.4f}")
print(f"E(X * Y) = {E_XY:.4f}")

print("\nd) Covariance C(X, Y):")
print(f"C(X, Y) = {cov_XY:.4f}")