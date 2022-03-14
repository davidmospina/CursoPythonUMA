import tkinter as tk
from tkinter.messagebox import showinfo

class Aplication:
    def __init__(self):
        self.ventana=tk.Tk()
        self.label=tk.Label(self.ventana, text = "Hola Mundo")
        self.boton=tk.Button(self.ventana, text = "Pulsame", command=self.saludar)
        self.label=tk.Label(self.ventana, text = "Hola Mundo")
        self.label.pack()
        self.boton.pack()
        self.ventana.mainloop()
        
    def saludar(self):
        showinfo(message = "me has saludado")

Aplication1 = Aplication()
