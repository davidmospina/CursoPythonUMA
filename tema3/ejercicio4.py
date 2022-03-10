import csv
import grp
from matplotlib import pyplot as plt
import numpy as np

#METODO CON CSV.

""" file = open('aceleraciones.csv')

Objeto_csv = csv.reader(file, dialect='excel')

next(Objeto_csv)


x = []
y = []
z = []

for row in Objeto_csv:
    x.append(int(row[0]))
    y.append(int(row[1]))
    z.append(int(row[2]))

lines = list(range(len(x))) """

#Otra forma de hacerlo
""" with open('aceleraciones.csv') as csvfile:
    Objeto_csv = csv.reader(csvfile, dialect='excel')
    next(Objeto_csv)
    
    x = []
    y = []
    z = []
      
    
    for row in Objeto_csv:
        x.append(int(row[0]))
        y.append(int(row[1]))
        z.append(int(row[2]))

lines = list(range(len(x)))

fig, graph = plt.subplots() 
graph.plot(lines,x,label = 'vibracion X')
graph.plot(lines,y,label = 'vibracion Y')
graph.plot(lines,z,label = 'vibracion Z')
plt.legend()
plt.show() 
"""

#METODO CON USO DE DICTREADER

""" 
x=[]
y=[]
z=[]

with open ('aceleraciones.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        x.append(int(row['X']))
        y.append(int(row['Y']))
        z.append(int(row['Z']))

lines = list(range(len(x)))

fig, graph = plt.subplots() 
graph.plot(lines,x,label = 'vibracion X')
graph.plot(lines,y,label = 'vibracion Y')
graph.plot(lines,z,label = 'vibracion Z')
plt.legend()
plt.show()  
"""

#METODO CON NUMPY

""" contentCsv = np.genfromtxt('aceleraciones.csv', dtype= float, delimiter= ',',skip_header=1)

x=[]
y=[]
z=[]

for row in contentCsv:
        x.append(int(row[0]))
        y.append(int(row[1]))
        z.append(int(row[2]))

lines = list(range(len(x)))

fig, graph = plt.subplots() 
graph.plot(lines,x,label = 'vibracion X')
graph.plot(lines,y,label = 'vibracion Y')
graph.plot(lines,z,label = 'vibracion Z')
plt.legend()
plt.show() """