import tkinter as tk
from tkinter.messagebox import showinfo

class Aplication:
    def __init__(self):
        self.ventana=tk.Tk()
        self.valor = 0
        self.label=tk.Label(self.ventana, text = self.valor)
        self.boton1=tk.Button(self.ventana, text = "+1", command=self.incrementar)
        self.boton2=tk.Button(self.ventana, text = "-11", command=self.decrementar)
        self.label.pack()
        self.boton1.pack()
        self.boton2.pack()
        self.ventana.mainloop()
        
        
    def incrementar(self):
        self.valor += 1
        self.label.configure(text=self.valor)
        self.selectColor()

    def decrementar(self):
        self.valor -= 1
        self.label.configure(text=self.valor)
        self.selectColor()
    

    def selectColor(self):
        if self.valor < 0:
            self.label.configure(foreground = 'red')
        elif self.valor > 0:
            self.label.configure(foreground = 'green')
        else:
            self.label.configure(foreground = 'blue')

Aplication1 = Aplication()

