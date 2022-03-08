from EmulatorGUI import GPIO
from matplotlib.pyplot import ginput
from sense_emu import SenseHat
import numpy as np
import time 
from matplotlib import pyplot as plt

# def pulsa(tecla):
# 	end = True

# with kb.Listener(pulsa)def pulsa(tecla):
# 	end = True

# with kb.Listener(pulsa) as escuchador:
# 	escuchador.join() as escuchador:
# 	escuchador.join()



sense = SenseHat()
pres = np.array([])
hum = np.array([])
temp = np.array([])

red = (250,0,0)
blue = (0,0,255)



for i in range(100):
    temp = np.append(temp,sense.temperature)

    hum = np.append(hum,sense.humidity)
    print(hum[i])

    pres = np.append(pres,sense.pressure)  
    
    time.sleep(1)
    pixels = [ red if i<sense.temperature else blue for i in range(64)]
    sense.set_pixels(pixels)
  

plt.plot(hum,label = 'humedad')
plt.show()

