import math

mu = []
sigma = []


def standardize(data):
    global mu, sigma
    mu = []
    for i in range(3):
        summ = 0
        for j in range(len(data)):
            summ += data[j][i]
        mu.append(summ / len(data))
    sigma = []
    for i in range(3):
        summ = 0
        for j in range(len(data)):
            summ += (data[j][i] - mu[i]) ** 2
        sigma.append(math.sqrt(summ / len(data)))
    for i in range(3):
        for j in range(len(data)):
            data[j][i] = (data[j][i] - mu[i]) / sigma[i]
    return data


def destandardize_value(x, index):
    return x * sigma[index] + mu[index]


def standardize_value(x, index):
    return (x - mu[index]) / sigma[index]