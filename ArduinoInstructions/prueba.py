from pymata4 import pymata4
import time

steps = 250
pinsAbajo = [8, 9, 10, 11]
pinsArriba = [2,3,5,6]
board = pymata4.Pymata4()
board.set_pin_mode_servo(12)

board.set_pin_mode_stepper(steps, pinsArriba)

for i in range(2):
    board.stepper_write(100,steps)
    time.sleep(1)
    board.stepper_write(100,-steps)
    time.sleep(1)
    board.servo_write(12,0)
    board.servo_write(12,90)
    board.servo_write(12,180)


board.set_pin_mode_stepper(steps, pinsAbajo)
board.set_pin_mode_servo(12)
for i in range(2):
    board.stepper_write(60,steps)
    time.sleep(1)
    board.stepper_write(60,-steps)
    time.sleep(1)
    for j in range(180):
        board.servo_write(12,j)
        time.sleep(0.1)
