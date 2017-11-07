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
