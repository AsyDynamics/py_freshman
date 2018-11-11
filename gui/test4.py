from tkinter import *

root = Tk()

#def printName():
def printName(event):
	print('Hello my name is gg')

#button_1 = Button(root, text='print hello', command=printName)
button_1 = Button(root, text='print hello')
button_1.bind('<Button-1>', printName)
button_1.pack()

root.mainloop()
