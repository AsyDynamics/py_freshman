from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('AsyDynamics', 'Doggies can live up to 100 years')
answer = tkinter.messagebox.askquestion('Quiz 1', 'Do u like new emoj')
if answer == 'yes':
	print('XD')
else:
	print('Now way')
	

root.mainloop()