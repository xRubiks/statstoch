# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

def seeleute(n, trials):
    total_correct = 0

    for _ in range(trials):
        betten = list(range(n))
        random.shuffle(betten)
        correct = sum(1 for i in range(n) if betten[i] == i)
        total_correct += correct

    return total_correct / trials

n = 10
trials = 1
average_correct = seeleute(n, trials)

print(f"Durchschnittlich liegen {average_correct:.2f} von {n} Seeleuten im richtigen Bett.")


