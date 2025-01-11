import math

import matplotlib.pyplot as plt

#stores the probabilities of the points with n dice
dice_points = {}
epsilonTilde = []
epsilonPlain = []
epsilonStd = []

#probability of 1 dice with k points
for i in range(6):
    dice_points[(1, i + 1)] = 1 / 6

#probability of n dice with k points
def probabilitynk(n, k):
    result = 0
    for i in range(6):
        if dice_points.get((n - 1, k - (i + 1))):
            result += dice_points.get((n - 1, k - (i + 1)))
        else:
            result += 0
    dice_points[(n, k)] = (1 / 6) * result

#populate the hashTable with all points with 1-n dice
def populateHashTable(n):
    if n == 1:
        return
    for j in range(2, n+1):
        for i in range(j, j * 6 + 1):
            probabilitynk(j, i)

populateHashTable(40)

distributionW_5 = []

#add all values from hashTable with a key that starts with 5 to distributionW_5
for key in dice_points:
    if key[0] == 5:
        distributionW_5.append(dice_points[key])

#plot the distribution as a bar chart
#x-axis: shift everything by 5
plt.bar(range(5, 5*6+1), distributionW_5)
plt.title("Wahrscheinlichkeitsverteilung von W_5")
plt.savefig("../pics/B5T1a1.png")
plt.close()

#plot the accumulated distribution as a line chart
accumulatedDistributionW_5 = [0]
for i in range(1, len(distributionW_5)):
    accumulatedDistributionW_5.append(accumulatedDistributionW_5[i-1] + distributionW_5[i])

plt.step(range(5, 5*6 +1), accumulatedDistributionW_5, where='post', color="blue")
plt.scatter(range(5, 5*6+1), accumulatedDistributionW_5)
plt.xticks(range(5, 5*6 + 1))
plt.title("Verteilungsfunktion von W_5")
plt.savefig("../pics/B5T1a2.png")
plt.close()

k_max = []
for i in range(2,41):
    distribution = {}
    accumulatedDistribution = {}
    k_star = 0
    for key in dice_points:
        if key[0] == i:
            distribution[key[1]] = dice_points[key]

    accumulatedDistribution_pre = 0
    for key in distribution:
        accumulatedDistribution[key] = accumulatedDistribution_pre + distribution[key]
        accumulatedDistribution_pre = accumulatedDistribution[key]
    for key in accumulatedDistribution:
        if accumulatedDistribution[key] <= 0.05:
            k_star = key
    k_max.append(k_star)

n=2
for k_star in k_max:
    epsilonTilde.append(3.5 - (k_star/n))
    epsilonPlain.append((math.sqrt((35/12)/(n * (1/10)))))
    epsilonStd.append(1.64 * math.sqrt((35 / 12) / n))
    n+=1
    # print("k* für n = " + str(k_max.index(k_star) + 2) + ": " + str(k_star))
    # print("epsilonTilde für n = " + str(k_max.index(k_star) + 2) + ": " + str(epsilonTilde[k_max.index(k_star)]))
    # print("epsilonPlain für n = " + str(k_max.index(k_star) + 2) + ": " + str(epsilonPlain[k_max.index(k_star)]))

plt.scatter(range(2, 41), epsilonTilde, color="blue", label="epsilonTilde")
plt.scatter(range(2, 41), epsilonPlain, color="red", label="epsilon")
plt.scatter(range(2, 41), epsilonStd, color="green", label="epsilonStd")
plt.legend()
plt.title("epsilonTilde und epsilon")
plt.savefig("../pics/B5T1b.png")
plt.close()