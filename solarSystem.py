import tkinter
import math
import time

sunSize=60
mercurySize=8
mercuryOrbit=78
mercuryYear=4.1493
venusSize=19
venusOrbit=144
venusYear=1.6260
earthSize=20
earthOrbit=200
earthYear=1.0
marsSize=11
marsOrbit=304
marsYear=0.5316

class SpaceObject:
    def __init__(self,canvas):
        self.canvas=canvas
    def draw(self,type,size):
        pass

class Planets:
    def __init__(self,canvas,name,size,orbit,year,color):
        self.canvas=canvas
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.orbit=orbit
        self.year = year
        self.x=xCenterScreen-orbit
        self.y=yCenterScreen
        self.i=1.0
        self.id=canvas.create_oval(self.x, self.y-size/2, self.x+size, self.y+size/2, fill=color)
    def draw(self):
        angle = self.i * 3.14 / 180
        self.x = self.orbit * math.cos(angle) + xCenterScreen
        self.y = self.orbit * math.sin(angle) + yCenterScreen
        self.canvas.moveto(self.id, self.x, self.y)
        if self.i>=360:
            self.i=0.0
        else:
            self.i = self.i + (1*self.year)/3

class Star:
    def __init__(self,canvas,name,size,color):
        self.canvas=canvas
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.id=canvas.create_oval(self.canvas_width/2-size/2, self.canvas_height/2-size/2, self.canvas_width/2+size/2, self.canvas_height/2+size/2, fill=color)
    def draw(self):
        pass

tk=tkinter.Tk()
tk.title('Солнечная система')
tk.resizable(0,0)
#tk.wm_attributes("-topmost",1)
canvas=tkinter.Canvas(tk,width=700,height=700,bd=0,highlightthickness=0)
canvas.pack()
tk.update()
yCenterScreen=canvas.winfo_height()/2
xCenterScreen=canvas.winfo_width()/2

sol=Star(canvas,'Солнце',sunSize,'yellow')
mercury=Planets(canvas,'Меркурий',mercurySize,mercuryOrbit,mercuryYear,'gray')
venus=Planets(canvas,'Венера',venusSize,venusOrbit,venusYear,'orange')
earth=Planets(canvas,'Земля',earthSize,earthOrbit,earthYear,'blue')
mars=Planets(canvas,'Марс',marsSize,marsOrbit,marsYear,'red')
while True:
    sol.draw()
    mercury.draw()
    venus.draw()
    earth.draw()
    mars.draw()

    time.sleep(0.01)
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
