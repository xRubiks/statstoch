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

print(hashTable)
populateHashTable(5)
print(hashTable)


