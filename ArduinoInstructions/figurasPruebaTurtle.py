import turtle
from turtle import Turtle, mainloop
lista = []
def dibujo():
    screen = turtle.getscreen()
    t = turtle.Turtle()
    t.goto(0,230)
    t.goto(230,230)
    t.goto(230,0)
    t.goto(0,0)
    posX = 0
    posY = 0

    for i in lista:
        t.goto(i[0],i[1])


    mainloop()

def circulo(r):
    for x in range(230):
        for y in range(230):
            if (((x-115)*(x-115)) + ((y)*(y)) == r*r):
                print("(" + str(x) + "," + str(y) + ")")
                lista.append([x,y])
circulo(100)
circulo(90)
circulo(80)
circulo(70)
circulo(60)
circulo(50)
circulo(40)
circulo(30)
circulo(20)
circulo(10)
dibujo()