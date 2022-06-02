import serial
import time


class ArduinoInstructions:

    def __init__(self,port):
        self.traduccion = ["%apagar%0"]
        self.arduino = serial.Serial(port=port, baudrate=115200, timeout=.1)
        self.instrucciones = []

    def obtenerPosXY(self, posString):
        posX = posString.split("Pos")[1].split(",")[0].replace("(", "")
        posY = posString.split("Pos")[1].split(",")[1].replace(")", "")
        return [posX, posY]

    def sendInstruccion(self, instrucciones):
        self.instrucciones = instrucciones
        for ins in self.instrucciones:
            div = ins.split()
            print(div)
            if (div[0] == "ContinueUp"):
                self.traduccion.append("%mover%0%-" + div[1])
            elif (div[0] == "ContinueDown"):
                self.traduccion.append("%mover%0%" + div[1])
            elif (div[0] == "ContinueRight"):
                self.traduccion.append("%mover%" + div[1] + "%0")
            elif (div[0] == "ContinueLeft"):
                self.traduccion.append("%mover%-" + (div[1]) + "%0")
            elif (div[0] == "UseColor"):
                self.traduccion.append("%color%" + (div[1]))
            elif (div[0] == "Up"):
                self.traduccion.append("%color%0")
            elif (div[0] == "Down"):
                self.traduccion.append("%color%f")
            elif (div[0] == "PosX"):
                self.traduccion.append("%posicion%" + div[1] + "%f")
            elif (div[0] == "PosY"):
                self.traduccion.append("%posicion%f%-" + div[1])
            elif (div[0] == "Beginning"):
                self.traduccion.append("%posicion%0%0")
            elif ("Pos" in ins):
                posXY = self.obtenerPosXY(ins)
                self.traduccion.append("%posicion%" + posXY[0] + "%-" + posXY[1])

    def run(self):
        self.traduccion.append("%apagar%0")
        self.traduccion.append("%apagar%0")

        for i in self.traduccion:
            time.sleep(1)
            self.arduino.write(bytes(i, 'utf-8'))
            time.sleep(1)
            print(self.arduino.readline())

    def ContinueUp(self, num):
        self.traduccion.append("%mover%0%" + str(num))

    def ContinueDown(self, num):
        self.traduccion.append("%mover%" + str(num) + "%0")

    def ContinueRight(self, num):
        self.traduccion.append("%mover%" + str(num) + "%0")

    def ContinueLeft(self, num):
        self.traduccion.append("%mover%-" + str(num) + "%0")

    def UseColor(self, num):
        self.traduccion.append("%color%" + str(num))

    def Up(self):
        self.traduccion.append("%color%0")

    def Down(self):
        self.traduccion.append("%color%f")

    def PosX(self,num):
        self.instrucciones.append("PosX "+str(num))

    def PosY(self,num):
        self.instrucciones.append("PosY "+str(num))

    def Beginning(self):
        self.traduccion.append("%posicion%0%0")

    def Pos(self, x, y):
        self.traduccion.append("%posicion%" + str(x) + "%-" + str(y))
