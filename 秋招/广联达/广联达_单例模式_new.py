class Single(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self):
        pass

    
cls1 = Single()
cls2 = Single()
assert id(cls1) == id(cls2)
