class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n

data_two = Data()
data_two.change_data(0, 500)
print(data_two.nums)

