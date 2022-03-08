import tkinter
tempStr=''
tempStr1=''
tempStr2=''
operator=''
widthButton=10
heightButton=2
secondArg=0

def inCalculator(inArgument):
    global secondArg
    global tempStr1
    global tempStr2
    global tempStr
    global operator
    if inArgument=='Plus' or inArgument=='Minus' or inArgument=='Multiply' or inArgument=='Divide':
        secondArg=1
        if inArgument=='Plus':
            inArgument='+'
            operator='+'
        elif inArgument=='Minus':
            inArgument = '-'
            operator = '-'
        elif inArgument=='Multiply':
            inArgument = '*'
            operator = '*'
        elif inArgument=='Divide':
            inArgument = '/'
            operator = '/'
    elif inArgument=='Result':
        secondArg=0
        inArgument=''
        if operator=='+':
            tempStr=str(float(tempStr1)+float(tempStr2))
        elif operator=='-':
            tempStr=str(float(tempStr1)-float(tempStr2))
        elif operator=='*':
            tempStr=str(float(tempStr1)*float(tempStr2))
        elif operator=='/':
            tempStr=str(float(tempStr1)/float(tempStr2))
    elif secondArg==0:
        tempStr1=tempStr1+inArgument
    elif secondArg==1:
        tempStr2=tempStr2+inArgument
    tempStr=tempStr+inArgument
    lbl.configure(text=tempStr)

tk=tkinter.Tk()
tk.geometry('400x400')

lbl=tkinter.Label(tk,text="Привет")
lbl.grid(column=0, row=0)

#btn1=tkinter.Button(tk,text='1',width=widthButton,height=heightButton,command=inCalculator(1))
btn1=tkinter.Button(tk,text='1',width=widthButton,height=heightButton,command=lambda: inCalculator('1'))
btn2=tkinter.Button(tk,text='2',width=widthButton,height=heightButton,command=lambda: inCalculator('2'))
btn3=tkinter.Button(tk,text='3',width=widthButton,height=heightButton,command=lambda: inCalculator('3'))
btn4=tkinter.Button(tk,text='4',width=widthButton,height=heightButton,command=lambda: inCalculator('4'))
btn5=tkinter.Button(tk,text='5',width=widthButton,height=heightButton,command=lambda: inCalculator('5'))
btn6=tkinter.Button(tk,text='6',width=widthButton,height=heightButton,command=lambda: inCalculator('6'))
btn7=tkinter.Button(tk,text='7',width=widthButton,height=heightButton,command=lambda: inCalculator('7'))
btn8=tkinter.Button(tk,text='8',width=widthButton,height=heightButton,command=lambda: inCalculator('8'))
btn9=tkinter.Button(tk,text='9',width=widthButton,height=heightButton,command=lambda: inCalculator('9'))
btnPlus=tkinter.Button(tk,text='+',width=widthButton,height=heightButton,command=lambda: inCalculator('Plus'))
btnMinus=tkinter.Button(tk,text='-',width=widthButton,height=heightButton,command=lambda: inCalculator('Minus'))
btnMultiply=tkinter.Button(tk,text='*',width=widthButton,height=heightButton,command=lambda: inCalculator('Multiply'))
btnDivide=tkinter.Button(tk,text='/',width=widthButton,height=heightButton,command=lambda: inCalculator('Divide'))
btnResult=tkinter.Button(tk,text='=',width=widthButton,height=heightButton,command=lambda: inCalculator('Result'))
btn1.grid(column=0, row=1)
btn2.grid(column=1, row=1)
btn3.grid(column=2, row=1)
btn4.grid(column=0, row=2)
btn5.grid(column=1, row=2)
btn6.grid(column=2, row=2)
btn7.grid(column=0, row=3)
btn8.grid(column=1, row=3)
btn9.grid(column=2, row=3)
btnPlus.grid(column=3, row=1)
btnMinus.grid(column=3, row=2)
btnMultiply.grid(column=3, row=3)
btnDivide.grid(column=3, row=4)
btnResult.grid(column=3, row=5)

tk.mainloop()
