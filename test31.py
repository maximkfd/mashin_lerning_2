import math

from standrad_utils import standardize, destandardize_value
from text_utils import read_data

Y = 2
X1 = 0
X2 = 1
# init
alpha = 0.0001
eps = 0.000000000001
epochs = 250
data = read_data()
theta = [1, 1, 1]

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
for i in data:
    calculated_cost = f(i[X1], i[X2])
    x_ = i[Y] - calculated_cost
    y_rewinded = destandardize_value(calculated_cost, Y)
    # print(y_rewinded)
    abs_error = destandardize_value(i[Y], Y) - y_rewinded
    err.append(abs_error ** 2)
print()
sm = 0
for i in err:
    sm += i
    # print(i / aver)
print('Errors: ')
print(sm / len(err))
print(math.sqrt(sm / len(err)))
print()
print('coefficients: ', theta)
# while True:
#     s = input("New point")
#     ints = process_input(s, 2)
#     print(destandardize_value(f(standardize_value(ints[0], X1), standardize_value(ints[1], X2)), Y))
