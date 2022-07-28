#線形探索を行う関数を定義

def liner_search(data, value):
    for i in range(len(data)):
        if data[i] == value:
            return i
    return -1

data = ["red", "green", "yellow", "blue", "black", "white"]
print(liner_search(data, "blue"))