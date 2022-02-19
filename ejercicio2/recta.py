import imp
from re import M
from punto import punto
class recta:
    def __init__ (self,p1,p2):
        self.m = ((p2.y - p1.y)/(p2.x - p1.x))
        self.b = p1.y - self.m * p1.x
    
    def x(self, y):
        return (y -self.b)/self.m  

    def y(self, x):
        return self.m*x + self.b

    