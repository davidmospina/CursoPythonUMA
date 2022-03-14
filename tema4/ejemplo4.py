from tkinter import *
root = Tk()

text = Label(root, font = ('Helvetica', 16, 'bold'), foreground= 'white', background= 'black', pady ='100', text='Universidad de Malaga')
text.pack(side= BOTTOM)

uma1 = PhotoImage(file='img/uma1.png')
umaLabel = Label(root,
borderwidth=3, relief=RIDGE, image=uma1)
umaLabel.pack(side=LEFT, fill= BOTH)
uma3 = PhotoImage(file='img/uma3.png')
uma2Label = Label(root,image=uma3)
uma2Label.pack(side=RIGHT,fill= BOTH, expand=False)
root.mainloop()