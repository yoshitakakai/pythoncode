class Data:
    def __init__(self):
        self.numbers = [1, 2, 3]

    def numberchange(self, index, n):
        self.numbers[index] = n

datachange = Data()
datachange.numbers[2] = 100
print(datachange.numbers)
