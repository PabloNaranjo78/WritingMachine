import ply.lex as lex
from ply.lex import TOKEN

reserved = {
        'Def' : 'DEF',
        'Put' : 'PUT',
        'Add' : 'ADD',
        'ContinueUp' : 'CONTINUE_UP',
        'ContinueDown' :'CONTINUE_DOWN',
        'ContinueLeft' : 'CONTINUE_RIGHT',
        'ContinueRight' : 'CONTINUE_LEFT',
        'Pos' : 'POS',
        'PosX' : 'POS_X',
        'PosY' : 'POS_Y',
        'UseColor' : 'USE_COLOR',
        'Down' : 'DOWN',
        'Up' : 'UP',
        'Beginning' : 'BEGINNING',
        'Speed' : 'SPEED',
        'Run' : 'RUN',
        'Repeat' : 'REPEAT',
        'If' : 'IF',
        'IfElse' : 'IF_ELSE',
        'Until' : 'UNTIL',
        'While' : 'WHILE',
        'Equal' : 'EQUAL',
        'And' : 'AND',
        'Or' : 'OR',
        'Greater' : 'GREATER',
        'Smaller' : 'SMALLER',
        'Substr' : 'SUBSTR',
        'Random' : 'RANDOM',
        'Mult' : 'MULT',
        'Div' : 'DIV',
        'Sum' : 'SUM',
        'PrintLine' : 'PRINT',
        'MAIN' : 'MAIN',
        'PARA' : 'PARA',
        'FIN' : 'FIN',

        'TRUE' : 'TRUE' ,
        'FALSE' : 'FALSE'
        }

## For operations
t_PLUS   = r'\+'
t_MINUS  = r'\-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_POW    = r'\^'

## For comparisons
t_GREATERTHAN  = r'\>'
t_SMALLERTHAN  = r'\<'
t_GREATEREQUAL = r'\>='
t_SMALLEREQUAL = r'\<='
t_EQUALS       = r'\='

## Parenthesis
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LSQUAREPAREN = r'\['
t_RSQUAREPAREN = r'\]'

## Separator
t_COMMA = "\,"

## Semicolon
t_SEMI_COLON = "\;"

## Keywords
tokens = [
        'ID',
        'COMMENT',
        'NUMBER',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'POW',
        'GREATERTHAN',
        'SMALLERTHAN',
        'GREATEREQUAL',
        'SMALLEREQUAL',
        'EQUALS',
        'LPAREN',
        'RPAREN',
        'LSQUAREPAREN',
        'RSQUAREPAREN',
        'COMMA',
        'SEMI_COLON'
        ] + list(reserved.values())

# Sets how to declare a variable
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9@]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Sets the properties to declare a number
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Counts new lines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignores white spaces and tabs
t_ignore = ' \t'

# Defines comments structure
def t_COMMENT(t):
    r'\//.*'
    return t

# Handles errors
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Handles end of file
def t_eof(t):
    return None

# Builds the lexer
lexer = lex.lex() 


##  _____ ##
## /TESTS ##
## ------ ##

# Test it out
data = '''
Def(var1, 3);
ContinueUp 2;
TRUE
PosY 14;
If Equal(2,2) [Beginning];
PrintLine(var1);
Sum(4,5);
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
#for tok in lexer:
#    print(tok)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok.type, tok.value, tok.lineno, tok.lexpos)

# .type: Tipo
# .value: Valor en cuestion
# .lineno: Numero de linea
# .lexpos: Numero de posicion
