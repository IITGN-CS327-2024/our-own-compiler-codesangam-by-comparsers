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
    
def access_handler(var_type, node, line):
    current_type = var_type
    for i in range(node.num_child):
        temp = getattr(node, "children{}".format(i))
        if temp.type=="STRING":
            if not isinstance(current_type, dict_type):
                error = Error(line, "Invalid Access", 'Semantic Analyzer') 
        if temp.type=="NUMBER":
            if not (isinstance(current_type, dict_type) or isinstance(current_type, list_type)):
                error = Error(line, "Invalid Access", 'Semantic Analyzer')
        if isinstance(current_type, dict_type):
            current_type = current_type.val_type
        else:
            current_type = current_type.element_type
    return current_type

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
        access_node = line_node.children1
        variable_type = access_handler(variable_type, access_node, line)
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

def analyze_while(line_node):
    cond = line_node.children1
    match = analyze_expression(cond,bool)
    if match:
        scope_tree.create_scope()
        for i in range(2,line_node.num_child):
            line = getattr(line_node, "children{}".format(i))
            res = analyze_line(line)
        scope_tree.close_scope()
    else:
        error_msg = "Type of expression given as while condition is not of boolean type '{}'.".format(cond)
        error = Error(line_node.children0.line, error_msg, 'Semantic Analyzer')

def analyze_for(line_node):
    declare = line_node.children1
    analyze_declare(declare)
    cond = line_node.children2
    match = analyze_expression(cond,bool)
    if match:
        scope_tree.create_scope()
        for i in range(4,line_node.num_child):
            line = getattr(line_node, "children{}".format(i))
            res = analyze_line(line)
        scope_tree.close_scope()
    else:
        error_msg = "Type of expression given as for condition is not of boolean type '{}'.".format(cond)
        error = Error(line_node.children0.line, error_msg, 'Semantic Analyzer')

def analyze_function(line_node):
    func_name = line_node.children2
    line = func_name.line
    return_type = get_type(line_node.children1, line)
    arg_node = line_node.children3
    args = []
    input_names = []
    for i in range(0, arg_node.num_child, 2):
        temp_type = get_type(getattr(arg_node, "children{}".format(i)), line)
        args.append(temp_type)
        var_name = getattr(arg_node, "children{}".format(i+1))
        input_names.append(var_name)
    function_type = func_type(args, return_type)
    scope_tree.add_variable(func_name, function_type, line)
    scope_tree.create_scope()
    for i in range(len(args)):
        scope_tree.add_variable(input_names[i], args[i], line)
    for i in range(4, line_node.num_child):
        in_line = getattr(line_node, "children{}".format(i))
        res = analyze_line(in_line) 
    scope_tree.close_scope()

def analyze_function_call(line_node):
    func_name = line_node.children0
    line = func_name.line
    arg_node = line_node.children1
    func_type = scope_tree.type_variable(func_name)
    if func_type==-1:
        error = Error(line, "Function called before defining it.", 'Semantic Analyzer')
    if arg_node.num_child > len(func_type.inputs):
        error = Error(line, "Too many arguments for the function", 'Semantic Analyzer')
    if arg_node.num_child < len(func_type.inputs):
        error = Error(line, "Too few arguments for the function", 'Semantic Analyzer')
    for i in range(arg_node.num_child): 
        match = analyze_expression(getattr(arg_node, "children{}".format(i)), func_type.inputs[i])
        if not match:
            error = Error(line, "The argument at position {} doesnt matches with the defination of the function".format(i), 'Semantic Analyzer')
def analyze_if(line_node):
    cond = line_node.children1
    match = analyze_expression(cond,bool)
    if match:
        scope_tree.create_scope()
        for i in range(2,line_node.num_child):
            line = getattr(line_node, "children{}".format(i))
            if isinstance(line,magar_temp):
                scope_tree.close_scope()
                scope_tree.create_scope()
                if (line.num_child==0):
                    continue
                else:
                    cond = line.children1
                    match2 = analyze_expression(cond,bool)
                    if match2:
                        for i in range(2,line.num_child):
                            line2 = getattr(line, "children{}".format(i))
                            analyze_line(line2)
                        scope_tree.close_scope()
                    else:
                        error_msg = "Type of expression given as elseif condition is not of boolean type '{}'.".format(cond)
                        error = Error(line.children0.line, error_msg, 'Semantic Analyzer')
            elif isinstance(line, nahitoh_temp):
                scope_tree.create_scope()
                for i in range(1,line.num_child):
                    line3 = getattr(line, "children{}".format(i))
                    analyze_line(line3)
                scope_tree.close_scope()
            else:
                res = analyze_line(line)
    else:
        error_msg = "Type of expression given as if condition is not of boolean type '{}'.".format(cond)
        error = Error(line_node.children0.line, error_msg, 'Semantic Analyzer')


def analyze_assignment():
    return True

def analyze_line(line_node):
    if isinstance(line_node, declaration):
        res = analyze_declare(line_node)
    elif isinstance(line_node, assignment):
        res = analyze_assignment(line_node)
    elif isinstance(line_node, while_loop):
        res = analyze_while(line_node)
    elif isinstance(line_node, function):
        res = analyze_function(line_node)
    elif isinstance(line_node, function_call):
        res = analyze_function_call(line_node)
    if isinstance(line_node, assignment):
        res = analyze_assignment(line_node)
    if isinstance(line_node, while_loop):
        res = analyze_while(line_node)
    if isinstance(line_node, for_loop):
        res = analyze_for(line_node)
    if isinstance(line_node, ifelse):
        res = analyze_if(line_node)

def analyze_program(node):
    for i in range(node.num_child):
        line = getattr(node, "children{}".format(i))
        res = analyze_line(line)