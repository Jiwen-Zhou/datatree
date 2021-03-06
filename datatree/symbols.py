
class Symbol(object):
    """A symbol is used to represent a string, usually one that is intended to
    be rendered as unquoted.
    """
    def __init__(self, name):
        self.name = name

    def __getattr__(self, name):
        self.__dict__[name] = result = self.__dict__.get(name, self.__class__(name))
        return result
    
    def __str__(self):
        return self.name
    
    def __getitem__(self, name):
        return self.__getattr__(name)
