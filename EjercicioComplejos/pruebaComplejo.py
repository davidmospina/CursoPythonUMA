from complejo import complejo, suma
#tambien podria haber importado todo : from complejo import *

# z = complejo(3,4)
# print(z.modulo())
# z2 = z.conjugado()
# print(z2.modulo())
# print(z)
# print(z2)
# z3 = suma(z,z2)
# print(z3)

# z.inc(z2)
# z4 = z 
# print (z4)


#prueba numero de definidos
# from complejo import complejo, suma
# zz1 = complejo(4, 1) #se define uno
# zz2 = zz1.conjugado() #se define uno
# otroComplejo = complejo(1, 0) #se define uno
# #zz1.inc(otroComplejo) 
# print(zz1)
# print(suma(zz2, otroComplejo)) #se define uno
# complejo.cuantosHay()

#prueba de ploteo
zz1 = complejo(4, 1)
otroComplejo = complejo(1, 0)
zz1.inc(otroComplejo)
zz1.prepara()
otroComplejo.prepara()
complejo.pinta()
