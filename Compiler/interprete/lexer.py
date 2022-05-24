from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('DEF', r'Def')
        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')
        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        # Number
        self.lexer.add('NUMBER', r'\d+')
        #Identifier
        self.lexer.add('IDENTIFIER', "[a-zA-Z_][a-zA-Z0-9_]*")
        # Ignore spaces
        self.lexer.ignore('\s+')
        # Comma
        self.lexer.add('COMMA', ',')
        # Float
        self.lexer.add('FLOAT', '-?\d+.\d+')
        # Integer
        self.lexer.add('INTEGER', '-?\d+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()