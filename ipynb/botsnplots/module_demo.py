""" 

Hello I am a module

"""

print "Executing stuff inside the module"

some_string = "What ???"
arbitrary_number = 123

def add(x, y):
    """ this function is mine """
    return x + y


def mul(x, z):
    """ this function is yours """
    return x * z


def exclaim(s, n=3):
    """ this function does something """
    return s + "!" * n


class MyPair:
    """ I am a class holding a pair of values """
    
    # this is a class attribute, and it's kind of hidden
    __allPairs = []
    
    def __init__(self, x, y):
        """ I am a method """
        
        # init instance attributes
        self.x = x
        self.y = y
        
        # add this object to the list
        self.__allPairs.append(self)     
        
    def __repr__(self):
        """ Display the object """
        return "MyPair(%i, %i)" % (self.x, self.y)
    
    def flip(self):
        """ exchange x and y """
        tmp = self.x
        self.x = self.y
        self.y = tmp
    
    @classmethod
    def getAll(cls):
        return cls.__allPairs[:]



