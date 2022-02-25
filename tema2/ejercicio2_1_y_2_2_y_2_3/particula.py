import numpy as np
import random

class particula:
    __cuantas = 0
    def __init__ (self):
        self.pos = np.array([0.0,0.0,0.0])
        self.vel = np.zeros(3)
        self.acc = np.zeros(3)
        particula.__cuantas += 1

    def set_valores(self, pPos, pVel,pAcc):
        self.pos = pPos
        self.vel = pVel
        self.acc = pAcc
        
    def init_random(self):
        self.pos = np.random.randint(-100,100,3)
        self.vel = np.random.randint(-100,100,3)
        

        
    def distancia(self, otra):
        return ((self.pos[0]-otra.pos[0])**2+(self.pos[1]-otra.pos[1])**2+(self.pos[2]-otra.pos[2])**2)**(1/2)
    
    def muestra(self):
        print("la posicion es: ", self.pos)
        print("la velocidad es: ", self.vel)
        print("la aceleracion es: ",self.acc)

    @classmethod
    
    def cuantasHay(cls):
        print("se han definido: "+ str(cls.__cuantas) + " particulas")
    


    

