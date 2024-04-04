from ast_classes import *
from symbol_table import *
from error_handling import *

_NUM = 1
_STRING = 2
_BOOL = 3
_LIST = 4
_TUP = 5
_DICT = 6
_UNDEF = -100
_ERROR = -1

scope_tree = Scope_tree()

def analyze_expression(node, variable_type):
    return True

def list_handler(node, line):
    if node.num_child==1:
        return node.children0
    else:
        return get_type(node.children2, line)
        
def tup_handler(node, line):
    if node.num_child==1:
        return node.children0
    else:
        return get_type(node.children2, line)
        
def dict_handler(node, line):
    val_type = get_type(node.children3, line)
    key_type = node.children2.children0
    return key_type, val_type

def get_type(node, line):
    if node.children0=='list':
        element_type = list_handler(node.children2, line)
        result = list_type(element_type)
        return result
    elif node.children0=='tup':
        element_type = tup_handler(node.children2, line)
        result = tup_type(element_type)
        return result
    elif node.children0=='dict':
        k, val_type = dict_handler(node, line)
        if k!='num' or k!='str' or k!='bool':
            error_msg = "The dictionay can only have num, bool, or str as the data type."
            error = Error(line, error_msg, 'Semantic Analyzer')
        result = dict_type(k, val_type)
        return result
    else:
        return node.children0

def analyze_declare(line_node):
    data_type_node = line_node.children0
    identifier = line_node.children1
    variable_type = get_type(data_type_node, identifier.line)
    value_expression = line_node.children3
    match = analyze_expression(value_expression, variable_type)
    if match:
        scope_tree.add_variable(identifier, variable_type, identifier.line)
        return True
    else:
        error_msg = "Type of expression assigned does not match with the declared data type for variable '{}'.".format(identifier)
        error = Error(identifier.line, error_msg, 'Semantic Analyzer')
        return False
    
def analyze_assignment(line_node):
    identifier = line_node.children0
    variable_type = scope_tree.type_variable(identifier)
    line = identifier.line
    if variable_type == -1:
        error_msg = "The variable '{}' needs to be defined first.".format(identifier)
        error = Error(line, error_msg, 'Semantic Analyzer')
    if line_node.num_child==3:
        equal_type = line_node.children1.children0
        if str(line_node.children2) == 'input_':
            data_type_node = line_node.children2.children1
            assign_type = get_type(data_type_node, line)
            if assign_type == variable_type:
                match = True
            else:
                match = False
            if not match:
                error = Error(line, "The inpus asks for a different data_type than that of the variable '{}'.".format(identifier))
        else:
            expression = line_node.children2
            match = analyze_expression(expression, variable_type)
            if not match : 
                error = Error(line, "The type of variable '{}' does not match with the assignment expression.".format(identifier), 'Semantic Analyzer')
        if equal_type=='+=' and (variable_type!='str' and variable_type!='num'):
            error = Error(line, "The += can only be used for str and num data_types.", 'Semantic Analyzer')
        if (equal_type=='-=' or equal_type=='/=' or equal_type=='*=') and variable_type!='num':
            error = Error(line, "The {} can only be used for num data_type".format(equal_type))
        return True
    else:
        equal_type = line_node.children2.children0
        if str(line_node.children3) == 'input_':
            data_type_node = line_node.children3.children1
            assign_type = get_type(data_type_node, line)
            if assign_type == variable_type:
                match = True
            else:
                match = False
            if not match:
                error = Error(line, "The inpus asks for a different data_type than that of the variable '{}'.".format(identifier))
        else:
            expression = line_node.children3
            match = analyze_expression(expression, variable_type)
            if not match : 
                error = Error(line, "The type of variable '{}' does not match with the assignment expression.".format(identifier), 'Semantic Analyzer')
        if equal_type=='+=' and (variable_type!='str' and variable_type!='num'):
            error = Error(line, "The += can only be used for str and num data_types.", 'Semantic Analyzer')
        if (equal_type=='-=' or equal_type=='/=' or equal_type=='*=') and variable_type!='num':
            error = Error(line, "The {} can only be used for num data_type".format(equal_type))
        return True

def analyze_line(line_node):
    if isinstance(line_node, declaration):
        res = analyze_declare(line_node)
    if isinstance(line_node, assignment):
        res = analyze_assignment(line_node)

def analyze_program(node):
    for i in range(node.num_child):
        line = getattr(node, "children{}".format(i))
        res = analyze_line(line)