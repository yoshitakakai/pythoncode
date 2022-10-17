
# 親クラス
class People():
    def __init__(self, greeting):
        self._greeting = greeting

    def greeting(self):
        if self._greeting == "Hello":
            return "Hi"
        else:
            return "What?"


# 子クラス１
class American(People):
    def greeting(self):
        if self._greeting == "Hello":
            return "Hello"
        else:
            return "Huh?"


# 子クラス２
class Spanish(People):
    def greeting(self):
        if self._greeting == "Hola":
            return "Hola"
        else:
            return "Eh?"


# 子クラス３
class French(People):
    def greeting(self):
        if self._greeting == "Bonjour":
            return "Bonjour"
        else:
            return "Hein?"


# 呼び出し方を統一
def greeting_people(obj):
    return obj.greeting()


# 実行
if __name__ == "__main__":
    american = American("Hello")
    print(greeting_people(american))

    spanish = Spanish("Hola")
    print(greeting_people(spanish))

    french = French("Bonjour")
    print(greeting_people(french))
