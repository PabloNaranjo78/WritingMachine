# Importing Libraries
import serial
import time
arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)
traduccion = []
def write_read(x):
    time.sleep(1)
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(1)
    print(arduino.readline())

def send_instruccion(instrucciones):
    for ins in instrucciones:
        div = ins.split()
        print (div)
        if (div[0] == "ContinueUp"):
            traduccion.append("%mover%0%-" + div[1])
        elif (div[0] == "ContinueDown"):
            traduccion.append("%mover%0%" + div[1])
        elif (div[0] == "ContinueRight"):
            traduccion.append("%mover%" + div[1] + "%0")
        elif (div[0] == "ContinueLeft"):
            traduccion.append("%mover%-" + (div[1]) + "%0")
        elif (div[0] == "UseColor"):
            traduccion.append("%color%" + (div[1]))
        elif (div[0] == "Up"):
            traduccion.append("%color%0")
        elif (div[0] == "Down"):
            traduccion.append("%color%f")
        elif (div[0] == "Pos"):
            traduccion.append("%color%f")
        else:
            traduccion.append("%apagar%0")

instrucciones = ["iniciar", "UseColor 1", "ContinueRight 250", "ContinueUp 50", "ContinueLeft 250", "UseColor 2", "ContinueUp 50","ContinueRight 250", "ContinueUp 50", "ContinueLeft 250", "ContinueUp 50","ContinueRight 250", "ContinueDown 250","ContinueLeft 250","apagar", "apagar"]
instrucciones2 = ["iniciar", "UseColor 2", "ContinueRight 250", "Up", "ContinueLeft 250", "Down", "ContinueRight 250", "Up", "ContinueLeft 250", "apagar", "apagar"]

send_instruccion(instrucciones2)
print(traduccion)

for i in traduccion:
    print (write_read(i))

"""while True:
    num = input("Enter a number: ") # Taking input from user
    value = write_read(num)
    #print(value) # printing the value"""

