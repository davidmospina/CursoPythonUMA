from particulaMasa import * 
# p1 = particulaMasa()
# p1.set_valores([0,5,0],[0,0,3],[0,0,0],5)
# print(p1.masa)
# print(p1.pos)
# print(p1.vel)
# print(p1.acc)
# print("\n")
# p1.muestra()
# print("\n")
# p2 = particulaMasa()
# p2.init_random()
# p2.muestra()

p1 = particulaMasa()
p2 = particulaMasa()
deltat = 0.1
p1.set_valores(np.zeros(3), np.zeros(3), np.zeros(3), 1.0e10)
p2.set_valores(np.array([1, 1, 0.]), #posicion
np.array([0,0.5,0.]), #velocidad
np.zeros(3), #aceleración
1.0e5) # masa
p1.muestra()
p2.muestra()
print("\n")
p1.aceleracion_gravitatoria(p2)
p2.aceleracion_gravitatoria(p1)
p1.actualiza_velocidad_y_posicion(deltat)
p2.actualiza_velocidad_y_posicion(deltat)
p1.muestra()
print("\n")
p2.muestra()