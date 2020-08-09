class Singleton:
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]


@Singleton
class Cls:
    def __init__(self):
        pass

cls1 = Cls()
cls2 = Cls()
assert id(cls1) == id(cls2)
