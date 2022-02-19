class complejo:
    __cuantos = 0
    def __init__(self,r,i):
        self.real = float (r)
        self.img = float(i)
        complejo.__cuantos += 1
    def modulo(self):
        return (self.real**2 + self.img**2)**(1/2)
    def conjugado(self):
        return complejo(self.real, -self.img)
    def inc(self, c1):
        self.real += c1.real
        self.img += c1.img
        
    def __str__(self):
        cadena = str(self.real)
        if self.img < 0:
            cadena = cadena + " " + str(self.img)+' i'
        else:
            cadena = cadena+ " " + '+' + " " + str(self.img)+ ' i'
        return cadena
    
    @classmethod
    
    def cuantosHay(cls):
        print("se han definido:" cls._cuantos)
       
def suma(c1, c2):
    return complejo(c1.real+c2.real, c1.img + c2.img)

#prueba de commit en main paralelo la commit de develop



# z = complejo(3,4)
# print(z.modulo())
# z2 = z.conjugado()
# print(z2.modulo())
# print(z)
# print(z2)