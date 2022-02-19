from complejo import complejo, suma
#tambien podria haber importado todo : from complejo import *

z = complejo(3,4)
print(z.modulo())
z2 = z.conjugado()
print(z2.modulo())
print(z)
print(z2)
z3 = suma(z,z2)
print(z3)

z.inc(z2)
z4 = z 
print (z4)