from lexer import Lexer


text_input = """
let a = 5;
"""

def lexer(text_input):
    lexer = Lexer().get_lexer()
    tokens = lexer.lex(text_input)

    for token in tokens:
        print(token)

if __name__ == '__main__':
    lexer(text_input)