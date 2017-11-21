
from data_helper import *


def mean_squared_error(real, predicted):
    return np.sqrt((np.sum((real - predicted) ** 2)) / len(real))


# returns [w0, w1, w2]
def gradient_decent(X, Y, steps, alpha):
    W = np.array([0, 0, 0], dtype=float)
    for step in range(steps):
        Y_predited = np.dot(X, W)
        delta = Y - Y_predited
        W = W + alpha * np.dot(delta, X)

    return W


#   SOME CONSTANTS
alpha = 0.1**9
steps = 2000
free_term_mul = 1

data = get_data()

X, Y = data[..., 0:3], data[..., 3]

#   START
W = gradient_decent(X, Y, steps, alpha)
print("W: ", W)
Y_predicted = np.dot(X, W)
print("mean_squared_error: ", mean_squared_error(Y, Y_predicted))

#   NEW DOTS CALCULATING
while True:
    new_data = input("Enter square and rooms num with space (like: \"2000 3\"): ")
    new_data = new_data.split(' ')

    S = int(new_data[0])
    rooms_num = int(new_data[1])

    new_X = np.array([[free_term_mul, S, rooms_num]])

    print(np.dot(new_X, W)[0])