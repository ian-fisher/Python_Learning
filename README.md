import tkinter

root = tkinter.Tk()

root.title('дверной лабиринт')

root.minsize(width = 570, height = 500)

root.maxsize(width = 570, height = 500)

Button1 = tkinter.Button(root, width = 30, height = 50, text = 'налево')

Button2 = tkinter.Button(root, width = 30, height = 50, text = 'направо')

Button3 = tkinter.Button(root, width = 30, height = 50, text = 'вернутся')

Button1.grid(row = 2,column = 0)

Button2.grid(row = 2,column = 1)

Button3.grid(row = 2,column = 2)

root.mainloop()
