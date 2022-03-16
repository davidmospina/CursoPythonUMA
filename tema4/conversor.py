import tkinter as tk

ventana = tk.Tk()
labelCantidad = tk.Label(ventana, text= "Cantidad:")
labelCantidad.grid(row=0, column=0)

cantidad=tk.StringVar()
entryCantidad=tk.Entry(ventana, width=10, textvariable=cantidad)
entryCantidad.grid(column=1, row=0)
ventana.mainloop()

