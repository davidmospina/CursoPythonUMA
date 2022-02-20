from particula import particula
import random
p1 = particula()
p1.set_valores([1,1,1],[1,1,1],[1,1,1])
p2 = particula()
p2.init_random()
print(p1.distancia(p2))
p3 = particula()
p3.set_valores([1,1,2],[1,1,1],[1,1,1])
print(p1.distancia(p3))

