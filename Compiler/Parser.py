import ply.yacc as yacc

from Syntax import tokens

## Setting precedence order
#precedence = (
#    ('left', 'PLUS', 'MINUS'),
#    ('left', 'TIMES', 'DIVIDE'),
#    ('right', 'UMINUS')
#        )

#  _______________ #
# / Grammar rules  #
# ---------------- #

## To work with numbers
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : value'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

#######################################

## -- Others -- ##
def p_asiggn(p):
    '''assign : DEF
              | PUT
              | ADD'''
    p[0] = p[1]

# Def
def p_def(p): #Validar asignacion
    '''expression : DEF LPAREN ID COMMA expression RPAREN SEMI_COLON
                  | DEF LPAREN ID COMMA TRUE RPAREN SEMI_COLON
                  | DEF LPAREN ID COMMA FALSE RPAREN SEMI_COLON'''
    p[0] = ['DEF', p[3], p[5]]

# Put   
def p_put(p): #Validar asignacion
    '''expression : PUT LPAREN ID COMMA expression RPAREN SEMI_COLON'''
    p[0] = ['PUT', p[3], p[5]]

# Add
def p_add(p): #Validar asignacion
    '''expression : ADD LPAREN ID RPAREN SEMI_COLON
                  | ADD LPAREN ID COMMA expression RPAREN SEMI_COLON'''
    if len(p) == 6:
        p[0] = ['ADD', p[3], 1] # Tree structure to add 1
    else: #len(p) == 8
        p[0] = ['ADD', p[3], p[5]] # Tree structure to mult by p[5]

# Continues: Up, Down, Right, Left
def p_continue(p): #Validar asignacion
    '''expression : CONTINUE_UP expression SEMI_COLON
                | CONTINUE_DOWN expression SEMI_COLON
                | CONTINUE_RIGHT expression SEMI_COLON 
                | CONTINUE_LEFT expression SEMI_COLON'''
    p[0] = [p[1], p[2]]

# Positions: Pos, PosX, PosY
def p_pos(p): #Validar asignacion
    '''expression : POS LPAREN expression COMMA expression RPAREN SEMI_COLON
                  | POS_X expression SEMI_COLON
                  | POS_Y expression SEMI_COLON'''
    if len(p) == 8:
        p[0] = ['POS', (p[3], p[5])]
    else: # len(p) == 4
        p[0] = [p[1], p[2]]

# UseColor
def p_usecolor(p): #Validar asignacion
    '''expression : USE_COLOR NUMBER SEMI_COLON'''
    if p[2] == 1 or p[2] == 2:
        p[0] = ['USE_COLOR', p[2]]
    # else: # Devolver error

# Up
def p_up(p):
    '''expression : UP SEMI_COLON'''
    p[0] = [p[1]]

# Down
def p_down(p):
    '''expression : DOWN SEMI_COLON'''
    p[0] = [p[1]]

# Beginning
def p_beginning(p):
    '''expression : BEGINNING SEMI_COLON'''
    p[0] = [p[1]]

# Speed
def p_speed(p):
    '''expression : SPEED expression SEMI_COLON'''
    p[0] = ['SPEED', p[2]]

# And
def p_and(p):
    '''expression : AND LPAREN expression COMMA expression RPAREN SEMI_COLON'''
    p[0] = ['AND', p[3], p[5]]

# Or
def p_or(p):
    '''expression : OR LPAREN expression COMMA expression RPAREN SEMI_COLON'''
    p[0] = ['OR', p[3], p[5]]

# Equal
def p_equal(p):
    '''expression : EQUAL LPAREN expression COMMA expression RPAREN SEMI_COLON'''
    p[0] = ['EQUAL', p[3], p[5]]

# Greater
def p_greater(p):
    '''expression : GREATER LPAREN expression COMMA expression RPAREN SEMI_COLON'''
    p[0] = ['GREATER', p[3], p[5]]

# Smaller
def p_smaller(p):
    '''expression : SMALLER LPAREN expression COMMA expression RPAREN SEMI_COLON'''
    p[0] = ['SMALLER', p[3], p[5]]

# Substr
def p_substr(p):
    '''expression : SUBSTR LPAREN expression COMMA expression RPAREN SEMI_COLON'''
    p[0] = ['SUBSTR', p[3], p[5]]

# Random
def p_random(p):
    '''expression : RANDOM LPAREN expression RPAREN SEMI_COLON'''
    p[0] = ['RANDOM', p[3]]

# Mult
def p_mult(p):
    '''expression : MULT LPAREN expression COMMA expression RPAREN SEMI_COLON'''
    p[0] = ['MULT', p[3], p[5]]

# Div
def p_div(p):
    '''expression : DIV LPAREN expression COMMA expression RPAREN SEMI_COLON'''
    p[0] = ['DIV', p[3], p[5]]

# Sum
def p_sum(p):
    '''expression : SUM LPAREN expression COMMA expression RPAREN SEMI_COLON'''
    p[0] = ['SUM', p[3], p[5]]

# Print
def p_print(p):
    '''expression : PRINT LPAREN expression RPAREN SEMI_COLON'''
    p[0] = ['PRINT', p[3]]

## Pendientes:
# - Run
# - Repeat
# - If
# - IfElse
# - Until
# - While
# Validacion - Under construction -

















"""
def p_id_def(p):
    'value : DEF LPAREN ID COMMA expression RPAREN SEMI_COLON'
    p[0] = p[5]

def p_id_put(p):
    'value : PUT LPAREN ID COMMA expression RPAREN'
    p[0] = p[5]

def p_add_one(p):
    'expression : ADD LPAREN expression RPAREN'
    p[0] = p[3] + 1

def p_add_two(p):
    'expression : ADD LPAREN expression COMMA expression RPAREN'
    p[0] = p[3] * p[5]

def p_continue_up(p):
    'expression : CONTINUE_UP expression'
    p[0] = p[2]

def p_continue_down(p):
    'expression : CONTINUE_DOWN expression'
    p[0] = p[2]

def p_continue_right(p):
    'expression : CONTINUE_RIGHT expression'
    p[0] = p[2]

def p_continue_left(p):
    'expression : CONTINUE_LEFT expression'
    p[0] = p[2]

def p_pos_xy(p):
    'expression : POS LPAREN expression COMMA expression RPAREN'
    p[0] = p[3], p[5]

def p_pos_x(p):
    'expression : POS_X expression'
    p[0] = p[2]

def p_pos_y(p):
    'expression : POS_Y expression'
    p[0] = p[2]

def p_use_color(p):
    'expression : USE_COLOR expression'
    p[0] = p[2]

def p_print(p):
    'expression : PRINT LPAREN expression RPAREN'
    p[0] = p[3]
    print(p[3])
"""
def p_value_values(p):
    '''value : NUMBER
             | TRUE
             | FALSE 
             | ID''' ## Add cadena de caracteres para poder meter comillas en el print
    p[0] = p[1]

#######################################

# To handle errors
def p_error(p):
    print("Syntax error in input!")

#######################################

parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)








