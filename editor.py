import tkinter

textTemp=' '

def textCopyAll():
    global textTemp
    textTemp=textarea.get(0.0,tkinter.END)

def textСopy():
    global textTemp
    textTemp=textarea.get(tkinter.SEL_FIRST,tkinter.SEL_LAST)

def textСut():
    global textTemp
    textTemp=textarea.get(tkinter.SEL_FIRST,tkinter.SEL_LAST)
    textTemp=textarea.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)

def textPaste():
    textarea.insert(tkinter.END, textTemp)

def textCapitalize():
    global textTemp
    textTemp=textarea.get(tkinter.SEL_FIRST,tkinter.SEL_LAST)
    textarea.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
    textarea.insert(tkinter.INSERT, textTemp.capitalize())

def textLower():
    global textTemp
    textTemp = textarea.get(tkinter.SEL_FIRST, tkinter.SEL_LAST)
    textarea.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
    textarea.insert(tkinter.INSERT, textTemp.lower())

def textUpper():
    global textTemp
    textTemp = textarea.get(tkinter.SEL_FIRST, tkinter.SEL_LAST)
    textarea.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
    textarea.insert(tkinter.INSERT, textTemp.upper())

def textTitle():
    global textTemp
    textTemp = textarea.get(tkinter.SEL_FIRST, tkinter.SEL_LAST)
    textarea.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
    textarea.insert(tkinter.INSERT, textTemp.title())

def textGetStatus():
    lblSymbols.configure(text='symbols:'+str(len(textarea.get(0.0, tkinter.END))))

app = tkinter.Tk()
textarea=tkinter.Text(master=app)
app.columnconfigure(0, weight=1, minsize=50)
app.rowconfigure(0, weight=1, minsize=50)
textarea.grid(row=0, column=0, sticky="nsew")

frameBottom1=tkinter.Frame(master=app)
frameBottom1.grid(row=1, column=0)

btnCopyAll=tkinter.Button(master=frameBottom1,text="Copy all",command=textCopyAll)
btnCopyAll.grid(row=0, column=0)
btnCopyAll=tkinter.Button(master=frameBottom1,text="Copy",command=textСopy)
btnCopyAll.grid(row=0, column=1)
btnPaste=tkinter.Button(master=frameBottom1,text="Cut",command=textСut)
btnPaste.grid(row=0, column=2)
btnPaste=tkinter.Button(master=frameBottom1,text="Paste",command=textPaste)
btnPaste.grid(row=0, column=3)

btnPaste=tkinter.Button(master=frameBottom1,text="Capitalize",command=textCapitalize)
btnPaste.grid(row=1, column=0)
btnPaste=tkinter.Button(master=frameBottom1,text="Lower",command=textLower)
btnPaste.grid(row=1, column=1)
btnPaste=tkinter.Button(master=frameBottom1,text="Upper",command=textUpper)
btnPaste.grid(row=1, column=2)
btnPaste=tkinter.Button(master=frameBottom1,text="Title",command=textTitle)
btnPaste.grid(row=1, column=3)

frameBottom2=tkinter.Frame(master=app)
frameBottom2.grid(row=2, column=0)

btnPaste=tkinter.Button(master=frameBottom2,text="Get status",command=textGetStatus)
btnPaste.grid(row=0, column=0)
lblSymbols=tkinter.Label(master=frameBottom2,text="symbols: ")
lblSymbols.grid(row=0, column=1)
lblLines=tkinter.Label(master=frameBottom2,text="lines: ")
lblLines.grid(row=0, column=2, sticky="ew")
lblNumLine=tkinter.Label(master=frameBottom2,text="line: ")
lblNumLine.grid(row=0, column=3, sticky="ew")
lblNumSymbol=tkinter.Label(master=frameBottom2,text="symbol: ")
lblNumSymbol.grid(row=0, column=4, sticky="ew")

app.mainloop()