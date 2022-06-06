import Compiler.Semantic as c
traduccion = []
def dele():
    from Compiler.Semantic import instrucciones

    print("data")
    for instruccion in instrucciones:
        print(instruccion)
    send_instruccion(instrucciones)
    return traduccion

def send_instruccion(instrucciones):
    for div in instrucciones:
        if (div[0] == "ContinueUp"):
            traduccion.append("%mover%0%-" + str(div[1]))
        elif (div[0] == "ContinueDown"):
            traduccion.append("%mover%0%" + str(div[1]))
        elif (div[0] == "ContinueRight"):
            traduccion.append("%mover%" + str(div[1]) + "%0")
        elif (div[0] == "ContinueLeft"):
            traduccion.append("%mover%-" + (str(div[1])) + "%0")
        elif (div[0] == "UseColor"):
            traduccion.append("%color%" + (str(div[1])))
        elif (div[0] == "Up"):
            traduccion.append("%color%0")
        elif (div[0] == "Down"):
            traduccion.append("%color%f")
        elif (div[0] == "PosX"):
            traduccion.append("%posicion%"+ str(div[1]) + "%f")
        elif (div[0] == "PosY"):
            traduccion.append("%posicion%f%-"+ str(div[1]))
        elif (div[0] == "Beginning"):
            traduccion.append("%posicion%0%0")
        elif (div[0] == "Pos"):
            traduccion.append("%posicion%" + str(div[1]) + "%-" + str(div[2]))
        else:
            traduccion.append("%apagar%0")
