import random
import numpy as np
import matplotlib.pyplot as plt

# Erneute Berechnung und Sicherstellen, dass der Wert bei M=6 exakt 1 ergibt
# Diesmal durch kumulative Berechnung
M_values = np.arange(1, 7)
# Berechnung der Verteilungsfunktion ohne Normalisierung
P_values = [(m / 6)**10 - ((m - 1) / 6)**10 for m in M_values]

# Kumulative Berechnung der Verteilung bis M=6, um sicherzustellen, dass sie 1 erreicht
cumulative_P_values = np.cumsum(P_values)

# Erstellen des korrigierten Plots mit kumulierten Werten
plt.figure(figsize=(8, 6))
plt.step(M_values, cumulative_P_values, where='post', label="P(M≤m)", color='r')
plt.scatter(M_values, cumulative_P_values, color='b')
plt.xlabel("M")
plt.ylabel("P(M≤m)")
plt.title("Kumulative Verteilungsfunktion für P(M≤m)")
plt.xticks(M_values)
plt.ylim(0, 1.05)  # Erweiterung der y-Achse, damit 1 deutlich sichtbar ist
plt.grid(True)
plt.legend()
plt.show()

# Ausgabe der kumulierten Wahrscheinlichkeiten für Überprüfung
cumulative_P_values