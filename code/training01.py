class CarPersonal:
    def __init__(self, d, m, c):
        self.dealer = d
        self.model = m
        self.color = c

    def carselect(self):
        print("あなたへおすすめの車は\n{}の{}で、色は{}です。".format(self.dealer, self.model, self.color))

data = CarPersonal("HONDA", "N-BOX", "Black")
data.carselect()
