from error_handling import *

class Scope_tree_node:
    def __init__(self, parent):
        self.table = {}
        self.parent_node = parent
        self.children = []

class Scope_tree:
    def __init__(self):
        self.root = Scope_tree_node(None)
        self.current_scope = self.root

    def create_scope(self):
        new_scope = Scope_tree_node(self.current_scope)
        self.current_scope.children.append(new_scope)
        self.current_scope = new_scope

    def close_scope(self):
        self.current_scope = self.current_scope.parent_node

    def type_variable(self, var_name):
        temp = self.current_scope
        while temp.parent_node!=None:
            if var_name in list(temp.table.keys()):
                return temp.table[var_name]
            temp = temp.parent_node
        if var_name in list(temp.table.keys()):
            return temp.table[var_name]
        else:
            return -1
        
    def add_variable(self, var_name, var_type, line):
        res = self.type_variable(var_name)
        if var_name in list(self.current_scope.table.keys()):
            error_msg = "The variable is already defined in the current scope and redefination is not allowed"
            error = Error(line, error_msg, 'Semantic Analyzer')
            return
        self.current_scope.table[var_name] = var_type
        return

class list_type:
    def __init__(self, dim, element_type):
        self.dim = dim
        self.element_type = element_type

class tup_type:
    def __init__(self, dim, element_type):
        self.dim = dim
        self.element_type = element_type

class dict_type:
    def __init__(self, key_type, val_type):
        self.key_type = key_type
        self.val_type = val_type

class func_type:
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs
