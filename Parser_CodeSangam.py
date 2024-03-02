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
            if line.has_error:
                print("Error at [line", line.line_number, "]")
                print("ERROR:", line.error)
            else:
                for token in line.token_list:
                    yield Token(str(token.type)[11:], token.content)

# Grammer for Parsing
grammer = '''
start: EOF

%declare IN NUM BOOL STR VAR SAHI GALAT DICT LIST TUP ARR INT FLOAT PRINT INPUT AGAR MAGAR NAHITOH NIKLO KELIYE JABTAK KARYA VAPAS VOID KHOLIYE LET KOSHISH VARNA LEN SLICE COUNT ACCESS APPEND INSERT JOIN SUM POP KEYS VAL COPY LEFT_PAREN RIGHT_PAREN LEFT_BRACE RIGHT_BRACE LEFT_SQUARE RIGHT_SQUARE COMMA DOT COLON SEMI EOF START_INDENT END_INDENT NEW_LINE PLUS PLUS_EQUAL MINUS MINUS_EQUAL MULT MULT_EQUAL DIV DIV_EQUAL INT_DIV EXP MODULO BANG_EQUAL EQUAL_EQUAL GREATER GREATER_EQUAL LESS LESS_EQUAL PLUS_PLUS MINUS_MINUS BANG AND_AND OR_OR OR XOR AND SPECIFIER_START SPECIFIER_END EQUAL IDENTIFIER STRING NUMBER COMMENT_MARKER COMMENT
'''

if __name__ == "__main__":
    file_path = sys.argv[1]
    parser = Lark(grammer, parser='lalr', lexer=OurLexer)
    tree = parser.parse(file_path)
    print(tree)