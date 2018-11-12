from tkinter import *

root = Tk()

def left_click(event):
	print('Left')

def right_click(event):
	print('right')

def middle_click(event):
	print('middle')

frame = Frame(root, width=640, height=480)
frame.bind('<Button-1>', left_click)
frame.bind('<Button-2>', middle_click)
frame.bind('<Button-3>', right_click)
frame.pack()

root.mainloop()
