from re import X


class punto:
    def __init__ (self,px,py):
        self.x = px
        self.y = py
    def iguales(self,otroPunto):
        resultado = ((self.x == otroPunto.x) & (self.y == otroPunto.y))
        return