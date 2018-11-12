from tkinter import *

root = Tk()

canvas = Canvas(root, width=600, height=400)
canvas.pack()

blackLine = canvas.create_line(5,5, 500,200)
redLine = canvas.create_line(0,400, 500,200, fill='red')
greenBox = canvas.create_rectangle(50,50, 220, 180, fill='green')

canvas.delete(redLine)
canvas.delete(ALL)


root.mainloop()