import tkinter
   
def complete():
    if textbox.get() == '':
        var.set('Field to empty')
    elif len(textbox.get()) >= 2:
        var.set('Too many symbvols')
    else:
        n = int(textbox.get())
        result = [int(textpack.get())**i for i in range(1, n+1)]
        var.set(result)


root = tkinter.Tk()
root.title('Number')
root.minsize(width = 400, height = 400)
root.maxsize(width = 600, height = 600)

var = tkinter.StringVar()

textpack = tkinter.Entry(root, width = 50)
textbox = tkinter.Entry(root, width = 100)
butComplete = tkinter.Button(root, text = 'Ok', width = 100, command = complete)
label = tkinter.Label(root, width = 100, textvariable = var)

textpack.pack(fill= 'x')
textbox.pack(fill = 'x')
butComplete.pack(fill = 'x')
label.pack(fill='x')

root.mainloop()
