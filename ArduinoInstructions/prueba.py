from pymata4 import pymata4
import time

steps = 250
pinsAbajo = [8, 9, 10, 11]
pinsArriba = [2, 3, 5, 6]
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
    board.servo_write(12, (i * 90))
    time.sleep(0.5)


def cuadrado(a):
    color(a)
    moverX(steps)
    moverY(steps)
    moverX(-steps)
    moverY(-steps)
    color(1)


def inicial():
    color(1)
    moverX(-steps)
    moverY(-steps)
    print("Inicio")


def final():
    color(1)
    moverX(steps)
    moverY(steps)
    print("Final")


def main():
    inicial()
    for i in range(0, 250, 10):
        moverX(i)
        # color(0)
        moverY(steps)
        # color(1)
        moverY(-steps)


inicial()
cuadrado(0)
print("Lista 1")
time.sleep(2)
cuadrado(2)
print("Lista 2")
time.sleep(2)
cuadrado(2)
print("Lista 3")
time.sleep(2)
final()
