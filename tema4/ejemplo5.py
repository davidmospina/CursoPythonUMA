from tkinter import Tk, Label, RAISED
root = Tk()
labels = [['1', '2', '3'],
['4', '5', '6'],
['7', '8', '9'],
['*', '0', '#']]
label = Label(root, relief= 'flat' ,padx=10,text='numbers')
label.grid(row=0,rowspan=1, column=1, columnspan=3)
for r in range(4):
    for c in range(3):
        # crear label para fila r y columna c
        label = Label(root, relief= 'groove' ,padx=10,text=labels[r][c])
        # colocar label en fila r y columna c
        label.grid(row=r+1,rowspan=1, column=c+1, columnspan=1)

root.mainloop()