import tkinter as tk

class Conversor:
    def __init__(self):
            
        self.ventana = tk.Tk()

        #Campor de cantidad a covertir
        self.labelCantidad = tk.Label(self.ventana, text= "Cantidad:")
        self.labelCantidad.grid(row=0, column=0)

        self.cantidad=tk.StringVar(value= "0.0")
        self.entryCantidad=tk.Entry(self.ventana, width=10, textvariable=self.cantidad)
        self.entryCantidad.grid(column=1, row=0)

        #Seleccion unidades iniciales
        self.initType=tk.IntVar()
        self.radioKelvin=tk.Radiobutton(self.ventana,text="Kelvin", variable=self.initType, value=0)
        self.radioKelvin.grid(column=0, row=1)
        self.radioCelcius=tk.Radiobutton(self.ventana,text="Celcius", variable=self.initType, value=1)
        self.radioCelcius.grid(column=1, row=1)
        self.radioFahrenheit=tk.Radiobutton(self.ventana,text="Fahrenheit", variable=self.initType, value=2)
        self.radioFahrenheit.grid(column=2, row=1)

        #Boton de conversion

        self.ConversionButton=tk.Button(self.ventana, text="Convertir a:", command=self.calcularConversion)
        self.ConversionButton.grid(column=1, row=2)

       

        #Seleccion unidades finales
        self.finalType = [tk.BooleanVar(False),tk.BooleanVar(False),tk.BooleanVar(False)]
        self.check3=tk.Checkbutton(self.ventana,text="Kelvin", variable=self.finalType[0], onvalue= True)
        self.check3.grid(column=0, row=3)
        self.check3=tk.Checkbutton(self.ventana,text="Celcius", variable=self.finalType[1], onvalue= True)
        self.check3.grid(column=1, row=3)
        self.check3=tk.Checkbutton(self.ventana,text="Fahrenheit", variable=self.finalType[2], onvalue= True)
        self.check3.grid(column=2, row=3)




    def calcularConversion(self):
        
        self.valorC = 0
        self.valorF = 0
        self.valorK = 0
        nConversiones = 4

        if self.finalType[0].get() == True:
            self.kConversion=tk.Label(self.ventana, text = "Kelvin")
            self.kConversion.grid(column=0, row=nConversiones)
            if self.initType.get() == 1:
                self.valorK = float(self.cantidad.get()) + 273.15
            elif self.initType.get() == 2:
                self.valorK = 5/9*(float(self.cantidad.get()) - 32)+273.15
            
            self.finalKelin=tk.Label(self.ventana, text = self.valorK, foreground= "blue")
            self.finalKelin.grid(column=1, row=nConversiones)
            nConversiones+=1
        
        if self.finalType[1].get() == True:
            self.cConversion=tk.Label(self.ventana, text = "Celcius")
            self.cConversion.grid(column=0, row=nConversiones)
            if self.initType.get() == 0:
                self.valorC = float(self.cantidad.get()) - 273.15
            elif self.initType.get() == 2:
                self.valorC = (float(self.cantidad.get()) -32)/1.8
            self.finalCelcius=tk.Label(self.ventana, text = self.valorC, foreground= "blue")
            self.finalCelcius.grid(column=1, row=nConversiones)
            nConversiones+=1

        if self.finalType[2].get() == True:

            self.fConversion=tk.Label(self.ventana, text = "Fahrenheit")
            self.fConversion.grid(column=0, row=nConversiones)
            
            if self.initType.get() == 1:
                self.valorF = float(self.cantidad.get()) * 1.8 + 32
                print(self.valorF)

            elif self.initType.get() == 0:
                self.valorF = 1.8*(float(self.cantidad.get()) - 273.15) +32  
            self.finalFahrenheit=tk.Label(self.ventana, text = self.valorF, foreground= "blue")
            self.finalFahrenheit.grid(column=1, row=nConversiones)
            nConversiones+=1        


Conversor1 = Conversor()
Conversor1.ventana.mainloop()
