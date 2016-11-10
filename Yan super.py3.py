 import tkinter
   
def complete():
    n = int(textbox.get())
    for i in range(1, n):
        result = 2**i

    label = tkifill = xnter.Label(root, width = 100, text = result)
    label.pack()
    return label

root = tkinter.Tk()
root.title('Number')
root.minsize(width = 400, height = 400)
root.maxsize(width = 600, height = 600)

textbox = tkinter.Entry(root, width = 100)
value = textbox.get()
print(value)
butComplete = tkinter.Button(root, text = 'Ok', width = 100 command = complete)

textbox.pack(fill = 'x')
butComplete.pack(fill = 'x')
s = v.get()

root.mainloop()

