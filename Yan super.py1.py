import tkinter


def save():
    nameFile = fileBox.get()
    txt = fieldBox.get("1.0",'end-1c')
    if nameFile != '':
        file = open(nameFile, mode = 'w')
        file.write(txt)
        file.close()
        print('Done write!')
    else:
        print('Error! Not Name File!')


root = tkinter.Tk()
root.title('Notepad')
root.minsize(width = 500, height = 500)
root.maxsize(width = 500, height = 10
             00)

fileBox = tkinter.Entry(root, width = 53)
fieldBox = tkinter.Text(root, width = 60,height = 40)
buttonSave = tkinter.Button(root, width = 60,height = 1,text = 'SAVE',command = save)

fileBox.grid()
fieldBox.grid()
buttonSave.grid()

root.mainloop()

