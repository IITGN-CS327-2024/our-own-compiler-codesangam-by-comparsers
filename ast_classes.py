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
    def __init__(self, children):
        self.num_child = 0
        children = children[:-1]
        child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'children{i}', child)

class line_temp(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        child = 0
        for i, child in enumerate(children):
            setattr(self, f'children{i}', child)

class line(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'children{i}', child)

class statement(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'children{i}', child)
    
class assignment(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        if len(children)==6:
            self.num_child+=1
            indices_to_remove = [1, 3]
            children = [children[i] for i in range(len(children)) if i not in indices_to_remove]
        for i, child in enumerate(children):
            setattr(self, f'children{i}', child)
    
class declaration(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'children{i}', child)
    
class all_equal(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'children{i}', child)

class expression(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'children{i}', child)

class e(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'children{i}', child)

class e1(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'children{i}', child)

class e2(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'children{i}', child)

class e3(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'children{i}', child) 
    
class e4(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'children{i}', child)
    
class e5(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'children{i}', child)
    
class e6(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'children{i}', child)
    
class e7(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'children{i}', child)
    
class e8(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'children{i}', child)
    
class e9(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'children{i}', child)

class datatype(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        if len(children)==6:
            self.num_child+=1
            children = children[:3] + children[4:]
        for i, child in enumerate(children):
            setattr(self, f'children{i}', child)

class comparators(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class access_temp(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class num_temp(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class els(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        children = [children[1]]
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class ob(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class ol(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class ou(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class obi(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class function_call(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        children = children[::2]
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class print_(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        children = children[::2]
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class print_body(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class print_temp(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class input_(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        children = [children[2], children[-2]]
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class let(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class ifelse(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        indices_to_remove = [1, 3, 4, 5, 6]
        chilself.num_child+=1
        dren = [children[i] for i in range(len(children)) if i not in indices_to_remove]
        children = children[:-4] + children[-2:]
        for i, child in enumerate(children):
            setattr(self, f'child{i}', child)

class magar_temp(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        indices_to_remove = [1, 3, 4, 5, 6]
        chilself.num_child+=1
        dren = [children[i] for i in range(len(children)) if i not in indices_to_remove]
        children = children[:-3] + children[-1:]
        for i, child in enumerate(children):
            setattr(self, f'child{i}', child)

class nahitoh_temp(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        indices_to_remove = [1, 2, 3]
        chilself.num_child+=1
        dren = [children[i] for i in range(len(children)) if i not in indices_to_remove]
        children = children[:-1]
        for i, child in enumerate(children):
            setattr(self, f'child{i}', child)

class update_temp(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class update(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class condition(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class arguments(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        children = children[:1]+children[2:]
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class args(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class return_func(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class function(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        indices_to_remove = [3, 5, 6, 7, 8]
        chilself.num_child+=1
        dren = [children[i] for i in range(len(children)) if i not in indices_to_remove]
        children = children[:-1]
        for i, child in enumerate(children):
            setattr(self, f'child{i}', child)

class function_call_arguments(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        children = children[::2]
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class ed(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        children = [children[1]]
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class dict_body(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class dict_element(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        children = [children[0], children[2]]
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class key(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class child(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class list_body(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class list_element(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class et(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        children = [children[1]]
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class access_temp(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class a_temp(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class num_temp(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class n_temp(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class closure(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        indices_to_remove = [5, 7, 8, 9, 10]
        chilself.num_child+=1
        dren = [children[i] for i in range(len(children)) if i not in indices_to_remove]
        children = children[:-1]
        for i, child in enumerate(children):
            setattr(self, f'child{i}', child)

class tryelse(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        indices_to_remove = [1, 2, 3]
        chilself.num_child+=1
        dren = [children[i] for i in range(len(children)) if i not in indices_to_remove]
        children = children[:-4] + children[-2:]
        for i, child in enumerate(children):
            setattr(self, f'child{i}', child)

class varna(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        indices_to_remove = [1, 2, 3]
        children = [children[i] for i in range(len(children)) if i not in indices_to_remove]
        children = children[:-1]
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class for_loop(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        indices_to_remove = [1, 3, 5, 7, 8, 9, 10]
        children = [children[i] for i in range(len(children)) if i not in indices_to_remove]
        children = children[:-2] + children[-1:]
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)

class while_loop(ASTNode):
    def __init__(self, children):
        self.num_child = 0
        indices_to_remove = [1, 3, 4, 5, 6]
        children = [children[i] for i in range(len(children)) if i not in indices_to_remove]
        children = children[:-2] + children[-1:]
        for i, child in enumerate(children):
            self.num_child+=1
            setattr(self, f'child{i}', child)
