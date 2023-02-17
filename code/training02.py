from matplotlib import pyplot

ranking = [('TOYOTA', 32),
           ('HONDA', 12),
           ('MAZDA', 6),
           ('NISSAN', 20),
           ('DAIHATSU', 18),
  1         ('MITSUBISHI', 12)]

rates = [x[1] for x in ranking]
labels = [x[0] for x in ranking]
pyplot.pie(rates, labels=labels)

pyplot.show()
