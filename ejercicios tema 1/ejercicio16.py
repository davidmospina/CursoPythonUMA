from matplotlib.pyplot import ginput
from sense_emu import SenseHat
import numpy as np
import time 
from pynput import keyboard as kb
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d

def pulsa(tecla):
	end = True

with kb.Listener(pulsa) as escuchador:
	escuchador.join()


sense = SenseHat()
pres = np.array()
hum = np.array()
temp = np.array()
t = np-np.array()


red = (250,0,0)
blue = (0,0,255)

tempL = 20


j= 0
end = False

while end == False:
    temp.append(sense.temperature)

    hum.append(sense.humidity)

    pres.append(sense.pressure)

    plt.plot(t,hum, label = 'humedad')
    plt.show()
    t.append(time.localtime())
    time.sleep(1)
    pixels = [ red if temp[j]>tempL else blue for i in range(64)]
    sense.set_pixel(pixels)
    print(sense.temperature)
    j= j + 1

