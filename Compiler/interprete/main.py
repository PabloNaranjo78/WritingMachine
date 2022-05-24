from lexer import Lexer


text_input = """
Def(nombrevariable, 15);
"""

def lexer(text_input):
    lexer = Lexer().get_lexer()
    tokens = lexer.lex(text_input)

    for token in tokens:
        print(token)

if __name__ == '__main__':
    lexer(text_input)