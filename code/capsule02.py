class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"
    #操作可能
    def public_method(self):
        pass
    #触ってはいけない
    def _unsefe_method(self):
        pass