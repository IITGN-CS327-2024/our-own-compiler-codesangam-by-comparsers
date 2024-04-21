from ast_classes import *
from symbol_table import *
from error_handling import *

last_scope_index = -1

def convert_function(line_node, scope_tree, file, indent):
    file.write("\t"*indent + '(func (export "{}")\n'.format(line_node.children2))
    indent+=1
    func_type = scope_tree.root.table[line_node.children2]
    num_inputs = len(func_type.inputs)
    for i in range(num_inputs):
        file.write("\t"*indent + "(params ${} i32)\n".format(func_type.input_names[i]))
    if scope_tree.root.has_return:
        file.write("\t"*indent + "(return i32)\n")
    last_scope_index = last_scope_index + 1
    function_node = scope_tree.root.children[last_scope_index]
    file.write("\t"*(indent-1) + ")\n")

def convert_line(line_node, scope_tree, file, indent):
    if isinstance(line_node, assignment):
        convert_assignment(line_node, scope_tree, indent)
    elif isinstance(line_node, function):
        convert_function(line_node, scope_tree, file, indent)
    return

def convert_program(node, scope_tree, file_name):
    with open('WAT_Code/{}.wat'.format(file_name), 'w') as file:
        file.write("(module\n")
        for i in range(node.num_child):
            line = getattr(node, "children{}".format(i))
            convert_line(line, scope_tree, file, 1)
        file.write(")")

