import random
import numpy as np
import matplotlib.pyplot as plt

def simulate_sammelbilder(n, trials):
    total_riegel_pro_sammlung = 0  # Gesamtanzahl der Schokoriegel pro vollständiger Sammlung
    schritte = [0] * n  # Schritte, um von i auf i+1 verschiedene Bilder zu kommen

    for _ in range(trials):
        gesammelt = set()  # Set der gesammelten Bilder
        riegel = 0  # Anzahl der verbrauchten Schokoriegel
        schritte_i = [0] * n  # Schokoriegel, um von i auf i+1 zu kommen
        bisher = 0  # Anzahl der bisher gesammelten unterschiedlichen Bilder

        while len(gesammelt) < n:
            bild = random.randint(0, n - 1)  # Zufällig ein neues Bild ziehen
            riegel += 1

            if bild not in gesammelt:
                gesammelt.add(bild)
                # Schritte protokollieren: von i = len(gesammelt)-1 auf len(gesammelt)
                schritte_i[len(gesammelt) - 1] = riegel - bisher
                bisher = riegel

        total_riegel_pro_sammlung += riegel
        # Schritte zu den gesamt Schritten addieren
        for i in range(n):
            schritte[i] += schritte_i[i]

    # Mittlere Anzahl der verbrauchten Schokoriegel pro vollständiger Sammlung
    durchschnitt_riegel = total_riegel_pro_sammlung / trials

    # Durchschnittliche Schritte, um von i auf i+1 zu kommen
    durchschnitt_schritte = [schritte[i] / trials for i in range(n)]

    return durchschnitt_riegel, durchschnitt_schritte

def plot_results(n, durchschnitt_schritte):
    plt.bar(range(1, n + 1), durchschnitt_schritte, color='blue')
    plt.xlabel('Anzahl der verschiedenen Bilder')
    plt.ylabel('Mittlere Anzahl der Schokoriegel')
    plt.title('Mittlere Anzahl der Schokoriegel, um von i auf i+1 zu kommen')
    plt.show()

# Parameter
n = 63  # Anzahl der verschiedenen Sammelbilder
trials = 10000  # Anzahl der Wiederholungen der Simulation

# Simulation starten
durchschnitt_riegel, durchschnitt_schritte = simulate_sammelbilder(n, trials)

# Ergebnisse ausgeben
print(f"Mittlere Anzahl von Schokoriegeln für eine vollständige Sammlung (n={n}): {durchschnitt_riegel:.2f}\n")
print("Mittlere Anzahl von Schokoriegeln, um von i auf i+1 zu kommen:")
for i, schritte in enumerate(durchschnitt_schritte):
    print(f"Von {i} auf {i + 1}: {schritte:.2f} Schokoriegel")

# Ergebnisse grafisch darstellen
plot_results(n, durchschnitt_schritte)