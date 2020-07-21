def singleton(cls):
    _instances = {}
    def get_instance(*args, **kw):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kw)
        return _instances[cls]
    return get_instance


@singleton
class Cls:
    def __init__(self):
        pass

cls1 = Cls()
cls2 = Cls()
assert id(cls1) == id(cls2)
