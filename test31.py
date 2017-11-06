from text_utils import read_data

Y = 2
X1 = 0
X2 = 1

# init
alpha = 0.1
epochs = 25
data = read_data()
theta = [0, 0, 0]


def f(x1, x2):
    return theta[0] + theta[1] * x1 + theta[2] * x2


def deriv_loss(theta_index):
    sum = 0
    for i in data:
        if theta_index == 0:
            sum += abs(i[Y] - f(i[X1], i[X2]))
        if theta_index == 1:
            sum += abs(i[Y] - f(i[X1], i[X2])) * X1
        if theta_index == 2:
            sum += abs(i[Y] - f(i[X1], i[X2])) * X2
    sum *= 2
    return sum


for i in range(epochs):
    for j in range(len(theta)):
        theta[j] -= alpha * deriv_loss(j)

