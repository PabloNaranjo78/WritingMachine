from pymata4 import pymata4
import time

steps = 250
pinsAbajo = [8, 9, 10, 11]
pinsArriba = [2,3,5,6]
board = pymata4.Pymata4()
board.set_pin_mode_servo(12)

def moverX(st):
    board.set_pin_mode_stepper(steps, pinsArriba)
    board.stepper_write(70, st)
    time.sleep(1)

def moverY(st):
    board.set_pin_mode_stepper(steps, pinsAbajo)
    board.stepper_write(70, st)
    time.sleep(1)

def color(i):
    board.servo_write(12, (i*90))
    time.sleep(0.5)

def cuadrado(a):
    color(a)
    moverX(steps)
    moverY(steps)
    moverX(-steps)
    moverY(-steps)
    color(1)
def inicial():
    moverX(-steps)
    moverY(-steps)
    #color(1)

def main():
    inicial()
    for i in range (0,250,10):
        moverX(i)
        #color(0)
        moverY(steps)
        #color(1)
        moverY(-steps)
#main()

cuadrado(0)
cuadrado(2)
cuadrado(2)