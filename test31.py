from text_utils import read_data, process_input

Y = 2
X1 = 0
X2 = 1

# init
alpha = 0.1
eps = 0.00000001
epochs = 250
data = read_data()
theta = [0, 0, 0]

y_max = 0
x1_max = 0
x2_max = 0


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

data = normalize(data)
# for i in range(epochs):
j_ = 100
while abs(j_) > eps:
    for j in range(len(theta)):
        j_ = alpha * deriv_loss(j)
        theta[j] += j_

aver = 0
err = []
abs_err = []
for i in data:
    x_ = i[Y] - f(i[X1], i[X2])
    print(x_ * y_max)
    abs_err.append(x_)
    err.append(x_ ** 2)
    aver += i[Y]
print()
aver /= len(data)
for i in err:
    print(i / aver)
print()
print(aver)
print(theta)
theta[0] *= y_max
theta[1] *= x1_max
theta[2] *= x2_max
print(theta)
while True:
    s = input("New point")
    ints = process_input(s, 2)
    print(f(ints[0], ints[1]))


