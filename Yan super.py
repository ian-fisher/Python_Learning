import tkinter
from tkinter import messagebox

def checkttt():
    if(but1['text'] == 'X' and but2['text'] == 'X' and but3['text'] == 'X' or
        but1['text'] == 'X' and but5['text'] == 'X' and but9['text'] == 'X' or
        but1['text'] == 'X' and but4['text'] == 'X' and but7['text'] == 'X' or
        but4['text'] == 'X' and but5['text'] == 'X' and but6['text'] == 'X' or
        but7['text'] == 'X' and but8['text'] == 'X' and but9['text'] == 'X' or
        but3['text'] == 'X' and but5['text'] == 'X' and but7['text'] == 'X' or
        but3['text'] == 'X' and but6['text'] == 'X' and but9['text'] == 'X' or
        but2['text'] == 'X' and but5['text'] == 'X' and but8['text'] == 'X'):
        messagebox.showinfo('Winner', 'Winner: X')
    elif (but1['text'] == '0' and but2['text'] == '0' and but3['text'] == '0' or
        but1['text'] == '0' and but5['text'] == '0' and but9['text'] == '0' or
        but1['text'] == '0' and but4['text'] == '0' and but7['text'] == '0' or
        but4['text'] == '0' and but5['text'] == '0' and but6['text'] == '0' or
        but7['text'] == '0' and but8['text'] == '0' and but9['text'] == '0' or
        but3['text'] == '0' and but5['text'] == '0' and but7['text'] == '0' or
        but3['text'] == '0' and but6['text'] == '0' and but9['text'] == '0' or
        but2['text'] == '0' and but5['text'] == '0' and but8['text'] == '0'):
        messagebox.showinfo('Winner', 'Winner: 0')

def xo(buttons):
    global flag
    if buttons['text'] == '' and flag == True:
        buttons['text'] = 'X'
        flag = False
        checkttt()
    elif buttons['text'] == '' and flag == False:
        buttons['text'] = '0'
        flag = True
        checkttt()
    
root = tkinter.Tk()
root.title('X and 0')
root.minsize(width = 300, height = 300)
root.maxsize(width = 300, height = 300)

buttons = tkinter.StringVar()
flag = True

but1 = tkinter.Button(root, width = 8, height = 4,command = lambda:xo(but1))
but2 = tkinter.Button(root, width = 8, height = 4,command = lambda:xo(but2))
but3 = tkinter.Button(root, width = 8, height = 4,command = lambda:xo(but3))
but4 = tkinter.Button(root, width = 8, height = 4,command = lambda:xo(but4))
but5 = tkinter.Button(root, width = 8, height = 4,command = lambda:xo(but5))
but6 = tkinter.Button(root, width = 8, height = 4,command = lambda:xo(but6))
but7 = tkinter.Button(root, width = 8, height = 4,command = lambda:xo(but7))
but8 = tkinter.Button(root, width = 8, height = 4,command = lambda:xo(but8))
but9 = tkinter.Button(root, width = 8, height = 4,command = lambda:xo(but9))

but1.grid(row = 0,column = 0)
but2.grid(row = 0,column = 1)
but3.grid(row= 0,column = 2)

but4.grid(row = 1,column = 0)
but5.grid(row = 1,column = 1)
but6.grid(row = 1,column = 2)

but7.grid(row = 2,column = 0)
but8.grid(row = 2,column = 1)
but9.grid(row = 2,column = 2)

root.mainloop()


