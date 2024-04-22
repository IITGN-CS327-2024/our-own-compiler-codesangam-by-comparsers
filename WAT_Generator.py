from ast_classes import *
from symbol_table import *
from error_handling import *

def write_local_vars(node, file, indent, input_names):
    for key in list(node.table.keys()):
        if key in input_names:
            continue
        file.write("\t"*indent + "(local ${} i32)\n".format(key))
    for child in node.children:
        write_local_vars(child, file, indent, input_names)

def find_in_e(node):
    if isinstance(node,e3):
        return True
    elif isinstance(node,e4):
        return True
    elif isinstance(node,e8):
        return True
    elif isinstance(node,e9):
        return True
    return False

def convert_expression(node, indent, file):
    # print(node)
    enode = find_in_e(node)
    if enode==True:
        if isinstance(node,e3):
            var1 = node.children0
            enode = find_in_e(var1)
            if enode==True:
                convert_expression(var1,indent,file)
            else:
                if var1.type=="IDENTIFIER":
                    file.write("\t"*indent+"local.get ${}".format(var1)+"\n")
                else:
                    file.write("\t"*indent +"i32.const {}".format(var1)+"\n")
            var2 = node.children2
            enode = find_in_e(var2)
            if enode==True:
                convert_expression(var2,indent,file)
            else:
                if var2.type=="IDENTIFIER":
                    file.write("\t"*indent+"local.get ${}".format(var2)+"\n")
                else:
                    file.write("\t"*indent +"i32.const {}".format(var2)+"\n")
            if node.children1.type=="PLUS":
                file.write("\t"*indent+"i32.add\n")
            elif node.children1.type=="MINUS":
                file.write("\t"*indent+"i32.sub\n")
        elif isinstance(node,e4):
            var1= node.children0
            enode = find_in_e(var1)
            if enode==True:
                convert_expression(var1,indent,file)
            else:
                if var1.type=="IDENTIFIER":
                    file.write("\t"*indent+"local.get ${}".format(var1)+"\n")
                else:
                    file.write("\t"*indent +"i32.const {}".format(var1)+"\n")
            var2 = node.children2
            enode = find_in_e(var2)
            if enode==True:
                convert_expression(var2,indent,file)
            else:
                if var2.type=="IDENTIFIER":
                    file.write("\t"*indent+"local.get ${}".format(var2)+"\n")
                else:
                    file.write("\t"*indent +"i32.const {}".format(var2)+"\n")
            if isinstance(node.children1,ob):
                if node.children1.children0.type=="MULT":
                    file.write("\t"*indent+"i32.mul\n")
                elif node.children1.children0.type=="DIV":
                    file.write("\t"*indent+"i32.div_s\n")
                elif node.children1.children0.type=="MODULO":
                    file.write("\t"*indent+"i32.rem_s\n")
        elif isinstance(node,e8):
            var1 = node.children0
            enode = find_in_e(var1)
            if enode==True:
                convert_expression(var1,indent,file)
            else:
                if var1.type=="IDENTIFIER":
                    file.write("\t"*indent+"local.get ${}".format(var1)+"\n")
                else:
                    file.write("\t"*indent +"i32.const {}".format(var1)+"\n")
            op = node.children1.children0
            if op.type=="PLUS_PLUS":
                file.write("\t"*indent +"i32.const 1\n")
                file.write("\t"*indent+"i32.add\n")
        elif isinstance(node,e9):
            # print(node.children0,"hirva")
            if node.num_child==1:
                convert_expression(node.children0,indent,file)
            elif node.num_child==2:
                if node.children0.type=="MINUS":
                    convert_expression(node.children1,indent,file)
                    file.write("\t"*indent+"i32.const -1\n")
                    file.write("\t"*indent+"i32.mul\n")
    elif isinstance(node,function_call):
        # print("hi")
        convert_func_call(node,indent,file)
    elif node.type=="NUMBER":
        num_i = node
        file.write("\t"*indent+"i32.const {}".format(num_i)+"\n")
    elif node.type=="IDENTIFIER":
        id = node
        file.write("\t"*indent+"local.get ${}".format(id)+"\n")

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
    write_local_vars(func_node, file, indent, func_type.input_names)
    for i in range(4, line_node.num_child):
        in_line = getattr(line_node, "children{}".format(i))
        convert_line(in_line, scope_tree, file, indent, func_num)
    file.write("\t"*(indent-1) + ")\n")

def convert_assignment(line_node, indent, file):
    var_name = line_node.children0
    # print(line_node.children2.children0)
    if line_node.children1.children0 == '=':
        expression_value = convert_expression(line_node.children2.children0, indent, file)
    elif line_node.children1.children0 =='+=':
        file.write("\t"*indent + "local.get ${}\n".format(var_name))
        expression_value = convert_expression(line_node.children2.children0, indent, file)
        file.write("\t"*indent+"i32.add\n")
    elif line_node.children1.children0 == '-=':
        file.write("\t"*indent + "local.get ${}\n".format(var_name))
        expression_value = convert_expression(line_node.children2.children0, indent, file)
        file.write("\t"*indent+"i32.sub\n")
    elif line_node.children1.children0 == '*=':
        file.write("\t"*indent + "local.get ${}\n".format(var_name))
        expression_value = convert_expression(line_node.children2.children0, indent, file)
        file.write("\t"*indent+"i32.mul\n")
    elif line_node.children1.children0 == '/=':
        file.write("\t"*indent + "local.get ${}\n".format(var_name))
        expression_value = convert_expression(line_node.children2.children0, indent, file)
        file.write("\t"*indent+"i32.div_s\n")
    file.write("\t"*indent + "local.set ${}\n".format(var_name))

def convert_declaration(line_node, indent, file):
    var_name = line_node.children1
    expression_value = convert_expression(line_node.children3.children0, indent, file)
    file.write("\t"*indent + "local.set ${}\n".format(var_name))

def convert_return(line_node, indent, file):
    expression_value = convert_expression(line_node.children1.children0, indent, file)
    file.write("\t"*indent+"return\n")

def convert_func_call(line_node, indent, file):
    # print("hir")
    args = line_node.children1
    for i in range(args.num_child):
        arg = getattr(args, "children{}".format(i))
        # print(arg)
        convert_expression(arg.children0, indent, file)
    file.write("\t"*indent + "call ${}\n".format(line_node.children0))

def convert_ifelse(line_node, indent, scope_tree, file, func_num):
    expr = line_node.children1.children0.children0.children0
    convert_expression(expr,indent,file)
    expr = line_node.children1.children0.children0.children2
    convert_expression(expr,indent,file)
    comp = line_node.children1.children0.children0.children1
    if comp.type=="LESS_EQUAL":
        file.write("\t"*indent +"i32.le_s"+"\n")
    elif comp.type=="GREATER_EQUAL":
        file.write("\t"*indent +"i32.ge_s"+"\n") 
    elif comp.type=="GREATER":
        file.write("\t"*indent +"i32.gt_s"+"\n")
    elif comp.type=="LESS":
        file.write("\t"*indent +"i32.lt_s"+"\n")
    elif comp.type=="BANG_EQUAL":
        file.write("\t"*indent +"i32.ne"+"\n")
    elif comp.type=="EQUAL_EQUAL":
        file.write("\t"*indent +"i32.eq"+"\n")  
    file.write("\t"*indent + "(if \n")
    indent+=1
    file.write("\t"*indent + "(then \n")
    j = line_node.num_child-1
    for i in range(2,line_node.num_child):
        line = getattr(line_node, "children{}".format(i))
        if isinstance(line , magar_temp):
            break
        else:
            convert_line(line, scope_tree, file, indent, func_num)
    line = getattr(line_node, "children{}".format(line_node.num_child - 1))
    indent-=1
    file.write("\t"*indent + ")\n")
    if (line.num_child!=0):
        indent+=1
        file.write("\t"*indent + "(else\n")
        for i in range(1,line.num_child):
            line_ = getattr(line, "children{}".format(i))
            indent+=1
            convert_line(line_, scope_tree, file, indent, func_num)
            indent-=1
        file.write("\t"*indent + ")\n")
        indent-=1
    file.write("\t"*indent + ")\n")

def convert_loop(node, indent, file, scope_tree, func_num):
    var_i = node.children1.children1
    convert_expression(node.children1.children3.children0, indent, file)
    file.write("\t"*indent +"local.set ${}".format(var_i)+"\n")
    file.write("\t"*indent + "loop\n")
    indent+=1
    update = node.children3.children0.children0
    convert_expression(update, indent, file)
    file.write("\t"*indent +"local.set ${}".format(var_i)+"\n")
    # file.write("\t"*indent +"call $log"+"\n")
    for i in range(4, node.num_child):
        in_line = getattr(node, "children{}".format(i))
        convert_line(in_line, scope_tree, file, indent, func_num)
    var_c = node.children2.children0.children0.children0
    file.write("\t"*indent +"local.get ${}".format(var_i)+"\n")
    expr = node.children2.children0.children0.children2
    convert_expression(expr,indent,file)
    comp = node.children2.children0.children0.children1
    if comp.type=="LESS_EQUAL":
        file.write("\t"*indent +"i32.le_s"+"\n")
    elif comp.type=="GREATER_EQUAL":
        file.write("\t"*indent +"i32.ge_s"+"\n") 
    elif comp.type=="GREATER":
        file.write("\t"*indent +"i32.gt_s"+"\n")
    elif comp.type=="LESS":
        file.write("\t"*indent +"i32.lt_s"+"\n")
    elif comp.type=="BANG_EQUAL":
        file.write("\t"*indent +"i32.ne"+"\n")
    elif comp.type=="EQUAL_EQUAL":
        file.write("\t"*indent +"i32.eq"+"\n")   
    file.write("\t"*indent + "br_if 0"+"\n")
    file.write("\t"*indent + "end"+"\n")

def convert_line(line_node, scope_tree, file, indent, func_num):
    if isinstance(line_node, assignment):
        convert_assignment(line_node, indent, file)
    elif isinstance(line_node, declaration):
        convert_declaration(line_node, indent, file)
    elif isinstance(line_node, function_call):
        convert_func_call(line_node, indent, file)
    elif isinstance(line_node, function):
        convert_function(line_node, scope_tree, file, indent, func_num)
        func_num+=1
    elif isinstance(line_node, return_func):
        convert_return (line_node, indent, file)
    elif isinstance(line_node, for_loop):
        convert_loop(line_node, indent, file, scope_tree, func_num)
    elif isinstance(line_node, ifelse):
        convert_ifelse(line_node, indent, scope_tree, file, func_num)

def convert_program(node, scope_tree, file_name):
    func_num = 0
    with open('WAT_Code/{}.wat'.format(file_name), 'w') as file:
        file.write("(module\n")
        file.write(
'''\t(memory (export "memory") 1)
    (func $store (param $value i32) (param $address i32)
        ;; Store the value at the specified address in memory
        (i32.store (local.get $address) (local.get $value))
    )
    (func $load (param $address i32) (result i32)
        (i32.load
        (local.get $address)  ;; Load value from specified address
        )
    )\n''')
        for i in range(node.num_child):
            line = getattr(node, "children{}".format(i))
            convert_line(line, scope_tree, file, 1, func_num)
        file.write(")")

