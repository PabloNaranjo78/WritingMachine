# Importa el módulo yacc para el compilador
import ply.yacc as yacc

# Pretty Printer
import pprint

# Sys para leer argumentos
import sys

# Generación de números aleatorios
import random

# Si no se da el archivo TXT para correr el programa
if len(sys.argv) != 2:
    exit()

# Define el archivo del programa
archivo_programa = sys.argv[1]

# Se importan los tokens creados en el otro archivo
from SyntaxLearning import tokens
from SyntaxLearning import reserved

# Diccionario de funciones almacenadas del programa para mapear
funciones = {}
lista_funciones = []

# Lista de errores del programa
lista_errores = []

# Cantidad de comentarios
comentarios = []

# Verificaciones
main = 0
num_comentarios = 0
num_variables = 0

# Precedencia para asignar a las operaciones
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)



# Maneja varias sentencias en un programa
def p_sentencias(p):
    ''' sentencias : sentencias sentencia
                            | sentencia
   '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]


# Definición de  sentencia
def p_sentencia_expr(p):
    ''' sentencia : expression
                           | add
                           | put
                           | continue
                           | pos
                           | operacion
                           | condicion
                           | operadorlogico
                           | comentario
                           | funcionreservada
                           | funcion
                           | funcioniter
                           | speed
                           | beginnning
                           | usecolor
                           | write
                           | main
                           | funccall
   '''
    p[0] = p[1]


# Definición de  sentencia
def p_sentencia_expr_error(p):
    ''' sentencia : error
   '''
    lista_errores.append("Error de sintaxis antes de {0} la línea {1}".format(p[1].type, p.lineno(1)))


### Def ###
def p_def(p):
    '''sentencia : DEF LPAREN ID COMMA oper RPAREN SEMI_COLON
                 | DEF LPAREN ID COMMA TRUE RPAREN SEMI_COLON
                 | DEF LPAREN ID COMMA FALSE RPAREN SEMI_COLON'''
    if not p[3][0].islower():
        lista_errores.append("La variable {0} no se pudo definir en la línea {1} ya que debe empezar con una letra minúscula.".format(p[2], p.lineno(2)))
    elif 3 <= len(p[3]) <= 10:
        p[0] = ['DEF', p[3], p[5]]
    else:
        lista_errores.append("La variable {0} no se pudo definir en la línea {1} ya que debe tener más de 3 posiciones y menos de 10 posiciones.".format(p[2], p.lineno(2)))

def p_def_error(p):
    '''sentencia : DEF error SEMI_COLON'''
    lista_errores.append("Error de sintaxis en la función {0} en la línea {1}.".format(p[1], p.lineno(2)))


### Put ###
def p_put(p):
    '''put : PUT LPAREN ID COMMA oper RPAREN SEMI_COLON'''
    p[0] = [p[1], p[3], p[5]]


def p_put_error(p):
    '''put : PUT error SEMI_COLON'''
    lista_errores.append("Error de sintaxis en la función {0} en la línea {1}.".format(p[1], p.lineno(2)))


### Add ###
def p_add(p): # Change corchetes to paren
    '''add : ADD LPAREN ID RPAREN SEMI_COLON
           | ADD LPAREN ID COMMA oper RPAREN SEMI_COLON'''
    if len(p) == 6:
        p[0] = [p[1], p[3], 1]
    else: # len(p) == 8:
        p[0] = [p[1], p[3], p[5]]

def p_add_error(p):
    '''add : ADD error SEMI_COLON
           | ADD LSQUAREPAREN error RSQUAREPAREN SEMI_COLON
           | ADD error RSQUAREPAREN SEMI_COLON'''
    lista_errores.append("Error de sintaxis en la función {0} en la línea {1}.".format(p[1], p.lineno(2)))


###############################
# Definición de valor         #
def p_valor(p):               #
    ''' valor : NUMBER        
              | ID'''         #
    if isinstance(p[1], int): #
        p[0] = p[1]           #
                              #
    else:                     #
        p[0] = str(p[1])      #
###############################


### Continues: ContinueUp, ContinueDowm, ContinueRight, ContinueLeft ###
def p_continue(p):
    '''continue : CONTINUE_UP oper SEMI_COLON
                | CONTINUE_DOWN oper SEMI_COLON
                | CONTINUE_RIGHT oper SEMI_COLON
                | CONTINUE_LEFT oper SEMI_COLON'''
    p[0] = [p[1], p[2]]

def p_continue_error(p):
    '''continue : CONTINUE_UP error SEMI_COLON
                        | CONTINUE_DOWN error SEMI_COLON
                        | CONTINUE_RIGHT error SEMI_COLON
                        | CONTINUE_LEFT error SEMI_COLON
                        | CONTINUE_UP error
                        | CONTINUE_DOWN error
                        | CONTINUE_RIGHT error
                        | CONTINUE_LEFT error'''
    lista_errores.append("Error de sintaxis en la función {0} en la línea {1}.".format(p[1], p.lineno(2)))


### Pos: Pos, PosX, PosY ###
def p_pos(p):
    '''pos : POS LPAREN parametros RPAREN SEMI_COLON
           | POS_X oper SEMI_COLON
           | POS_Y oper SEMI_COLON'''
    if len(p) == 6:
        p[0] = [p[1], p[3]]
    else:
        p[0] = [p[1], p[2]]

def p_pos_error(p):
    '''pos : POS error SEMI_COLON
           | POS_X error SEMI_COLON
           | POS_Y error SEMI_COLON'''
    lista_errores.append("Error de sintaxis en la función {0} en la línea {1}.".format(p[1], p.lineno(2)))


### Up and Down ###
def p_write(p):
    '''write : DOWN SEMI_COLON
             | UP SEMI_COLON'''
    p[0] = p[1]

def p_write_error(p):
    ''' write : DOWN
              | UP'''
    lista_errores.append("Error de sintaxis en la función {0} en la línea {1}.".format(p[1], p.lineno(1)))


### UseColor ###
def p_usecolor(p):
    '''usecolor : USE_COLOR oper SEMI_COLON'''
    if isinstance(p[2], int):
        if 1 <= p[2] <= 2:
            p[0] = [p[1], p[2]]
        else:
            lista_errores.append("Los valores aceptados para UseColor son 1 o 2. Se utilizó {0} en la linea {1}.".format(p[2],p.lineno(1)))
            p[0] = None
    else:
        p[0] = [p[1], p[2]]

def p_usecolor_error(p):
    '''usecolor : USE_COLOR error
                | USE_COLOR error SEMI_COLON'''
    lista_errores.append("Error de sintaxis en la función {0} en la línea {1}.".format(p[1], p.lineno(2)))


### Beginning ###
def p_beginnning(p):
    '''beginnning : BEGINNING SEMI_COLON'''
    p[0] = p[1]

def p_beginnning_error(p):
    '''beginnning : BEGINNING
                  | BEGINNING error SEMI_COLON'''
    lista_errores.append("ERROR: Error de sintaxis en la función {0} en la línea {1}".format(p[1], p.lineno(1)))


### Speed ###
def p_speed(p):
    '''speed : SPEED oper SEMI_COLON'''
    p[0] = [p[1], p[2]]

def p_speed_error(p):
    '''speed : SPEED error SEMI_COLON'''
    lista_errores.append("ERROR: Error de sintaxis en la función {0} en la línea {1}".format(p[1], p.lineno(2)))


# Definicion de operación matemática
def p_expression_op(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if p[2] == '+': # Plus
        p[0] = p[1] + p[3]

    elif p[2] == '-': #Minus
        p[0] = p[1] - p[3]

    elif p[2] == '*': # Times
        p[0] = p[1] * p[3]

    elif p[2] == '/': # Divide
        p[0] = p[1] / p[3]

# Define un término como parte de una expresión
def p_expression_num(p):
    '''expression : NUMBER'''
    p[0] = p[1]


# Expresiones entre paréntesis
def p_factor_expr(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]


# Número negativo error
def p_expression_menos_error(p):
    '''expression : MINUS error'''
    lista_errores.append("ERROR: Error de sintaxis en la función {0} en la línea {1}".format(p[2], p.lineno(1)))



# Definición de comentarios
def p_comentario(p):
    'comentario : COMMENT'

    # Le suma al número de comentarios
    global num_comentarios
    num_comentarios = num_comentarios + 1

    # Agrega el comentario para luego verificar que haya uno en la primera línea
    comentarios.append(p[1])

    # Devuelve el comentario
    p[0] = p[1]



# Condicion
def p_condicion(p):
    """ condicion : oper GREATERTHAN oper
                  | oper SMALLERTHAN oper
                  | oper SMALLEREQUAL oper
                  | oper GREATEREQUAL oper
                  | oper EQUALS oper"""
    p[0] = [p[1], p[2], p[3]]


# Operador de funciones
def p_operadorcondicion(p):
    '''oper : valor
            | expression
            | operacion'''
    if isinstance(p[1], int):
        p[0] = p[1]
    elif isinstance(p[1], list):
        p[0] = p[1]
    else:
        p[0] = str(p[1])



### Equal ###
def p_equal(p):
    """condicion : EQUAL LPAREN oper COMMA oper RPAREN SEMI_COLON"""
    p[0] = [p[1], p[3], p[5]]


### Greater ###
def p_greater(p):
    """ condicion : GREATER LPAREN oper COMMA oper RPAREN SEMI_COLON"""
    p[0] = [p[1], p[3], p[5]]


### Smaller ###
def p_smaller(p):
    """ condicion : SMALLER LPAREN oper COMMA oper RPAREN SEMI_COLON"""
    p[0] = [p[1], p[3], p[5]]


# Error de la función Condición y Comparadores
def p_condicion_error(p):
    ''' condicion : error GREATERTHAN error
                  | error SMALLERTHAN error
                  | error SMALLEREQUAL error
                  | error GREATEREQUAL error
                  | error EQUALS error
                  | EQUAL error SEMI_COLON
                  | SMALLER error SEMI_COLON
                  | GREATER error SEMI_COLON'''
    if p[1] == "Equal" or p[1] == "Smaller" or p[1] == "Greater":
        lista_errores.append("Error de sintaxis en la condición {0} en la línea {1}".format(p[1], p.lineno(2)))
    else:
        lista_errores.append("Error de sintaxis en la condición {0} en la línea {1}".format(p[2], p.lineno(1)))



### And ###
def p_and(p):
    """operadorlogico : AND LPAREN condicion COMMA condicion RPAREN SEMI_COLON"""
    p[0] = [p[1], p[3], p[5]]


### Or ###
def p_or(p):
    """operadorlogico : OR LPAREN condicion COMMA condicion RPAREN SEMI_COLON"""
    p[0] = [p[1], p[3], p[5]]


def p_operadorlogico_error(p):
    '''operadorlogico : OR error SEMI_COLON
                      | AND error SEMI_COLON'''
    lista_errores.append("Error de sintaxis en la función {0} en la línea {1}".format(p[1], p.lineno(2)))


### Substr ###
def p_substr(p):
   """operacion : SUBSTR LPAREN parametros RPAREN SEMI_COLON"""
   resultado = p[3][0] * 2
   op_entera = True
   for i in p[3]:
      if isinstance(i,int) and isinstance(resultado,int):
         resultado = resultado - i
      else:
         op_entera = False

   if op_entera == True:
      p[0] = resultado
   else:
      p[0] = ["Operacion", p[1], p[3]]


### Random ###
def p_random(p):
    """operacion : RANDOM LPAREN expression RPAREN SEMI_COLON"""
    p[0] = random.randint(0, p[3])


### Div ###
def p_div(p):
   """operacion : DIV LPAREN oper COMMA oper RPAREN SEMI_COLON"""
   if isinstance(p[3],int) and isinstance(p[5],int): # Simplifies
      p[0] = p[3] / p[5]
   else:
      p[0] = ["Operacion",p[1],p[3],p[5]]


### Sum ###
def p_sum(p):
    """operacion : SUM LPAREN parametros RPAREN SEMI_COLON"""

    # Como se recibe una lista de parámetros, se suman los parámetros recibidos
    resultado = 0
    op_entera = True
    for i in p[3]:
        if isinstance(i, int):
            resultado = resultado + i
        else:
            op_entera = False

    if op_entera == True:
        p[0] = resultado
    else:
        p[0] = ["Operacion", p[1], p[3]]


### Mult ###
def p_mult(p):
   """operacion : MULT LPAREN parametros RPAREN SEMI_COLON"""
   # Como se recibe una lista de parámetros, se multiplican los parámetros recibidos
   resultado = 1
   op_entera = True
   for i in p[3]:
      if isinstance(i,int):
         resultado = resultado * i
      else:
          op_entera = False
   if op_entera == True:
      p[0] = resultado
   else:
      p[0] = ["Operacion",p[1],p[3]]

def p_operacion_error(p):
    '''operacion : MULT error SEMI_COLON
                 | SUM error SEMI_COLON
                 | DIV error SEMI_COLON
                 | RANDOM error SEMI_COLON
                 | SUBSTR error SEMI_COLON'''
    lista_errores.append("Error de sintaxis en la función {0} en la línea {1}".format(p[1], p.lineno(2)))


def p_parametros(p):
    '''parametros : expression
                  | valor
                  | oper
                  | parametros COMMA oper'''

    # Si es solo una expression
    if len(p) == 2:
        p[0] = [p[1]]

    # Si son más de dos
    else:
        p[0] = p[1] + [p[3]]


### Run ###
def p_run(p):
    '''funcionreservada : RUN LSQUAREPAREN ordenes RSQUAREPAREN SEMI_COLON'''
    # Solo devuelve las órdenes a ejecutar
    p[0] = p[3]


### Repeat ###
def p_repeat(p):
    '''funcionreservada : REPEAT oper LSQUAREPAREN ordenes RSQUAREPAREN SEMI_COLON'''
    # Devuelve las ordenes a ejecutar y numero de veces que debe hacerlo
    p[0] = [p[1], p[4], p[2]]


### If ###
def p_if(p):
    '''funcionreservada : IF LPAREN condicion RPAREN LSQUAREPAREN ordenes RSQUAREPAREN SEMI_COLON
                        | IF LPAREN operadorlogico RPAREN LSQUAREPAREN ordenes RSQUAREPAREN SEMI_COLON'''
    p[0] = ['IF', p[3], p[6]]


### If Else ###
def p_ifelse(p):
    '''funcionreservada : IF_ELSE LPAREN condicion RPAREN LSQUAREPAREN ordenes RSQUAREPAREN LSQUAREPAREN ordenes RSQUAREPAREN SEMI_COLON
                        | IF_ELSE LPAREN operadorlogico RPAREN LSQUAREPAREN ordenes RSQUAREPAREN LSQUAREPAREN ordenes RSQUAREPAREN SEMI_COLON'''
    # Si se cumple la condición, devuelve las ordenes a ejecutar
    p[0] = ['IF_ELSE', p[3], p[6], p[9]]

def p_funcionreservada_error(p):
    '''funcionreservada : IF error SEMI_COLON
                                       | IF_ELSE error SEMI_COLON
                                       | REPEAT error SEMI_COLON
                                       | RUN error SEMI_COLON'''
    lista_errores.append("Error de sintaxis en la función {0} en la línea {1}".format(p[1], p.lineno(2)))


### Until ###
def p_until(p):
    '''funcioniter : UNTIL LSQUAREPAREN ordenes RSQUAREPAREN LSQUAREPAREN condicion RSQUAREPAREN SEMI_COLON
                   | UNTIL LSQUAREPAREN ordenes RSQUAREPAREN LPAREN condicion  RPAREN SEMI_COLON
                   | UNTIL LSQUAREPAREN ordenes RSQUAREPAREN LSQUAREPAREN operadorlogico RSQUAREPAREN SEMI_COLON
                   | UNTIL LSQUAREPAREN ordenes RSQUAREPAREN LPAREN operadorlogico  RPAREN SEMI_COLON'''
    # Retorna la informacion necesaria para su evaluacion
    p[0] = [p[1], p[3], p[6]]


### While ###
def p_while(p):
    '''funcioniter : WHILE  LSQUAREPAREN condicion RSQUAREPAREN LSQUAREPAREN ordenes RSQUAREPAREN SEMI_COLON
                   | WHILE LPAREN condicion RPAREN LSQUAREPAREN ordenes RSQUAREPAREN SEMI_COLON
                   | WHILE  LSQUAREPAREN operadorlogico RSQUAREPAREN LSQUAREPAREN ordenes RSQUAREPAREN SEMI_COLON
                   | WHILE LPAREN operadorlogico RPAREN LSQUAREPAREN ordenes RSQUAREPAREN SEMI_COLON'''
    # Retorna la informacion necesaria para su evaluacion
    p[0] = [p[1], p[6], p[3]]


def p_funcionreservada_error(p):
    '''funcionreservada : WHILE error SEMI_COLON
                        | UNTIL error SEMI_COLON'''
    lista_errores.append("Error de sintaxis en la función {0} en la línea {1}".format(p[1], p.lineno(2)))


# For functions #
def p_funciones(p):
    '''funcion : PARA ID LSQUAREPAREN parametros RSQUAREPAREN LSQUAREPAREN ordenes RSQUAREPAREN FIN'''
    # Si se intenta usar una palabra reservada como ID
    if p[2] in reserved.values():
        lista_errores.append("La función {0} no se pudo definir en la línea {1} ya que no puede tener el mismo nombre que una palabra reservada".format(p[2], p.lineno(2)))

    # Si no hay ningún procedimiento definido con este nombre
    if p[2] not in funciones:
        funciones[p[2]] = [len(lista_funciones)]
        lista_funciones.append([p[4], p[7]])

        # Si ya existe un procedimiento con este nombre
    elif p[2] in funciones:
        flag = True

        # Busca el procedimiento en el diccionario y la posición que tiene en la lista de funciones
        for i in funciones[p[2]]:
            # Verifica en la lista de funciones si aparte de tener el mismo nombre, tienen la misma cantidad de parámetros
            if len(lista_funciones[i][0]) == len(p[4]):
                lista_errores.append("La función {0} no se pudo definir en la línea {1} ya que está duplicada".format(p[2], p.lineno(2)))

                # Define el flag como falso para que no se agregue luego la función a la lista en caso de estar duplicado
                flag = False

        # Si se determina que los parámetros son diferentes, la agrega a la lista
        if flag == True:
            funciones[p[2]] = funciones[p[2]] + [len(lista_funciones)]
            lista_funciones.append([p[4], p[7]])

        # Definición de errores para los procedimientos


def p_funciones_error(p):
    '''funcion : PARA error SEMI_COLON'''
    lista_errores.append("ERROR: Error de sintaxis en la definición de procedimiento en la línea {0}".format(p.lineno(2)))


# Definición de MAIN
def p_main(p):
    '''main : PARA MAIN LSQUAREPAREN ordenes RSQUAREPAREN FIN'''
    global main

    if main != 0:
        lista_errores.append("ERROR: No puede haber más de una definición de Main, se encontró otra definición en la línea {0}".format(p.lineno(2)))

    else:
        main = main + 1
        p[0] = [p[2], p[4]]


def p_main_error(p):
    '''main : PARA MAIN error FIN
                 | PARA MAIN error LSQUAREPAREN ordenes RSQUAREPAREN FIN
                 | PARA MAIN LSQUAREPAREN error RSQUAREPAREN LSQUAREPAREN ordenes RSQUAREPAREN FIN'''
    if len(p) == 5:
        lista_errores.append("Error en la definición de Main en la línea {0}.".format(p.lineno(3)))
    else:
        lista_errores.append("Error en la definición de Main en la línea {0}. Main no puede incluir parámetros".format(p.lineno(3)))


def p_funccall(p):
    """funccall : ID LSQUAREPAREN parametros RSQUAREPAREN SEMI_COLON"""
    p[0] = ['funccall', p[1], p[3]]


def p_ordenes(p):
    '''ordenes : continue
               | funcionreservada
               | add
               | pos
               | operacion
               | put
               | funccall
               | sentencia
               | funcioniter
               | ordenes add
               | ordenes funccall
               | ordenes sentencia
               | ordenes funcionreservada
               | ordenes continue
               | ordenes funcioniter
               | ordenes put
               | ordenes pos
               | ordenes operacion'''

    # Si es solo un elemento
    if len(p) == 2:
        p[0] = [p[1]]

    # Si es más de una orden, se concatenan
    else:
        p[0] = p[1] + [p[2]]








#################### PARSER ####################

# Construye el parser
parser = yacc.yacc()

# Crea el printer para poder imprimir tanto en el Shell de Python como en CMD
pp = pprint.PrettyPrinter(indent=2)

# Implementación para leer un archivo que será el insumo del parser
with open(archivo_programa, 'r') as archivo:
    insumo = archivo.read()
    resultado = parser.parse(insumo)

    # Elimina las producciones vacías (None)
    if resultado != None:
        resultado = list(filter(None, resultado))

    # Imprime el resultado del parser
    print("\n--------- Resultados del parser ---------")
    pp.pprint(resultado)
