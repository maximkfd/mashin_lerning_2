
def read_data():
    with open("in.txt", "r") as f:
        res = []
        for i in f.readlines():
            words = i.split(",")
            nums = [int(words[0]), int(words[1]), int(words[2])]
            res.append(nums)
        return res



