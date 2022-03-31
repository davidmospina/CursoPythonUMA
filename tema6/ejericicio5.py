from numpy import random
import threading
# import time
from pynput import keyboard
# import sys


# def on_press(key):
#     if key.char == ('e'):
#         sys.exit()
#     pass

class player(threading.Thread):
    __cerrojo = threading.Lock()
    def __init__ (self, pID):
        threading.Thread.__init__(self)
        self.numero = 0
        self.ID = pID
        

    def run(self):
        while True:
            self.numero = random.randint(1,100)
        
            player.__cerrojo.acquire()
            print("P" + str(self.ID) + ": " + str(self.numero))
            player.__cerrojo.release()

            allNumberChoseen.wait()
            endGame.wait()


class Director(threading.Thread):
    def __init__(self, p0, p1, p2):
        threading.Thread.__init__(self)
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
            
    def elegirGanador(self):
        if self.p0.numero > self.p1.numero and self.p0.numero > self.p2.numero:
            print("Gana el P" + str(self.p0.ID))
        elif self.p1.numero > self.p0.numero and self.p1.numero > self.p2.numero:
            print("Gana el P" + str(self.p1.ID))
        elif self.p2.numero > self.p0.numero and self.p2.numero > self.p1.numero:
            print("Gana el P" + str(self.p2.ID))
        
        print()
        

    def run(self):
        while True:
            allNumberChoseen.wait()
            self.elegirGanador()
            endGame.wait()
            



allNumberChoseen = threading.Barrier(4, timeout = 5)
endGame= threading.Barrier(4, timeout = 5)

# listener = keyboard.Listener(on_press=on_press)
# listener.start()  # start to listen on a separate thread

p1 = player(0)
p2 = player(1)
p3 = player(2)
Director1 = Director(p1, p2, p3)

p1.start()
p2.start()
p3.start()
Director1.start()
