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
    return False

def list_handler(node, dim):
    if node.num_child==1:
        return dim, node.children0
    else:
        if node.children0=='list':
            return list_handler(node.children2, dim+1)
        else:
            error_msg = "List can only have lists in it."
            return -1, error_msg
        
def tup_handler(node, dim):
    if node.num_child==1:
        return dim, node.children0
    else:
        if node.children0=='tup':
            return tup_handler(node.children2, dim+1)
        else:
            error_msg = "Tuples can ontly have Tuples in it."
            return -1, error_msg
        
def dict_handler(node, line):
    val_type = get_type(node.children3, line)
    key_type = node.children2.children0
    return key_type, val_type

def get_type(node, line):
    if node.children0=='list':
        dim, element_type = list_handler(node.children2, 1)
        if dim==-1:
            error = Error(line, element_type, 'Semantic Analyzer')
        result = list_tup_type(dim, element_type)
        return result
    elif node.children0=='tup':
        dim, element_type = tup_handler(node.children2, 1)
        if dim==-1:
            error = Error(line, element_type, 'Semantic Analyzer')
        result = list_tup_type(dim, element_type)
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
        scope_tree.add_variable(identifier, variable_type)
    else:
        error_msg = "Type of expression assigned does not match with the declared data type for variable '{}'.".format(identifier)
        error = Error(identifier.line, error_msg, 'Semantic Analyzer')

def analyze_line(line_node):
    if isinstance(line_node, declaration):
        res = analyze_declare(line_node)

def analyze_program(node):
    for i in range(node.num_child):
        line = getattr(node, "children{}".format(i))
        res = analyze_line(line)