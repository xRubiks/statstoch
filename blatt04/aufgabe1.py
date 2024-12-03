data = [16, 10, 6.5, 7, 3, 6, 7, 5, 5.5, 4, 7]

#calculate arithmetic mean
def arithmeticMean(dataAsList):
    aMean = 0
    for i in dataAsList:
        aMean = aMean + i
    return aMean/len(dataAsList)

#calculate geometric mean
def geometricMean(dataAsList):
    gMean = 1
    for i in dataAsList:
        gMean *= i
    return gMean ** (1/len(dataAsList))

#calculate harmonic mean
def harmonicMean(dataAsList):
    hMean = 0
    for i in dataAsList:
        hMean += 1/i
    return len(dataAsList) / hMean



print(arithmeticMean(data))
print(geometricMean(data))
print(harmonicMean(data))