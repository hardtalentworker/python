import os
import tkinter
#import tkinter.messagebox
import tkinter.filedialog

countDeletedFiles=0

def work(dirSample,dirEdit):
    listForSample=[]
    listForEdit=[]
    listForEditDirpath=[]
    listIndexForDelete=[]

    os.chdir(dirEdit)
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in filenames:
            listForEdit.append(filename)
            listForEditDirpath.append(os.path.join(dirpath, filename))

    for filename in listForEditDirpath:
        print(filename)

    os.chdir(dirSample)
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in filenames:
            listForSample.append(filename)

    i=0
    for memberListForCheck in listForEdit:
        if memberListForCheck in listForSample:
            listIndexForDelete.append(i)
        i+=1

    os.chdir(dirEdit)
    for filename in listIndexForDelete:
        os.remove(listForEditDirpath[filename])

    lblResult.configure(text=("Удалено "+str(len(listIndexForDelete))+" файлов"))

def selectDirSample():
    dirSample=tkinter.filedialog.askdirectory() #поле выбора каталога
    lblSample.configure(text=dirSample)

def selectDirEdit():
    dirEdit=tkinter.filedialog.askdirectory() #поле выбора каталога
    lblEdit.configure(text=dirEdit)

tk=tkinter.Tk()
tk.geometry('380x200')
tk.title("Удалятор дубликатов файлов по имени")

lblSample=tkinter.Label(tk,text="Каталог образца",padx=10,pady=10,font=("Arial Bold",16)) #C:/test/testSample
lblSample.grid(column=0, row=0)
#txtSample=tkinter.Entry(tk,width=50) #поле для ввода
#txtSample.grid(column=0, row=0)
btnSample=tkinter.Button(tk,text="Каталог образца",bg="green",fg="black",width=20,command=lambda: selectDirSample()) #создание кнопки
btnSample.grid(column=1, row=0)
btnSample.focus()
lblEdit=tkinter.Label(tk,text="Каталог копий",padx=10,pady=10,font=("Arial Bold",16)) #C:/test/testEdit
lblEdit.grid(column=0, row=2)
#txtEdit=tkinter.Entry(tk,width=50)
#txtEdit.grid(column=0, row=2)
btnEdit=tkinter.Button(tk,text="Каталог копий",bg="orange",fg="black",width=20,command=lambda: selectDirEdit()) #создание кнопки
btnEdit.grid(column=1, row=2)

btn=tkinter.Button(tk,text="старт",bg="red",fg="black",font=("Arial Bold",20),command=lambda: work(lblSample.cget("text"),lblEdit.cget("text"))) #создание кнопки
btn.grid(column=1, row=4)

lblResult=tkinter.Label(tk,text="Удалено 0 файлов",padx=10,pady=10,font=("Arial Bold",16)) #Каталог копий
lblResult.grid(column=0, row=6)

tk.mainloop()
