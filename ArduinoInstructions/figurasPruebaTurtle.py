import turtle
from turtle import Turtle, mainloop

def dibujo():
    screen = turtle.getscreen()
    t = turtle.Turtle()
    posX = 0
    posY = 0

    t.goto(250/2,250)
    t.goto(250,0)
    t.goto(0,150)
    t.goto(250,150)
    t.goto(0,0)


    mainloop()



dibujo()