задание на етот раз такое:
import tkinter

def plus():
    lb = tkinter.Label(root, width = 400, height = 400, text = 'Hello World')
    lb.pack()
    return lb

def plus2():
    print('Hello world')
    
root = tkinter.Tk()
root.title('Game PRO')
root.minsize(width = 400, height = 400)
root.maxsize(width = 400, height = 400)

but = tkinter.Button(root, text = 'Hello World', command = plus)
but2 = tkinter.Button(root, text = 'Hello World', command = plus2)
but2.pack(fill = 'x')
but.pack(fill = 'y')

root.mainloop()
