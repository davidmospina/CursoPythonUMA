from recta import *

p1 = punto(1.0,1.0)
p2 =punto(2.0,3.0)


if p1.iguales(p2):
    print("no se puede definir recta")
else: 
    r = recta(p1,p2)
    print ("la pendiente es", r.m)
    print("el origen pasa por: ", r.b)

    print("para el valor x = 5 la recta pasa por", r.y(5.0))
    print("para el valor y = 9, la x vale ", r.x(9.0))