import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 2, 100)
plt.plot(x,x,label = 'lineal')
plt.plot(x,x**2,label = 'cuadrado')
plt.plot(x,x**3,label = 'cubo')


plt.xlabel('x')
plt.ylabel('y')

plt.title ("ejercicio 13")
plt.legend()

plt.show()


