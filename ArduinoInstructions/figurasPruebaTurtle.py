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

def prueba1():
    for c in range(100, 0, -10):
        circulo(c)
    dibujo()

def cuadrado(size,ang):
    print(size)
    lista.append([230-size-ang,230-size])
    lista.append([230-size, size+ang])
    lista.append([size+ang, size])
    lista.append([size, 230-size-ang])
    lista.append([230-size-ang,230-size])


def prueba2():
    i = 0
    for c in range(230, 0, -20):
        cuadrado(c,i*20)
        i = i+1
    dibujo()

prueba2()




