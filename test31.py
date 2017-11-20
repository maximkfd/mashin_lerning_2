import math

from text_utils import read_data, process_input

Y = 2
X1 = 0
X2 = 1
mu = []
sigma = []
# init
alpha = 0.0001
eps = 0.000000000001
epochs = 250
data = read_data()
theta = [1, 1, 1]

y_max = 1
x1_max = 1
x2_max = 1


def f(x1, x2):
    return theta[0] + theta[1] * x1 + theta[2] * x2


def normalize(X):
    # normilize X table
    global y_max, x1_max, x2_max
    for i in data:
        if i[Y] > y_max:
            y_max = i[Y]
    for i in range(len(data)):
        data[i][Y] /= y_max
    for i in data:
        if i[X1] > x1_max:
            x1_max = i[X1]
    for i in range(len(data)):
        data[i][X1] /= x1_max
    for i in data:
        if i[X2] > x2_max:
            x2_max = i[X2]
    for i in range(len(data)):
        data[i][X2] /= x2_max

    return X


def deriv_loss(theta_index):
    sum = 0
    for data_row in data:
        if theta_index == 0:
            sum += (data_row[Y] - f(data_row[X1], data_row[X2]))
        elif theta_index == 1:
            sum += (data_row[Y] - f(data_row[X1], data_row[X2])) * data_row[X1]
        elif theta_index == 2:
            sum += (data_row[Y] - f(data_row[X1], data_row[X2])) * data_row[X2]
    sum *= 2 / len(data)
    return sum


# def normaleaze(data):
#     mul = [1000, 1, 100000]
#     for i in range(3):
#         for j in range(len(data)):
#             data[j][i] /= mul[i]
#     return data

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


# data = normaleaze(data)
# for i in range(epochs):
data = standardize(data)
delta_min = 100
while abs(delta_min) > eps:
    # for i in range(100):
    for j in range(len(theta)):
        delta = alpha * deriv_loss(j)
        theta[j] += delta
        delta_min = min(abs(delta), delta_min)

aver = 0
err = []
abs_err = []
for i in data:
    calculated_cost = f(i[X1], i[X2])
    x_ = i[Y] - calculated_cost
    y_rewinded = calculated_cost * sigma[Y] + mu[Y]
    print(y_rewinded)
    abs_error = destandardize_value(i[Y], Y) - destandardize_value(calculated_cost, Y)
    abs_err.append(abs_error)
    err.append(abs_error ** 2)
    aver += destandardize_value(i[Y], Y)
print()
aver /= len(data)
sm = 0
for i in err:
    sm += i
    print(i / aver)
print()
print(sm / len(err))
print(math.sqrt(sm / len(err)))
print()
print(aver)
print(theta)
# theta[0] *= y_max
# theta[1] *= x1_max
# theta[2] *= x2_max
print(theta)
while True:
    s = input("New point")
    ints = process_input(s, 2)
    print(destandardize_value(f(standardize_value(ints[0], X1), standardize_value(ints[1], X2)), Y))
