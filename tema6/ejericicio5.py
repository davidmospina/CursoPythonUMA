from sqlite3 import paramstyle
from numpy import random
import threading
import time

class player(threading.Thread):
    def __init__ (self, pID):
        threading.Thread.__init__(self)
        self.numero = 0
        self.ID = pID

    def run(self):
        while True:
            self.numero = random.randint(1,100)
            print("P" + str(self.ID) + ": " + str(self.numero)+ "\n")
            allNumberChoseen.wait()
            endGame.wait()


class Director(threading.Thread):
    def __init__(self, p0, p1, p2):
        threading.Thread.__init__(self)
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
            
    def elegirGanador(self):
        if self.p0.numero > self.p1.numero and self.p0.numero > self.p2.numero:
            print("Gana el " + str(self.p0.ID)+ "\n")
        elif self.p1.numero > self.p0.numero and self.p1.numero > self.p2.numero:
            print("Gana el " + str(self.p1.ID) + "\n")
        elif self.p2.numero > self.p0.numero and self.p2.numero > self.p1.numero:
            print("Gana el " + str(self.p2.ID) + "\n")
        
        print()
        

    def run(self):
        while True:
            allNumberChoseen.wait()
            self.elegirGanador()
            endGame.wait()
            


pausa = 5
allNumberChoseen = threading.Barrier(4, timeout = 5)
endGame= threading.Barrier(4, timeout = 5)

p1 = player(0)
p2 = player(1)
p3 = player(2)
Director1 = Director(p1, p2, p3)

p1.start()
p2.start()
p3.start()
Director1.start()


# fallo el primero no se imprime
""" 
Que es mejor poner el while en cada clase, o un while que llame cada rato las hebras, o eso no es optipo porque para
eso esta start """