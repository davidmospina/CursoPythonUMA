from numpy import append
from particulaMasa import *
deltat = 0.1
class simulacion:
    def __init__(self,NumParticulas,ptiempoTot):
        self.tiempoTot = ptiempoTot
        self.particulas = list ()
        for i in range(NumParticulas):            
            self.particulas.append(particulaMasa())
            self.particulas[i].set_valores(np.ones(3)*i,np.zeros(3),np.zeros(3),1.493e10)
            self.particulas[i].muestra()
            print("\n")

    def avanza(self):
        for i in range(len(self.particulas)):
            self.particulas[i].aceleracion_cero()
                
        for i in range(len(self.particulas)):
            tempParticulas = self.particulas.copy()
            del tempParticulas[i]
            for j in range(len(tempParticulas)):
                self.particulas[i].aceleracion_gravitatoria(tempParticulas[j])

        for i in range(len(self.particulas)):
            self.particulas[i].actualiza_velocidad_y_posicion(deltat)
        
        for i in range(len(self.particulas)):            
            self.particulas[i].muestra()
            print("\n")

    def simula(self):

        tiempo = 0.0
        while tiempo < self.tiempoTot:
            tiempo = tiempo + deltat
            self.avanza()