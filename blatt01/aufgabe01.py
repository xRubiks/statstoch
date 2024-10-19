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
    plt.bar(range(n + 1), correct_counts, color='blue')
    plt.xlabel('Anzahl der Seeleute im richtigen Bett')
    plt.ylabel('Häufigkeit')
    plt.title(f'Häufigkeit der korrekten Zuordnungen bei {trials} Versuchen')
    plt.show()

n = 10
trials = 10000
average_correct, correct_counts = seeleute(n, trials)

print(f"Durchschnittlich liegen {average_correct:.2f} von {n} Seeleuten im richtigen Bett.")

# Ergebnisse grafisch darstellen
plot_results(n, correct_counts, trials)