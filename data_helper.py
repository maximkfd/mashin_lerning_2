import numpy as np


def get_data():
    data = []
    for line in open('in.txt'):
        line = line.split('\n')  # избавляемся от последнего элемента (\n)
        line = line[0]  # ---------------------------------------
        line = line.split(',')
        S = float(line[0])
        rooms_num = float(line[1])
        price = float(line[2])
        free_term_mul = 1  # множитель при свободном члене линейного уравнения
        data.append([free_term_mul, S, rooms_num, price])
    return np.array(data)
