from Lexer_CodeSangam import *
from Line import *
from lark import Lark, tree
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
                print()
            else:
                for token in line.token_list:
                    if token.type != TokenClass.COMMENT and token.type != TokenClass.COMMENT_MARKER:
                        yield Token(str(token.type)[11:], token.content)

# Grammar for Parsing
                        

# el: LEFT_PAREN el RIGHT_PAREN | el ol el | ea comparators ea | SAHI | GALAT | IDENTIFIER
 
grammar = '''
start: line_temp EOF

line: statement NEW_LINE | NEW_LINE
line_temp: line line_temp |

statement: assignment | print | ifelse | while | for | tryelse | function | closure | function_call | return | INDENT DEDENT

# Expression
e: let | e1
e1: e1 ol e2 | BANG e2 | e2
e2: e2 comparators e3 | e3
e3: e3 PLUS e4 | e3 MINUS e4 | e4
e4: e4 ob e5 | e5
e5: e5 EXP e6 | e6
e6: e6 obi e7 | e7
e7: ou e7 | e8
e8: e8 ou | e9
e9: NUMBER | STRING | SAHI | GALAT | IDENTIFIER | LEFT_PAREN e RIGHT_PAREN | IDENTIFIER DOT COUNT LEFT_PAREN all_e RIGHT_PAREN | IDENTIFIER DOT LEN LEFT_PAREN RIGHT_PAREN | SUM LEFT_PAREN IDENTIFIER RIGHT_PAREN | INT LEFT_PAREN e RIGHT_PAREN | FLOAT LEFT_PAREN e RIGHT_PAREN | STR LEFT_PAREN e RIGHT_PAREN | IDENTIFIER DOT SLICE LEFT_PAREN e COLON e RIGHT_PAREN | IDENTIFIER DOT ACCESS LEFT_PAREN num_temp RIGHT_PAREN | IDENTIFIER LEFT_SQUARE access_temp RIGHT_SQUARE | IDENTIFIER DOT POP LEFT_PAREN access_temp RIGHT_PAREN | IDENTIFIER DOT KEYS LEFT_PAREN RIGHT_PAREN | IDENTIFIER DOT VAL LEFT_PAREN RIGHT_PAREN | IDENTIFIER DOT JOIN LEFT_PAREN IDENTIFIER RIGHT_PAREN | IDENTIFIER DOT INSERT LEFT_PAREN els COMMA all_e RIGHT_PAREN | IDENTIFIER DOT APPEND LEFT_PAREN all_e RIGHT_PAREN | IDENTIFIER DOT COPY LEFT_PAREN RIGHT_PAREN | function_call
ob: MULT | DIV | INT_DIV | MODULO  
ou: PLUS_PLUS | MINUS_MINUS 
obi: AND | OR | XOR 
ol: AND_AND | OR_OR 
comparators: BANG_EQUAL | EQUAL_EQUAL | GREATER | LESS | GREATER_EQUAL | LESS_EQUAL

ed: DICT_LEFT dict_body DICT_RIGHT
dict_body: dict_element dict_temp | dict_temp
dict_temp: COMMA dict_element dict_temp |  
dict_element: key COLON value
key: NUMBER | STRING
value: NUMBER | STRING | SAHI | GALAT | ed | els | et

els: LEFT_SQUARE list_body RIGHT_SQUARE
list_body: list_element list_temp | list_temp
list_temp: COMMA list_element list_temp  |
list_element: value

et: LEFT_BRACE list_body RIGHT_BRACE

all_e: e | ed | els | et

data_types: NUM | STR | BOOL | DICT SPECIFIER_START data_types COMMA data_types SPECIFIER_END | LIST SPECIFIER_START data_types SPECIFIER_END | TUP SPECIFIER_START data_types SPECIFIER_END  

assignment: IDENTIFIER all_equal all_e| IDENTIFIER all_equal input | data_types IDENTIFIER EQUAL all_e | IDENTIFIER LEFT_SQUARE access_temp RIGHT_SQUARE all_equal all_e
temp: NUMBER | STRING 
access_temp: temp a_temp | a_temp
a_temp: COMMA temp a_temp | 
num_temp: NUMBER n_temp | n_temp
n_temp: COMMA NUMBER n_temp | 
temp_: NUMBER | STRING | ed | els | et | SAHI | GALAT 
all_equal: EQUAL | PLUS_EQUAL | MINUS_EQUAL | MULT_EQUAL | DIV_EQUAL 

print: PRINT LEFT_PAREN print_body RIGHT_PAREN
print_body: all_e print_temp | print_temp
print_temp: COMMA all_e print_temp |  

input: INPUT LEFT_PAREN STRING COMMA data_types RIGHT_PAREN

let: LET assignment IN e1

ifelse: AGAR LEFT_PAREN e RIGHT_PAREN COLON NEW_LINE INDENT line_temp DEDENT NEW_LINE magar_temp nahitoh_temp
magar_temp: MAGAR LEFT_PAREN e RIGHT_PAREN COLON NEW_LINE INDENT line_temp DEDENT NEW_LINE magar_temp |  
nahitoh_temp: NAHITOH COLON NEW_LINE INDENT line_temp DEDENT |  

while: JABTAK LEFT_PAREN e RIGHT_PAREN COLON NEW_LINE INDENT line_temp DEDENT nahitoh_temp

for: KELIYE LEFT_PAREN assignment SEMI e SEMI update RIGHT_PAREN COLON NEW_LINE INDENT line_temp DEDENT nahitoh_temp
update: e update_temp | update_temp
update_temp: COMMA e update_temp | 

tryelse: KOSHISH COLON NEW_LINE INDENT line_temp DEDENT NEW_LINE VARNA COLON NEW_LINE INDENT line_temp DEDENT 

function: KARYA func_data_types IDENTIFIER LEFT_PAREN arguments RIGHT_PAREN COLON NEW_LINE INDENT line_temp DEDENT
arguments: data_types COLON IDENTIFIER args | args
args: COMMA data_types COLON IDENTIFIER args |  
func_data_types: data_types | VOID
return: VAPAS return_type
return_type: all_e | 

function_call: IDENTIFIER LEFT_PAREN function_call_arguments RIGHT_PAREN 
function_call_arguments: all_e input_args | input_args
input_args: COMMA all_e input_args|  

closure: data_types IDENTIFIER EQUAL KHOLIYE func_data_types LEFT_PAREN arguments RIGHT_PAREN COLON NEW_LINE INDENT line_temp DEDENT

%declare DICT_RIGHT DICT_LEFT IN NUM BOOL STR VAR SAHI GALAT DICT LIST TUP ARR INT FLOAT PRINT INPUT AGAR MAGAR NAHITOH NIKLO KELIYE JABTAK KARYA VAPAS VOID KHOLIYE LET KOSHISH VARNA LEN SLICE COUNT ACCESS APPEND INSERT JOIN SUM POP KEYS VAL COPY LEFT_PAREN RIGHT_PAREN LEFT_BRACE RIGHT_BRACE LEFT_SQUARE RIGHT_SQUARE COMMA DOT COLON SEMI EOF INDENT DEDENT NEW_LINE PLUS PLUS_EQUAL MINUS MINUS_EQUAL MULT MULT_EQUAL DIV DIV_EQUAL INT_DIV EXP MODULO BANG_EQUAL EQUAL_EQUAL GREATER GREATER_EQUAL LESS LESS_EQUAL PLUS_PLUS MINUS_MINUS BANG AND_AND OR_OR OR XOR AND SPECIFIER_START SPECIFIER_END EQUAL IDENTIFIER STRING NUMBER
'''

if __name__ == "__main__":
    file_path = sys.argv[1]
    parser = Lark(grammar, parser='lalr', strict=True, lexer=OurLexer)
    parse_tree = parser.parse(file_path)
    print(parse_tree.pretty())

    def make_png(filename):
        tree.pydot__tree_to_png( parse_tree, filename)
    make_png(sys.argv[2])
