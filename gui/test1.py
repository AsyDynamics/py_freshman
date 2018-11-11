from tkinter import *

root = Tk()
#theLabel = Label(root, text='Main, this is too easy')
#theLabel.pack()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text='Kiss me', fg='red')
button2 = Button(topFrame, text='Click me', fg='blue')
button3 = Button(topFrame, text='Sleep me', fg='green')
button4 = Button(bottomFrame, text='Wow me', fg='purple')

button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=LEFT)
button4.pack()

root.mainloop()
