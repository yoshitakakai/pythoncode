class Dog:
    def __init__(self, name, breed, owner):
        self.owner = owner
        self.name = name
        self.breed = breed

class Person:
    def __init__(self, name):
        self.name = name

mick = Person("Mick Jager")
#Personオブジェクトの引数nameを使う
#mickにPersonを代入
stan = Dog("Stanley", "Bulldog", mick)
#一つの目のオブジェクトの引数(name, breed, owner)を使う
#stanに代入
print(stan.owner.name)
#ownerは一つ目のオブジェクトの引数
#nameは二つ目のオブジェクトの引数
#stanのowner(mick)