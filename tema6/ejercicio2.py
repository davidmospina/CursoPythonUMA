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


    for i in range(counter):
        #time.sleep(1)
        #temp = np.array([])
        
        global temp
        temp = np.append(temp,sense.temperature)



def LecturaSensorP(counter):

    
    for i in range(counter):
        #time.sleep(1)
        #pres = np.array([])

        global pres
        pres = np.append(pres,sense.pressure)

    
 
    

def LecturaSensorH(counter):

    
    for i in range(counter):
        #time.sleep(1)        
        #hum = np.array([])

        global hum
        hum = np.append(hum,sense.humidity)


#temp = np.array([])


sense = SenseHat()

temp = np.array([])
pres = np.array([])
hum = np.array([])

thread0 = myThread(0, "Temp", 200)
thread1 = myThread(1, "Hum", 200)
thread2 = myThread(2, "Pres", 200)

thread0.start()
thread1.start()
thread2.start()


thread0.join()
thread1.join()
thread2.join()

plt.plot(hum,label = 'humedad')
plt.plot(pres,label= 'presion')
plt.plot(temp,label = 'temperatura')
plt.legend()

plt.show()

print("hecho")


