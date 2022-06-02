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

def obtenerPosXY(posString):
    posX = posString.split("Pos")[1].split(",")[0].replace("(", "")
    posY = posString.split("Pos")[1].split(",")[1].replace(")", "")
    return [posX,posY]

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
        elif (div[0] == "PosX"):
            traduccion.append("%posicion%"+ div[1] + "%f")
        elif (div[0] == "PosY"):
            traduccion.append("%posicion%f%-"+ div[1])
        elif (div[0] == "Beginning"):
            traduccion.append("%posicion%0%0")
        elif ("Pos" in ins):
            posXY = obtenerPosXY(ins)
            traduccion.append("%posicion%"+posXY[0]+"%-"+posXY[1])
        else:
            traduccion.append("%apagar%0")
instrucciones = ["iniciar", "UseColor 1", "ContinueRight 250", "ContinueUp 50", "ContinueLeft 250", "UseColor 2", "ContinueUp 50","ContinueRight 250", "ContinueUp 50", "ContinueLeft 250", "ContinueUp 50","ContinueRight 250", "ContinueDown 250","ContinueLeft 250","apagar", "apagar"]
instrucciones2 = ["iniciar", "UseColor 2", "ContinueRight 250", "Up", "ContinueLeft 250", "Down", "ContinueRight 250", "Up", "ContinueLeft 250", "apagar", "apagar"]
instrucciones3 = ["iniciar", "PosX 100", "PosY 100", "PosY 50", "PosX 50", "Beginning", "apagar", "apagar"]

instrucciones4 = ["iniciar", "Pos(100,100)", "Beginning","apagar", "apagar"]
instrucciones5=["iniciar", "Down"]

def circulo(r):
    for x in range(230):
        for y in range(230):
            if ((x-115)*(x-115) + (y)*(y) == r*r):
                print("(" + str(x) + "," + str(y) + ")")
                instrucciones5.append("Pos("+ str(x) + "," + str(y) + ")")
    instrucciones5.append("Beginning")

for c in range(100, 0, -10):
    circulo(c)

instrucciones5.append("apagar")
instrucciones5.append("apagar")

send_instruccion(instrucciones5)

print(traduccion)

for i in traduccion:
    print (write_read(i))
"""while True:
    num = input("Enter a number: ") # Taking input from user
    value = write_read(num)
    #print(value) # printing the value"""

