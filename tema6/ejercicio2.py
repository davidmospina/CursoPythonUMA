from sense_emu import SenseHat
import numpy as np
import time
from matplotlib import pyplot as plt
import threading


class myThread (threading.Thread):
    def __init__(self, ID, name, counter):
        threading.Thread.__init__(self)
        self.ID =ID
        self.name = name
        self.counter = counter

    def run(self):
        print("Empiezo lectura: " + self.name)

        if self.ID == 0:
            LecturaSensorT(self.counter)

        elif self.ID == 1:
            LecturaSensorH(self.counter)
        
        else:
            LecturaSensorP(self.counter)        

        print("Termino lectura:" + self.name)


def LecturaSensorT(counter):

    temp = np.array([])

    for i in range(counter):
        #time.sleep(1)
        temp = np.append(temp,sense.temperature)

    """     plt.plot(temp,label = 'temperatura')
    plt.legend()
    plt.legend()
    plt.show()
     """

def LecturaSensorP(counter):

    pres = np.array([])

    for i in range(counter):
        #time.sleep(1)
        pres = np.append(pres,sense.pressure)

    """  plt.plot(pres,label = 'presion')
    plt.legend()
    plt.show() """
    

def LecturaSensorH(counter):

    hum = np.array([])

    for i in range(counter):
        #time.sleep(1)        
        hum = np.append(hum,sense.humidity)

    """  plt.plot(hum,label = 'humedad')
    plt.legend()
    plt.show()
     """

sense = SenseHat()

thread0 = myThread(0, "Temp", 8)
thread1 = myThread(1, "Hum", 8)
thread2 = myThread(2, "Pres", 8)

thread0.start()
thread1.start()
thread2.start()

thread0.join()
thread1.join()
thread2.join()

print("hecho")





""" Falla aveces la hebra de TEMP.

Tampoco entiendo mucho porqué debo poner el delay si en el ejericio 3 no lo pongo.

No puedo cerrar la ultima ventana.

los fallos van cambiando:
 main thread is not in main loop
 async handler deleted by the wrong thread
 """
