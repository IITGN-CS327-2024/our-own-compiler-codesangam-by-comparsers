from ast_classes import *

_INT = 0
_FLOAT = 1
_STRING = 2
_BOOL = 3
_NULL = 4
_LIST = 5
_DICT = 6
_TUP = 7

_UNDEF = -100 

NODE_OK = 100
ERROR = -1

OB = ['+','-','','/','//','%','*','&','|','^']
OU = ['++','--']
OL = ['&&','||']
COMP = ['!=','==','>','<','<=','>=']

def analyze_program(node):
    table = [[]]
    stack = []

    res = _analyze_program(node, table, stack)

    del table 
    del stack 

    return res

def _analyze_program(node, table, stack):
    i=0
    child_attr = f"children{i}"
    line = getattr(node, child_attr)
    
    status = _UNDEF
    res = NODE_OK
    status = analyze_line(line, table, stack)
        
        # if status < 0:
        #     print(f"ERROR: {type2str(status)}")
        #     res = SEMANTIC_ERROR
        # else:
        #     print(f"OK. Type is {type2str(status)}")
        
        # # Skip Endline
        # i +=1
        # child_attr = f"children{i}"
        # line = getattr(node, child_attr)
    
    return res

def analyze_line(node, table, stack):
    line = node
    print(type(line))
    if isinstance(line, declaration):
        res = analyze_declare(line,table)
    # elif line.data.type == "Assign":
    #     res = analyze_assign(line, table)
    # elif line.data.type == "IfLine":
    #     res = analyze_if_line(line, table, stack)
    # elif line.data.type == "Break":
    #     res = analyze_break_line(line, table, stack)
    # elif line.data.type == "Continue":
    #     res = analyze_continue_line(line, table, stack)
    # elif line.data.type == "Input":
    #     res = analyze_input(line, table)
    # elif line.data.type == "Output":
    #     res = analyze_output(line, table)
    # elif line.data.type == "LoopLine":
    #     res = analyze_loop_line(line, table, stack)
    # else:
    #     res = SEMANTIC_ERROR

    # if res < 0:
    #     return res
    # else:
    return NODE_OK

def analyze_declare(node,table):
    print("hi")
    datatype = node.children0.children0
    id = node.children1
    print(datatype)
    expr = node.children3
    analyze_expr(expr,table,datatype)
    return NODE_OK
    

def analyze_expr(node, table, type):
    # num = node.num_child
    if isinstance(node,e9):
        res = analyze_expr(node.children0.children0, table, type)
    elif node.children1:
        line = node.children1
        if line in (OB or COMP):
            res = analyze_expr(node.children0, table, type)
            if res==NODE_OK:
                res = analyze_expr(node.children2, table, type)
        elif line in OU:
            res = analyze_expr(node.chidren0,table,type)
    line = node.children0
    if line in OU:
        res = analyze_expr(node.children1, table, type)
    # elif line is "NUMBER/STRING/BOOL":
    #     if type==num
    #         res = NODE_OK
    #     else:
    #         res = -100
    # elif symboltable(line)[0]==True:
    #     if node.children1 is "SUM/INT/FLOAT/STR":
    #         if check type:
    #             res = NODE_OK
    #         else:
    #             res = -100
    #     if node.children1 is "LEN/COUNT/SLICE/ACCESS/ACCESSTEMP/POP/KEYS/VAL":
    #         do the needful

    return res

        

def analyze_assign(node, table):
    var = node.child
    expr = var.sibling.sibling

    found_var = analyze_var(var, table)
    if found_var == UNDEFINED_SYMBOL:
        # Add the symbol to the table
        add_symbol(table, var.data.lexeme)

    sym = search_symbol(table, var.data.lexeme)
    valid_expr = analyze_expr(expr, table, sym)
    if valid_expr < 0:
        print("Expression is not valid")
        return valid_expr
    if sym.type != _undef and valid_expr != sym.type:
        print("ERROR: Cannot Modify Type for Identifier", var.data.lexeme, "to", type2str(valid_expr), ". It was", type2str(sym.type))
        return OVERWRITE_TYPE_ERROR
    assign_type(table, var.data.lexeme, valid_expr)
    return valid_expr


def analyze_var(node, table):
    found = search_symbol(table, node.data.lexeme)
    if found is not None:
        return found.type
    print("Variable Symbol Not Found In Symbol Table:", node.data.lexeme)
    return UNDEFINED_SYMBOL