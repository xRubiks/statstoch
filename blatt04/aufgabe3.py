import scipy as sp
import numpy as np

K_wi = [10, 8, 10, 16]

print(np.mean(K_wi))
print(np.var(K_wi))
print()

#add to a new array every pair in K_wi
#no repetition but order matters
pairs = []
for i in range(len(K_wi)):
    for j in range(i+1, len(K_wi)):
        pairs.append([K_wi[i], K_wi[j]])
        pairs.append([K_wi[j], K_wi[i]])

#for each pair calculate the mean
means = []
for pair in pairs:
    means.append(np.mean(pair))

for pair in pairs:
    print(np.mean(pair))

print()
print(np.mean(means))
print(np.var(means))

print()

#add to pairs all pairs with the same element

for i in range(len(K_wi)):
    pairs.append([K_wi[i], K_wi[i]])

means = []
for pair in pairs:
    means.append(np.mean(pair))

print(np.mean(means))
print(np.var(means))
print()