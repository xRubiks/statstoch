import matplotlib.pyplot as plt

hashTable = {}

for i in range(6):
    hashTable["1" + str(i+1)] = 1/6

def probabilitynk(n, k):
    result = 0
    for i in range(6):
        if hashTable.get(str(n-1) + str(k-(i+1))):
            result += hashTable.get(str(n-1) + str(k-(i+1)))
        else:
            result += 0
    hashTable[str(n) + str(k)] = (1/6) * result

def populateHashTable(n):
    if n == 1:
        return
    for j in range(2, n+1):
        for i in range(j, j * 6 + 1):
            probabilitynk(j, i)

populateHashTable(5)

distributionW_5 = []

#add all values from hashTable with a key that starts with 5 to distributionW_5
for key in hashTable:
    if key.startswith("5"):
        distributionW_5.append(hashTable[key])

#plot the distribution as a bar chart
#x-axis: shift everything by 5
plt.bar(range(5, 5*6+1), distributionW_5)
plt.title("Wahrscheinlichkeitsverteilung von W_5")
plt.savefig("../pics/distributionW_5.png")
plt.show()

#plot the accumulated distribution as a line chart
#extend the lines to the box of the plot

accumulatedDistributionW_5 = [0]
for i in range(1, len(distributionW_5)):
    accumulatedDistributionW_5.append(accumulatedDistributionW_5[i-1] + distributionW_5[i])

plt.step(range(5, 5*6 +1), accumulatedDistributionW_5, where='post', color="blue")
plt.scatter(range(5, 5*6+1), accumulatedDistributionW_5)
plt.xticks(range(5, 5*6 + 1))
plt.title("Verteilungsfunktion von W_5")
plt.savefig("../pics/accumulatedDistributionW_5.png")
plt.show()

