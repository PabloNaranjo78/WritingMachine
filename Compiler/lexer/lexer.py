from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add('DEF', r'Def')
        self.lexer.add('FLOAT', '-?\d+.\d+')
        self.lexer.add('INTEGER', '-?\d+')
        self.lexer.add('STRING', '(""".?""")|(".?")|(\'.?\')')
        self.lexer.add('BOOLEAN', "true(?!\w)|false(?!\w)")
        self.lexer.add('IF', 'if(?!\w)')
        self.lexer.add('ELSE', 'else(?!\w)')
        self.lexer.add('END', 'end(?!\w)')
        self.lexer.add('AND', "and(?!\w)")
        self.lexer.add('OR', "or(?!\w)")
        self.lexer.add('NOT', "not(?!\w)")
        self.lexer.add('LET', 'let(?!\w)')
        self.lexer.add('FUNCTION', 'func(?!\w)')
        self.lexer.add('MODULE', 'mod(?!\w)')
        self.lexer.add('IMPORT', 'import(?!\w)')
        self.lexer.add('IDENTIFIER', "[a-zA-Z_][a-zA-Z0-9_]")
        self.lexer.add('==', '==')
        self.lexer.add('!=', '!=')
        self.lexer.add('>=', '>=')
        self.lexer.add('<=', '<=')
        self.lexer.add('>', '>')
        self.lexer.add('<', '<')
        self.lexer.add('=', '=')
        self.lexer.add('[', '[')
        self.lexer.add(']', ']')
        self.lexer.add('{', '{')
        self.lexer.add('}', '}')
        self.lexer.add('|', '|')
        self.lexer.add(',', ',')
        self.lexer.add('DOT', '.')
        self.lexer.add('COLON', ':')
        self.lexer.add('PLUS', '+')
        self.lexer.add('MINUS', '-')
        self.lexer.add('MUL', '*')
        self.lexer.add('DIV', '/')
        self.lexer.add('MOD', '%')
        self.lexer.add('(', '(')
        self.lexer.add(')', ')')
        self.lexer.add('NEWLINE', '\n')

        # ignore whitespace
        self.lexer.ignore('[ \t\r\f\v]+')
        # Ignore spaces
        #self.lexer.ignore('\s+')
        #NAMES
        self.lexer.add("ID", r"[][a-zA-Z][a-zA-Z0-9]*")

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()