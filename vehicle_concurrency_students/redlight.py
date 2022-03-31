import threading
from time import sleep

class RedLight(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
        self.activated= False

        self.pos = 0
        

    def activate(self):
        self.activated=True

    def deactivate(self):
        self.pos=0  # number of lights on
        self.activated= False

    def get_activated(self):
        return self.activated

    def get_status(self):
        return self.pos

    def run(self):
        hola = 1
        while True:
            # if self.activated:
                if self.pos <= 5:
                    self.pos +=1
                    
                    sleep(0.2)
                else:
                    self.pos =0
                    sleep(0.2)
            
            
            