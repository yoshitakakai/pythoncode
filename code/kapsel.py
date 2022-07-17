class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n
#indexはリストの0、nは値を示している

data_two = Data()
data_two.change_data(3, 100)
#indexを3に変換、nを100に変換
#nums[3] = 100
print(data_two.nums)

