import numpy as np


def read_data():
    with open("in.txt", "r") as f:
        res = []
        for i in f.readlines():
            res.append(process_input(i))
        return res


def process_input(input, k=3):
    words = input.split(",")
    nums = []
    for i in range(k):
        nums.append(int(words[i]))
    return nums


def process_input_np(input, k=3):
    words = input.split(",")
    nums = [1.0]
    for i in range(k):
        nums.append(int(words[i]))
    return nums


def read_data_np():
    with open("in.txt", "r") as f:
        res = []
        for i in f.readlines():
            res.append(process_input_np(i))
        np_res = np.array(res)
        return np_res
