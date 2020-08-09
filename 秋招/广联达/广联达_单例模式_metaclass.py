class Singleton(type):
    def __call__(cls, *args, **kw):
        if not hasattr(cls, "_instance"):
            cls._instance = type.__call__(cls, *args, **kw)
        return cls._instance

class Single(metaclass=Singleton):
    pass

    
cls1 = Single()
cls2 = Single()
assert id(cls1) == id(cls2)
