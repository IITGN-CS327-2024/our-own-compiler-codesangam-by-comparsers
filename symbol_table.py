class symbol_table:
    def __init__(self, global_symbol_table):
        self.variables = []
        for entry in global_symbol_table.variables:
            self.variables.append(entry)
            self.variables[-1].scope = False

    def add_entry(self, variable_name, variable_type):
        flag = 0
        for entry in self.variables:
            if entry.variable_name == variable_name and entry.scope==True:
                flag = 1
                # Error
        if flag==0:
            new_entry = noremal_entry(variable_name, variable_type)
            self.variables.append(new_entry)
            
class noremal_entry:
    def __init__(self, variable_name, variable_type):
        self.variable_name = variable_name
        self.variable_type = variable_type
        self.scope = True # True is for local and False is for global

class list_tup_entry:
    def __init__(self, variable_name, variable_type, element_type, dim):
        self.variable_name = variable_name
        self.variable_type = variable_type
        self.element_type = element_type
        self.dimension = dim
        self.scope = True # True is for local and False is for global

class dict_entry:
    def __init__(self, variable_name, variable_type, key_type, val_type, dim):
        self.variable_name = variable_name
        self.variable_type = variable_type
        self.key_type = key_type
        self.val_type = val_type
        self.dimension = dim
        self.scope = True # True is for local and False is for global

class function_entry:
    def __init__(self, variable_name, variable_type, return_type):
        self.variable_name = variable_name
        self.variable_type = variable_type
        self.return_type = return_type
        self.scope = True # True is for local and False is for global