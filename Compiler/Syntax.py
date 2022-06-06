# Func for number len
def numLen(n):
    cont = 0
    while num > 0:
        num = num // 10
        cont += 1
#

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
        'PrintLine' : 'PRINT'
        }

## For operations
t_PLUS   = r'\+'
t_MINUS  = r'\-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'

## Parenthesis
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LSQUAREPAREN = r'\['
t_RSQUAREPAREN = r'\]'

## Separator
t_COMMA = "\,"

## Semicolon
t_SEMI_COLON = "\;"

## True or False
t_TRUE  = r'TRUE'
t_FALSE = r'FALSE'

## Keywords
tokens = [
        'NUMBER',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'LPAREN',
        'RPAREN',
        'LSQUAREPAREN',
        'RSQUAREPAREN',
        'ID',
        'COMMA',
        'SEMI_COLON',
        'TRUE',
        'FALSE'
        ] + list(reserved.values())

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#@TOKEN(identifier)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_COMMENT(t):
    r'\#.*'
    pass #No value returned. Token discarded

lexer = lex.lex() 

# Test it out
data = '''
Def(var1, 3);
ContinueUp 2;
PosY 14;
If Equal(2,2) [Beginning];
PrintLine(var1);
Sum(4,5);
While [Equal(1,1)]
[Up; PosY 90];
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









