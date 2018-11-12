from tkinter import *

class BuckysButtons:
	def __init__(self, master):
		frame = Frame()
		frame.pack()

		self.printButton = Button(frame, text='print message', command=self.printMessage)
		self.printButton.pack(side=LEFT)

		self.quitButton = Button(frame, text='quit', command=frame.quit)
		self.quitButton.pack(side=LEFT)

	def printMessage(self):
		print('this is print message function')



root = Tk()
b = BuckysButtons(root)
root.mainloop()
