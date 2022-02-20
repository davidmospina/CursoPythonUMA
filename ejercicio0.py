""" message = "hola mundo"
print(message)
print("adios")
nombre=input("introduce tu nombre:") 

print("hola {}".format(nombre))

print(f"hola {nombre}")


n = 5
while n > 0:
    print(n)
    n = n -1 
print  ('Fin!') """

""" 
edad  = input ("dime edad")
dias  = int(edad)*364
print('has vivido{} dias'.format(dias)) """
""" 
for i in [5,4,3,2,1]:
    print (i)
print('fin')

for i in range (5):
    print(i)
print('fin')


for i in range (6,10):
    print(i)
print('fin') """


""" def Funcion_prueba():
    print('dentro de la fucion de prueba')
    print('saliendo de la funcion de prueba')

Funcion_prueba();
print('hola')
 """
import random
randomlist = list(range(-100,100))

print(randomlist)

randSample = random.sample(randomlist, 3)
print(randSample) 

# mport numpy as np # Importamos numpy como el alias np
# g=np.array( [[3,4,-9], [7,4,-5] ,[1,3,9]] )
# print(g)
# b=np.array( [[-9], [-5] ,[9]] )
# print(b)
# c=g*b
# print(c)
# bt=b.T #traspuestas
# print(bt)
# bh=b.conj().T #traspuestas y conjudaga
# print(bh)
# detg=np.linalg.det(g) #calculo del determinante
# print(detg)


# identidad = np.eye(4,4)
# print(identidad)

# identidadT = identidad.T
# print(identidadT)
