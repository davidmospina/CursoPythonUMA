class poligono:
    def __init__(self,pa,pb):
        self.a = pa
        self.b = pb

class rectangulo(poligono):
    def area(self):
        return  self.a * self.b

class triangulo(poligono):
    def area(self):
        return (self.a *self.b)/2

class cuadrado(poligono):
    def __init__(self,a):
        super().__init__(a,a)
    
    def area(self):
        return (self.a)**2

