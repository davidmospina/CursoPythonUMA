import threading
import time

class myThread (threading.Thread):
    def __init__(self, ID, name, counter):
        threading.Thread.__init__(self)
        self.threadID =ID
        self.name = name
        self.counter = counter

    def run(self):
        print("Empiezo" + self.name)

        print_time(self.name, self.counter, 2)

        print("Termino " + self.name)

def print_time(threadName, counter, delay):
    while counter>0:
        time.sleep(delay)
        print (threadName + " " + str(counter) + "\n")
        counter -= 1        

    # Creo nuevos threads
thread1 = myThread(1, "Thread-1", 8)
thread2 = myThread(2, "Thread-2", 8)
# Lanzo nuevas Threads
thread1.start()
thread2.start()


print ("Programa principal")