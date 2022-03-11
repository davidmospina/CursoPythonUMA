import csv
from matplotlib import pyplot as plt
import numpy as np
from sense_emu import SenseHat
import time 

sense = SenseHat()
pres = np.array([])
hum = np.array([])
temp = np.array([])

red = (250,0,0)
blue = (0,0,255)

file = open('senseHatResgister.csv','a',newline='')

fieldNames = ['press','temp','hum']

writer = csv.DictWriter(file, dialect='excel', fieldnames= fieldNames)

writer.writeheader()

for i in range(20):
    writer.writerow({'press': sense.pressure, 'temp':sense.temperature, 'hum': sense.humidity})
    pixels = [ red if i<sense.temperature else blue for i in range(64)]
    sense.set_pixels(pixels)
    time.sleep(1)


