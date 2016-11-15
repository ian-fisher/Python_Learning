

countx = 0
count0 = 0
flag = False


def xo(flag, countx, count0):
    if flag == False:
        data.set('X')
        countx += 1
        flag = True
    else:
        data.set('0')
        count0 += 1
    flag = False
        
root = tkinter.Tk()
root.title('X and 0')
root.minsize(width = 800, height = 900)
root.maxsize(width = 800, height = 900)

data = tkinter.StringVar()

but1 = tkinter.Button(root, width = 100, height = 5, textvariable = data, command = xo(flag, countx, count0))
but2 = tkinter.Button(root, width = 100, height = 5, textvariable = data, command = xo(flag, countx, count0))
but3 = tkinter.Button(root, width = 100, height = 5, textvariable = data, command = xo(flag, countx, count0))
but4 = tkinter.Button(root, width = 100, height = 5, textvariable = data, command = xo(flag, countx, count0))
but5 = tkinter.Button(root, width = 100, height = 5, textvariable = data, command = xo(flag, countx, count0))
but6 = tkinter.Button(root, width = 100, height = 5, textvariable = data, command = xo(flag, countx, count0))
but7 = tkinter.Button(root, width = 100, height = 5, textvariable = data, command = xo(flag, countx, count0))
but8 = tkinter.Button(root, width = 100, height = 5, textvariable = data, command = xo(flag, countx, count0))
but9 = tkinter.Button(root, width = 100, height = 5, textvariable = data, command = xo(flag, countx, count0))

but1.pack()
but2.pack()
but3.pack()

but4.pack()
but5.pack()
but6.pack()

but7.pack()
but8.pack()
but9.pack()

root.mainloop()

