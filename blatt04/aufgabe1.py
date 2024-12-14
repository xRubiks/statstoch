import math

data = [16, 10, 6.5, 7, 3, 6, 7, 5, 5.5, 4, 7]

#calculate arithmetic mean
def arithmetic_mean(data_as_list):
    a_mean = 0
    for i in data_as_list:
        a_mean = a_mean + i
    return a_mean/len(data_as_list)

#calculate geometric mean
def geometric_mean(data_as_list):
    g_mean = 1
    for i in data_as_list:
        g_mean *= i
    return g_mean ** (1 / len(data_as_list))

#calculate harmonic mean
def harmonic_mean(data_as_list):
    h_mean = 0
    for i in data_as_list:
        h_mean += 1/i
    return len(data_as_list) / h_mean

#calculate variance
def variance(data_as_list):
    a_mean = arithmetic_mean(data_as_list)
    var = 0
    for i in data_as_list:
        var += (i - a_mean)**2
    return var/len(data_as_list)

#calculate samplevariance
def sample_variance(data_as_list):
    a_mean = arithmetic_mean(data_as_list)
    var = 0
    for i in data_as_list:
        var += (i-a_mean)**2
    return var/len(data_as_list)-1

#calculate median
def median(data_as_list):
    data_as_list.sort()
    if (len(data_as_list) % 2) == 0:
        return (data_as_list[math.floor((len(data_as_list) - 1) / 2)] + data_as_list[math.ceil(((len(data_as_list)) / 2))]) / 2
    else:
        return data_as_list[math.floor((len(data_as_list) + 1) / 2) - 1]

#calculate quartil
def quartil(data_as_list, p):
    data_as_list.sort()
    index = math.floor(len(data_as_list) * p) + 1
    return data_as_list[index]

#calculate xquarter
def x_quarter(data_as_list):
    return quartil(data_as_list, 0.25)

#calculate xthreequarter
def x_three_quarter(data_as_list):
    return quartil(data_as_list, 0.75)

#claculate IQR
def IQR(data_as_list):
    return x_three_quarter(data_as_list) - x_quarter(data_as_list)

#caculate whiskers
def whiskers(data_as_list):
    return "[" + str(x_quarter(data_as_list) - 1.5 * IQR(data_as_list)) + ", " + str(x_three_quarter(data_as_list) + 1.5 * IQR(data_as_list)) +"]"

#calculate values for empirical distributionfunction
def distribution_values(data_as_list):
    distribution = 0
    for i in data_as_list:
        distribution += i/sum(data_as_list)
        print(" " + str(i) + ": " + str(distribution))

#calculate values for lorenz-curve
def lorenz_curve(data_as_list):
    for i in range(1, len(data_as_list) + 1):
        numerator = sum(data_as_list[:i])
        denominator = sum(data_as_list)
        print(" (" + str(i/len(data_as_list)) + ", " + str(numerator/denominator) + ")")
print("distribution values:")
distribution_values(data)


print("\nArithmetic Mean: " + str(arithmetic_mean(data)))
print("Geometric Mean: " + str(geometric_mean(data)))
print("Harmonic Mean: " + str(harmonic_mean(data)))
print("Variance: " + str(variance(data)))
print("Samplevariance: " + str(sample_variance(data)))

print("\nBoxplot values:")
print("Median: " + str(median(data)))
print("x_0.25: " + str(x_quarter(data)))
print("x_0.75: " + str(x_three_quarter(data)))
print("IQR: " + str(IQR(data)))
print("Whiskers: " + whiskers(data))


print("\nLorenz-curve values:")
lorenz_curve(data)


