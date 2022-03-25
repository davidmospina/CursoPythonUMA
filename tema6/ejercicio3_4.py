import threading
import time
class VariableCompartida:
    def __init__(self):
        self.value = 0
        self.cerrojo = threading.Lock()
    def Actualizar(self, name,cuanto):
        
        print("Thread " + name + ": Empiezo ")
        local_copy = cuanto
        for i in range(local_copy):
            
            self.cerrojo.acquire()
            self.value += 1
            self.cerrojo.release()

        print("Thread "  + name + "Termino", name)

class myThread (threading.Thread):
    def __init__(self, ID, name, MAX, tipo):
        threading.Thread.__init__(self)
        self.threadID =ID
        self.name = name
        self.cuantos = MAX
        self.tipo=tipo  
    
    def run(self):
        compartido.Actualizar(self.name,self.cuantos)


compartido=VariableCompartida()
thread1 = myThread(1, "Thread-1", 200000,"Primero")
thread2 = myThread(2, "Thread-2", 400000,"Segundo")

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Hebra principal:valor final {}".format(compartido.value))