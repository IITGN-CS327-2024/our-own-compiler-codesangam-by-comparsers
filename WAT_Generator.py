from ast_classes import *
from symbol_table import *
from error_handling import *

# def write_local_vars(node, file, indent):

def find_in_e(node):
    if isinstance(node,e3):
        return True
    elif isinstance(node,e4):
        return True
    return False

def convert_expression(node, indent, file):
    enode = find_in_e(node.children0)
    if enode==True:
        if isinstance(node.children0,e3):
            node = node.children0
            var1 = node.children0
            file.write("\t"*indent+"local.get ${}".format(var1)+"\n")
            var2 = node.children2
            file.write("\t"*indent+"local.get ${}".format(var2)+"\n")
            if node.children1.type=="PLUS":
                file.write("\t"*indent+"i32.add\n")
            elif node.children1.type=="MINUS":
                file.write("\t"*indent+"i32.sub\n")
        elif isinstance(node.children0,e4):
            node = node.children0
            var1= node.children0
            file.write("\t"*indent+"local.get ${}".format(var1)+"\n")
            var2 = node.children2
            file.write("\t"*indent+"local.get ${}".format(var2)+"\n")
            if isinstance(node.children1,ob):
                if node.children1.children0.type=="MULT":
                    file.write("\t"*indent+"i32.mul\n")
                elif node.children1.children0.type=="DIV":
                    file.write("\t"*indent+"i32.div_u\n")
                elif node.children1.children0.type=="DIV":
                    file.write("\t"*indent+"i32.rem\n")

def convert_function(line_node, scope_tree, file, indent, func_num):
    file.write("\t"*indent + '(func ${} (export "{}")\n'.format(line_node.children2, line_node.children2))
    indent+=1
    func_type = scope_tree.root.table[line_node.children2]
    num_inputs = len(func_type.inputs)
    for i in range(num_inputs):
        file.write("\t"*indent + "(param ${} i32)\n".format(func_type.input_names[i]))
    if func_type.outputs.value!='void':
        file.write("\t"*indent + "(result i32)\n")
    func_node = scope_tree.root.children[func_num]
    # write_local_vars(func_node, file, indent)
    for i in range(4, line_node.num_child):
        in_line = getattr(line_node, "children{}".format(i))
        convert_line(in_line, scope_tree, file, indent, func_num)
    file.write("\t"*(indent-1) + ")\n")

def convert_assignment(line_node, indent, file):
    expression_value = convert_expression(line_node.children2, indent, file)
    var_name = line_node.children0
    if line_node.children1 == '=':
        file.write("\t"*indent + "local.set ${}".format(var_name))

def convert_declaration(line_node, indent, file):
    expression_value = convert_expression(line_node.children3, indent, file)
    var_name = line_node.children1
    if line_node.children2 == '=':
        file.write("\t"*indent + "local.set ${}".format(var_name))

def convert_return(line_node, indent, file):
    expression_value = convert_expression(line_node.children1, indent, file)
    file.write("\t"*indent+"return\n")

def convert_loop(line_node, indent, file):
    file.write("\t"*indent + "loop")

    file.write("\t"*indent + "end")

def convert_line(line_node, scope_tree, file, indent, func_num):
    if isinstance(line_node, assignment):
        convert_assignment(line_node, indent, file)
    elif isinstance(line_node, declaration):
        convert_declaration(line_node, indent, file)
    elif isinstance(line_node, function):
        convert_function(line_node, scope_tree, file, indent, func_num)
        func_num+=1
    elif isinstance(line_node, return_func):
        convert_return (line_node, indent, file)

def convert_program(node, scope_tree, file_name):
    func_num = 0
    with open('WAT_Code/{}.wat'.format(file_name), 'w') as file:
        file.write("(module\n")
        for i in range(node.num_child):
            line = getattr(node, "children{}".format(i))
            convert_line(line, scope_tree, file, 1, func_num)
        file.write(")")

