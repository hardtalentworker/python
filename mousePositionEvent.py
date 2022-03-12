import tkinter

def mouse_motion(event):
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    text = "Позиция курсора: ({}, {})".format(x, y)
    lbl.config(text=text)

app = tkinter.Tk()
app.title("Базовый canvas")
canvas = tkinter.Canvas(app, bg="white")
lbl = tkinter.Label(app)
canvas.bind("<Button-1>", lambda event: mouse_motion(event))

canvas.pack()
lbl.pack()

app.mainloop()
