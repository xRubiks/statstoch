import random
import numpy as np
import matplotlib.pyplot as plt

def seeleute(n, trials):
    total_correct = 0
    correct_counts = [0] * (n + 1)  # Liste zur Speicherung der Häufigkeit der korrekten Zuordnungen

    for _ in range(trials):
        betten = list(range(n))
        random.shuffle(betten)
        correct = sum(1 for i in range(n) if betten[i] == i)
        total_correct += correct
        correct_counts[correct] += 1  # Häufigkeit der korrekten Zuordnungen erhöhen

    return total_correct / trials, correct_counts

def plot_results(n, correct_counts, trials):
    plt.stem(range(n + 1), correct_counts, linefmt='b-', markerfmt='bo', basefmt='r-')
    plt.xlabel('Anzahl der Seeleute im richtigen Bett')
    plt.ylabel('Häufigkeit')
    plt.title(f'Häufigkeit der korrekten Zuordnungen bei {trials} Versuchen')
    plt.show()

n = 3
trials = 1000000
average_correct, correct_counts = seeleute(n, trials)

print(f"Durchschnittlich liegen {average_correct:.2f} von {n} Seeleuten im richtigen Bett.")

# Ergebnisse grafisch darstellen
plot_results(n, correct_counts, trials)

def seeleute_simulation(n, trials):
    correct_counts = [0] * (n + 1)  # Liste zur Speicherung der Häufigkeit der korrekten Zuordnungen

    for _ in range(trials):
        betten = list(range(n))
        random.shuffle(betten)
        correct = sum(1 for i in range(n) if betten[i] == i)
        correct_counts[correct] += 1  # Häufigkeit der korrekten Zuordnungen erhöhen

    # Umrechnung der Häufigkeit in Wahrscheinlichkeiten
    probabilities = [count / trials for count in correct_counts]
    return probabilities

# Parameter
n = 3  # Anzahl der Seeleute
trials = 1000000  # Anzahl der Versuche

# Wahrscheinlichkeiten für die Anzahl der Seeleute im richtigen Bett
probabilities = seeleute_simulation(n, trials)

# Kumulierte Wahrscheinlichkeiten für die Verteilungsfunktion F_X
cumulative_probabilities = np.cumsum(probabilities)

# Zeichnen der Verteilungsfunktion F_X
x_values = range(n + 1)

plt.step(x_values, cumulative_probabilities, where='post', label="Verteilungsfunktion $F_X(x)$", color="red")
plt.scatter(x_values, cumulative_probabilities, color="red")
plt.title("Verteilungsfunktion $F_X(x)$ für 3 Seeleute")
plt.xlabel("$x$")
plt.ylabel("$F_X(x)$")
plt.xticks(range(n + 1))
plt.yticks(np.linspace(0, 1, 5))
plt.grid(True)
plt.show()

# Wahrscheinlichkeiten ausgeben
probabilities, cumulative_probabilities