from Lexer_CodeSangam import *
from Line import *
from lark import Lark, tree
from lark.lexer import Lexer, Token 
from AST_CodeSangam import *
from graphviz import Digraph
from Semantic_Analyzer import *
from WAT_Generator import *
from error_handling import *
import traceback
import re

current_line = 0
last_token = "Start"
has_error = False

class OurLexer(Lexer):
    def __init__(self, lexer_conf):
        pass

    def lex(self, data):
        global current_line
        global has_error
        global last_token
        lexer = Lexer_(data)
        lexer.classify_lexemes()
        for line in lexer.lines:
            if line.has_error:
                has_error = True
                error = Error(line.line_number, line.error, 'Lexer')
            else:
                current_line = line.line_number
                for token in line.token_list:
                    if token.type != TokenClass.COMMENT and token.type != TokenClass.COMMENT_MARKER:
                        yield Token(str(token.type)[11:], token.content, line=line.line_number)
                        last_token = token

# Grammar for Parsing 
grammar = '''
start: line_temp EOF

line: statement NEW_LINE | NEW_LINE
line_temp: line line_temp |

statement: assignment | print | ifelse | while_loop | for_loop | tryelse | function | closure | function_call | return_func | INDENT DEDENT

# Expression
e: let | e1
e1: e1 ol e2 | e2
e2: e2 comparators e3 | e3 | BANG e3
e3: e3 PLUS e4 | e3 MINUS e4 | e4
e4: e4 ob e5 | e5
e5: e5 EXP e6 | e6
e6: e6 obi e7 | e7
e7: ou e7 | e8
e8: e8 ou | e9
e9: MINUS NUMBER | NUMBER | STRING | SAHI | GALAT | IDENTIFIER | LEFT_PAREN e RIGHT_PAREN | IDENTIFIER DOT COUNT LEFT_PAREN all_e RIGHT_PAREN | IDENTIFIER DOT LEN LEFT_PAREN RIGHT_PAREN | SUM LEFT_PAREN IDENTIFIER RIGHT_PAREN | INT LEFT_PAREN e RIGHT_PAREN | FLOAT LEFT_PAREN e RIGHT_PAREN | STR LEFT_PAREN e RIGHT_PAREN | IDENTIFIER DOT SLICE LEFT_PAREN e COLON e RIGHT_PAREN | IDENTIFIER DOT ACCESS LEFT_PAREN num_temp RIGHT_PAREN | IDENTIFIER LEFT_SQUARE access_temp RIGHT_SQUARE | IDENTIFIER DOT POP LEFT_PAREN access_temp RIGHT_PAREN | IDENTIFIER DOT KEYS LEFT_PAREN RIGHT_PAREN | IDENTIFIER DOT VAL LEFT_PAREN RIGHT_PAREN | IDENTIFIER DOT JOIN LEFT_PAREN IDENTIFIER RIGHT_PAREN | IDENTIFIER DOT INSERT LEFT_PAREN els COMMA all_e RIGHT_PAREN | IDENTIFIER DOT APPEND LEFT_PAREN all_e RIGHT_PAREN | IDENTIFIER DOT COPY LEFT_PAREN RIGHT_PAREN | function_call
ob: MULT | DIV | INT_DIV | MODULO  
ou: PLUS_PLUS | MINUS_MINUS 
obi: AND | OR | XOR 
ol: AND_AND | OR_OR 
comparators: BANG_EQUAL | EQUAL_EQUAL | GREATER | LESS | GREATER_EQUAL | LESS_EQUAL

ed: DICT_LEFT dict_body DICT_RIGHT
dict_body: dict_element dict_temp | 
dict_temp: COMMA dict_element dict_temp |  
dict_element: key COLON value
key: NUMBER | STRING
value: NUMBER | STRING | SAHI | GALAT | ed | els | et

els: LEFT_SQUARE list_body RIGHT_SQUARE
list_body: list_element list_temp | 
list_temp: COMMA list_element list_temp  |
list_element: value

et: LEFT_BRACE list_body RIGHT_BRACE

all_e: e | ed | els | et

data_types: NUM | STR | BOOL | DICT SPECIFIER_START data_types COMMA data_types SPECIFIER_END | LIST SPECIFIER_START data_types SPECIFIER_END | TUP SPECIFIER_START data_types SPECIFIER_END | VOID

assignment: IDENTIFIER all_equal all_e| IDENTIFIER all_equal input | data_types IDENTIFIER EQUAL all_e | IDENTIFIER LEFT_SQUARE access_temp RIGHT_SQUARE all_equal all_e | IDENTIFIER LEFT_SQUARE access_temp RIGHT_SQUARE all_equal input
temp: NUMBER | STRING 
access_temp: temp a_temp
a_temp: COMMA temp a_temp | 
num_temp: NUMBER n_temp
n_temp: COMMA NUMBER n_temp | 
all_equal: EQUAL | PLUS_EQUAL | MINUS_EQUAL | MULT_EQUAL | DIV_EQUAL 

print: PRINT LEFT_PAREN print_body RIGHT_PAREN
print_body: all_e print_temp |
print_temp: COMMA all_e print_temp |  

input: INPUT LEFT_PAREN STRING COMMA data_types RIGHT_PAREN

let: LET assignment IN all_e

ifelse: AGAR LEFT_PAREN condition RIGHT_PAREN COLON NEW_LINE INDENT line_temp DEDENT NEW_LINE magar_temp nahitoh_temp
magar_temp: MAGAR LEFT_PAREN condition RIGHT_PAREN COLON NEW_LINE INDENT line_temp DEDENT NEW_LINE magar_temp |  
nahitoh_temp: NAHITOH COLON NEW_LINE INDENT line_temp DEDENT |  

while_loop: JABTAK LEFT_PAREN all_e RIGHT_PAREN COLON NEW_LINE INDENT line_temp DEDENT nahitoh_temp

for_loop: KELIYE LEFT_PAREN assignment SEMI condition SEMI update RIGHT_PAREN COLON NEW_LINE INDENT line_temp DEDENT nahitoh_temp
update: all_e update_temp | 
update_temp: COMMA all_e update_temp | 
condition: all_e

tryelse: KOSHISH COLON NEW_LINE INDENT line_temp DEDENT NEW_LINE varna
varna: VARNA COLON NEW_LINE INDENT line_temp DEDENT 

function: KARYA func_data_types IDENTIFIER LEFT_PAREN arguments RIGHT_PAREN COLON NEW_LINE INDENT line_temp DEDENT
arguments: data_types COLON IDENTIFIER args |
args: COMMA data_types COLON IDENTIFIER args |  
func_data_types: data_types 
return_func: VAPAS return_type
return_type: all_e | 

function_call: IDENTIFIER LEFT_PAREN function_call_arguments RIGHT_PAREN 
function_call_arguments: all_e input_args | 
input_args: COMMA all_e input_args|  

closure: data_types IDENTIFIER EQUAL KHOLIYE func_data_types LEFT_PAREN arguments RIGHT_PAREN COLON NEW_LINE INDENT line_temp DEDENT

%declare DICT_RIGHT DICT_LEFT IN NUM BOOL STR VAR SAHI GALAT DICT LIST TUP ARR INT FLOAT PRINT INPUT AGAR MAGAR NAHITOH NIKLO KELIYE JABTAK KARYA VAPAS VOID KHOLIYE LET KOSHISH VARNA LEN SLICE COUNT ACCESS APPEND INSERT JOIN SUM POP KEYS VAL COPY LEFT_PAREN RIGHT_PAREN LEFT_BRACE RIGHT_BRACE LEFT_SQUARE RIGHT_SQUARE COMMA DOT COLON SEMI EOF INDENT DEDENT NEW_LINE PLUS PLUS_EQUAL MINUS MINUS_EQUAL MULT MULT_EQUAL DIV DIV_EQUAL INT_DIV EXP MODULO BANG_EQUAL EQUAL_EQUAL GREATER GREATER_EQUAL LESS LESS_EQUAL PLUS_PLUS MINUS_MINUS BANG AND_AND OR_OR OR XOR AND SPECIFIER_START SPECIFIER_END EQUAL IDENTIFIER STRING NUMBER
'''

def tree_to_graphviz(tree, graph=None):

    if graph is None:
        graph = Digraph()

    if isinstance(tree, ast_classes.ASTNode):
        graph.node(str(id(tree)), label=str(tree))
        children = vars(tree).items()
        for _,child in children:
            if _ == 'num_child':
                continue
            if isinstance(child, ast_classes.ASTNode):
                graph.node(str(id(child)), label = str(child))
                graph.edge(str(id(tree)), str(id(child)))
                tree_to_graphviz(child, graph)

            else:
                graph.node(str(id(child)), label=str(child))
                graph.edge(str(id(tree)), str(id(child)))
    return graph

if __name__ == "__main__":
    file_path = sys.argv[1]
    parser = Lark(grammar, parser='lalr', strict=True, lexer=OurLexer)
    try:
        parse_tree = parser.parse(file_path)
    except:
        traceback_str = traceback.format_exc()
        next_token = re.search(r"KeyError: '(.*?)'", traceback_str)
        next_token = next_token.group(1)
        expected_list = traceback_str.split("Expected one of:")
        expected_text = expected_list[1].strip()
        expected_items = [item.strip()[2:] for item in expected_text.split("\n") if item.strip()]
        error_msg = "Instead of " + next_token + ", expected one of the following token after "+str(last_token.type)[11:]+": "+str(expected_items)
        error = Error(current_line, error_msg, 'Parser')
        has_error = False
    # print(parse_tree.pretty())
    if not has_error:
        transformer = OurTransformer()
        ast = transformer.transform(parse_tree)
        graph = tree_to_graphviz(ast)
        graph.render('ASTs/{}'.format(file_path[10:-11]),format='png', view=True)
        scope_tree = analyze_program(ast)
        # convert_program(ast, scope_tree, file_path[10:-11])
        if (len(sys.argv)>=3):
            tree.pydot__tree_to_png( parse_tree, sys.argv[2])