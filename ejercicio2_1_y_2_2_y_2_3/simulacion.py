from numpy import append
from particulaMasa import *
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

deltat = 0.1
class simulacion:
    def __init__(self,pNumParticulas,ptiempoTot):
        self.tiempoTot = ptiempoTot
        self.particulas = list ()
        self.NumParticulas = pNumParticulas
        for i in range(self.NumParticulas):            
            self.particulas.append(particulaMasa())
        #     self.particulas[i].set_valores(np.ones(3)*i,np.ones(3)*i,np.ones(3)*i,1.493e10)
        #     self.particulas[i].muestra()
        #     print("\n")
        self.particulas[0].set_valores(np.zeros(3), np.zeros(3),np.zeros(3),1.0e10)
        self.particulas[1].set_valores(np.array([1.0,1.0,0.0]),np.array([0.0,0.5,0.0]),np.zeros(3),1.0e5)
        self.particulas[2].set_valores(np.array([1.2,0.25,0.0]),np.array([0.0,0.5,0.0]),np.zeros(3),1.0e5)
        
        self.prepara_grafico()
    def avanza(self):
        for i in range(len(self.particulas)):
            self.particulas[i].aceleracion_cero()
                
        for i in range(len(self.particulas)):
            # tempParticulas = self.particulas.copy()
            # del tempParticulas[i]
            for j in range(len(self.particulas)):
                if i != j:
                    self.particulas[i].aceleracion_gravitatoria(self.particulas[j])

        for i in range(len(self.particulas)):
            self.particulas[i].actualiza_velocidad_y_posicion(deltat)
        
        for i in range(len(self.particulas)):            
            self.particulas[i].muestra()
            print("\n")

        self.refresca_particulas()

    def prepara_grafico(self):
        plt.ion()
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111,projection='3d')
        self.ax.set_xlim(-2.5,2.5)
        self.ax.set_ylim(-2.5,2.5)
        self.ax.set_zlim(-2.5,2.5)
        self.grafico = self.ax.scatter([],[],[],c='r',marker='o')
        plt.draw() 

    def refresca_particulas(self):
        self.grafico.remove()
        #Limpia el grafico para mostrar las posiciones nuevas
        col=['g'] # La primera verde y el resto rojas
        for _ in range (1,self.NumParticulas):
            col.append('r')
        x,y,z = self.vectoriza()

        self.grafico = self.ax.scatter(x,y,z,c=col,marker='o')
        plt.draw()

        plt.pause(0.02)

    def vectoriza(self):
        x=[]
        y=[]
        z=[]
        for i in range(0,self.NumParticulas):
            x.append(self.particulas[i].pos[0])
            y.append(self.particulas[i].pos[1])
            z.append(self.particulas[i].pos[2])
        return x,y,z

    

    def simula(self):

        tiempo = 0.0
        while tiempo < self.tiempoTot:
            tiempo = tiempo + deltat
            self.avanza()