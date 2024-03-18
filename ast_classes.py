class ASTNodeMeta(type):
    def __new__(cls, name, bases, dct):
        if name != 'ASTNode':
            def repr_func(self):
                return name
            dct['__repr__'] = repr_func
        return super().__new__(cls, name, bases, dct)

class ASTNode(metaclass=ASTNodeMeta):
    """Abstract b"""
    pass

class start(ASTNode):
    def __init__(self, values):
        values = values[:-1]
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)

class line_temp(ASTNode):
    def __init__(self, values):
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)

class line(ASTNode):
    def __init__(self, values):
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)

class statement(ASTNode):
    def __init__(self, values):
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)
    
class assignment(ASTNode):
    def __init__(self, values):
        if len(values)==6:
            indices_to_remove = [1, 3]
            values = [values[i] for i in range(len(values)) if i not in indices_to_remove]
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)
    
class declaration(ASTNode):
    def __init__(self, values):
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)
    
class all_equal(ASTNode):
    def __init__(self, values):
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)

class expression(ASTNode):
    def __init__(self, values):
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)

class e(ASTNode):
    def __init__(self, values):
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)

class e1(ASTNode):
    def __init__(self, values):
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)

class e2(ASTNode):
    def __init__(self, values):
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)

class e3(ASTNode):
    def __init__(self, values):
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value) 
    
class e4(ASTNode):
    def __init__(self, values):
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)
    
class e5(ASTNode):
    def __init__(self, values):
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)
    
class e6(ASTNode):
    def __init__(self, values):
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)
    
class e7(ASTNode):
    def __init__(self, values):
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)
    
class e8(ASTNode):
    def __init__(self, values):
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)
    
class e9(ASTNode):
    def __init__(self, values):
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)

class datatype(ASTNode):
    def __init__(self, values):
        if len(values)==6:
            values = values[:3] + values[4:]
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)

class comparators(ASTNode):
    def __init__(self, children):
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class access_temp(ASTNode):
    def __init__(self, children):
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class num_temp(ASTNode):
    def __init__(self, children):
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class els(ASTNode):
    def __init__(self, children):
        children = [children[1]]
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class ob(ASTNode):
    def __init__(self, children):
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class ol(ASTNode):
    def __init__(self, children):
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class ou(ASTNode):
    def __init__(self, children):
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class obi(ASTNode):
    def __init__(self, children):
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class function_call(ASTNode):
    def __init__(self, children):
        children = children[::2]
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class print_(ASTNode):
    def __init__(self, children):
        children = children[::2]
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class print_body(ASTNode):
    def __init__(self, children):
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class print_temp(ASTNode):
    def __init__(self, children):
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class input_(ASTNode):
    def __init__(self, children):
        children = [children[2], children[-2]]
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class let(ASTNode):
    def __init__(self, children):
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class ifelse(ASTNode):
    def __init__(self, values):
        indices_to_remove = [1, 3, 4, 5, 6]
        values = [values[i] for i in range(len(values)) if i not in indices_to_remove]
        values = values[:-4] + values[-2:]
        for i, child in enumerate(values):
            setattr(self, f'value{i}', child)

class magar_temp(ASTNode):
    def __init__(self, values):
        indices_to_remove = [1, 3, 4, 5, 6]
        values = [values[i] for i in range(len(values)) if i not in indices_to_remove]
        values = values[:-3] + values[-1:]
        for i, child in enumerate(values):
            setattr(self, f'value{i}', child)

class nahitoh_temp(ASTNode):
    def __init__(self, values):
        indices_to_remove = [1, 2, 3]
        values = [values[i] for i in range(len(values)) if i not in indices_to_remove]
        values = values[:-1]
        for i, child in enumerate(values):
            setattr(self, f'value{i}', child)

class update_temp(ASTNode):
    def __init__(self, children):
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class update(ASTNode):
    def __init__(self, children):
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class condition(ASTNode):
    def __init__(self, children):
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class arguments(ASTNode):
    def __init__(self, values):
        values = values[:1]+values[2:]
        for i, child in enumerate(values):
            setattr(self, f'value{i}', child)

class args(ASTNode):
    def __init__(self, children):
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class return_func(ASTNode):
    def __init__(self, children):
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class function(ASTNode):
    def __init__(self, values):
        indices_to_remove = [3, 5, 6, 7, 8]
        values = [values[i] for i in range(len(values)) if i not in indices_to_remove]
        values = values[:-1]
        for i, child in enumerate(values):
            setattr(self, f'value{i}', child)

class function_call_arguments(ASTNode):
    def __init__(self, children):
        children = children[::2]
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class ed(ASTNode):
    def __init__(self, children):
        children = [children[1]]
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class dict_body(ASTNode):
    def __init__(self, children):
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class dict_element(ASTNode):
    def __init__(self, children):
        children = [children[0], children[2]]
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class key(ASTNode):
    def __init__(self, children):
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class value(ASTNode):
    def __init__(self, children):
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class list_body(ASTNode):
    def __init__(self, children):
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class list_element(ASTNode):
    def __init__(self, children):
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class et(ASTNode):
    def __init__(self, children):
        children = [children[1]]
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class access_temp(ASTNode):
    def __init__(self, children):
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class a_temp(ASTNode):
    def __init__(self, children):
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class num_temp(ASTNode):
    def __init__(self, children):
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class n_temp(ASTNode):
    def __init__(self, children):
        for i, child in enumerate(children):
            setattr(self, f'value{i}', child)

class closure(ASTNode):
    def __init__(self, values):
        indices_to_remove = [5, 7, 8, 9, 10]
        values = [values[i] for i in range(len(values)) if i not in indices_to_remove]
        values = values[:-1]
        for i, child in enumerate(values):
            setattr(self, f'value{i}', child)

class tryelse(ASTNode):
    def __init__(self, values):
        indices_to_remove = [1, 2, 3]
        values = [values[i] for i in range(len(values)) if i not in indices_to_remove]
        values = values[:-4] + values[-2:]
        for i, child in enumerate(values):
            setattr(self, f'value{i}', child)

class varna(ASTNode):
    def __init__(self, values):
        indices_to_remove = [1, 2, 3]
        values = [values[i] for i in range(len(values)) if i not in indices_to_remove]
        values = values[:-1]
        for i, child in enumerate(values):
            setattr(self, f'value{i}', child)

class for_loop(ASTNode):
    def __init__(self, values):
        indices_to_remove = [1, 3, 5, 7, 8, 9, 10]
        values = [values[i] for i in range(len(values)) if i not in indices_to_remove]
        values = values[:-2] + values[-1:]
        for i, child in enumerate(values):
            setattr(self, f'value{i}', child)

class while_loop(ASTNode):
    def __init__(self, values):
        indices_to_remove = [1, 3, 4, 5, 6]
        values = [values[i] for i in range(len(values)) if i not in indices_to_remove]
        values = values[:-2] + values[-1:]
        for i, child in enumerate(values):
            setattr(self, f'value{i}', child)
