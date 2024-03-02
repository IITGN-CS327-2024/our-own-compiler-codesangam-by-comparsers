from Lexer_CodeSangam import *
from Line import *
from lark import Lark
from lark.lexer import Lexer, Token 

class OurLexer(Lexer):
    def __init__(self, lexer_conf):
        pass

    def lex(self, data):
        lexer = Lexer_(data)
        lexer.classify_lexemes()
        for line in lexer.lines:
            for token in line.token_list:
                yield Token(str(token.type)[11:], token.content)

# Grammer for Parsing
grammer = '''
    start: 
'''

if __name__ == "__main__":
    file_path = sys.argv[1]
    parser = Lark(grammer, lexer=OurLexer)
    tree = parser.parse(file_path)
    print(tree)