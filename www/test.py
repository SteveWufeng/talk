import random as r

class testClass:
    def __init__ (self):
        self.string = "random_string"
    
    def get_rand(self):
        i = r.randint(0,len(self.string))
        return self.string[i]