import numpy as np

x = np.linspace(0,1,100)

y = np.sin(x)

r = np.fft.fft(y)
print(r)

