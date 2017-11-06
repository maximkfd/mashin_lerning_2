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


def deriv_loss():
    sum = 0
    for i in data:
        sum += abs(data[Y] - f(data[X1], data[X2]))
    sum *= 2


for i in range(epochs):
    for j in range(len(theta)):
        j = j - alpha * deriv_loss()
