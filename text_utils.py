
def read_data():
    with open("in.txt", "r") as f:
        res = []
        for i in f.readlines():
            res.append(i.split(","))
        return res



