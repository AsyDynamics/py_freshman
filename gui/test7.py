from tkinter import *

def doNothing():
	print('aha!')

def doSomething():
	print('wow!')


root = Tk()

# ********************* menu ***************************
myMenu = Menu(root)
root.config(menu=myMenu)

subMenu = Menu(myMenu)
myMenu.add_cascade(label='file', menu=subMenu)
subMenu.add_command(label='New project', command=doNothing)
subMenu.add_command(label='ah', command=doSomething)
subMenu.add_separator()
subMenu.add_command(label='exit', command=doNothing)

editMenu = Menu(myMenu)
myMenu.add_cascade(label='edit', menu=editMenu)
editMenu.add_command(label='redo', command=doSomething)

# ***************** tool bar **********************
toolbar = Frame(root, bg='blue')
insertButton = Button(toolbar, text='insert Image', command=doNothing)
insertButton.pack(side=LEFT, padx=2, pady=2)
printButton = Button(toolbar, text='print', command=doSomething)
printButton.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# ******************** status bar *********************
status = Label(root, text='preparing to do nothing', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)



root.mainloop()
