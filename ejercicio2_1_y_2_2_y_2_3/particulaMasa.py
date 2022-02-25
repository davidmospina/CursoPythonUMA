from particula import *
G = 6.67259e-11
class particulaMasa(particula):
    def __init__(self):
        super().__init__()
        self.masa = 0
    def set_valores(self, pPos, pVel, pAcc,pMasa):
        "definimos los parametros de la particula."
        super().set_valores(pPos,pVel,pAcc)
        self.masa = pMasa
        
    def init_random(self):
        "los parametros de la particula se incializan de una manera aleatoria."
        super().init_random()
        self.masa = np.random.randint(0,100)
    
    def muestra(self):
        "impriema los parametros de la particula"
        super().muestra()
        print("la masa de la particula es: ",self.masa)
        
    def aceleracion_gravitatoria(self, otra):
        dx = -otra.pos[0]+ self.pos[0]
        dy = -otra.pos[1]+ self.pos[1]
        dz = -otra.pos[2]+ self.pos[2]
        dv = np.array([dx,dy,dz])
        dt = self.distancia(otra)
        self.acc = -G*self.masa/(dt**3)*dv
        
        return self.acc
    def actualiza_velocidad_y_posicion(self,deltat):

            self.vel = self.vel + self.acc*deltat

            self.pos = self.pos + self.vel*deltat

    # def actualiza_velocidad_y_posicion(self,deltat):
    #     for i in range(3):
    #         self.vel[i] = self.vel[i] + self.acc[i]*deltat
        
    #         self.pos[i] = self.pos[i] + self.vel[i]*deltat
 
    def aceleracion_cero(self):
        self.acc = np.zeros(3)

    