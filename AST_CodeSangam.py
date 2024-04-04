import ast_classes
import lark  

def remove_none(lst):
    flat_list = []
    for sublist in lst:
        if isinstance(sublist, list):
            flat_list.extend(remove_none(sublist))

        elif(sublist is not None):
            flat_list.append(sublist)

    return flat_list

class OurTransformer(lark.Transformer):

    """We write a transformer for each node in the parse tree
    (concrete syntax) by writing a method with the same name.
    Non-terminal symbols are passed a list of their children
    after transformation, which proceeds from leaves to root
    recursively. Terminal symbols (like NUMBER) are instead
    passed a lark.Token structure.
    """

    def start(self, children):
        children = remove_none(children)
        return ast_classes.start(children)
    
    def line_temp(self, children):
        children = remove_none(children)
        if len(children)==0:
            return None
        else:
            return children
    
    def line(self, children):
        children = remove_none(children)
        return children[0]
    
    def statement(self, children):
        children = remove_none(children)
        return children
    
    def assignment(self, children):
        children = remove_none(children)
        if len(children)==4:
            return ast_classes.declaration(children)
        else:
            return ast_classes.assignment(children)
        
    def all_equal(self, children):
        children = remove_none(children)
        return children
    
    def all_e(self, children):
        children = remove_none(children)
        return ast_classes.expression(children)
    
    def e(self, children):
        children = remove_none(children)
        return children
    
    def e1(self, children):
        children = remove_none(children)
        if len(children)!=1:
            return ast_classes.e1(children)
        return children
    
    def e2(self, children):
        children = remove_none(children)
        if len(children)!=1:
            return ast_classes.e2(children)
        return children
    
    def e3(self, children):
        children = remove_none(children)
        if len(children)!=1:
            return ast_classes.e3(children)
        return children
    
    def e4(self, children):
        children = remove_none(children)
        if len(children)!=1:
            return ast_classes.e4(children)
        return children
    
    def e5(self, children):
        children = remove_none(children)
        if len(children)!=1:
            return ast_classes.e5(children)
        return children
    
    def e6(self, children):
        children = remove_none(children)
        if len(children)!=1:
            return ast_classes.e6(children)
        return children
    
    def e7(self, children):
        children = remove_none(children)
        if len(children)!=1:
            return ast_classes.e7(children)
        return children
    
    def e8(self, children):
        children = remove_none(children)
        if len(children)!=1:
            return ast_classes.e8(children)
        return children
    
    def e9(self, children):
        children = remove_none(children)
        newchildren = []
        if len(children)!=1:
            for child in children:
                if (child!="." and child!="(" and child!=")" and child!="[" and child!="]" and child!=","):
                    newchildren.append(child) 
            return ast_classes.e9(newchildren)           
        return children
    
    def data_types(self, children):
        children = remove_none(children)
        return ast_classes.datatype(children)
    
    def comparators(self, children):
        children = remove_none(children)
        return children

    def access_temp(self, children):
        children = remove_none(children)
        return ast_classes.access_temp(children)

    def num_temp(self, children):
        children = remove_none(children)
        return ast_classes.num_temp(children)

    def els(self, children):
        children = remove_none(children)
        return ast_classes.els(children)

    def ob(self, children):
        children = remove_none(children)
        return ast_classes.ob(children)
    
    def ol(self, children):
        children = remove_none(children)
        return ast_classes.ol(children)

    def ou(self, children):
        children = remove_none(children)
        return ast_classes.ou(children)

    def obi(self, children):
        children = remove_none(children)
        return ast_classes.obi(children)
    
    def function_call(self, children):
        children = remove_none(children)
        return ast_classes.function_call(children)

    def print(self, children):
        children = remove_none(children)
        return ast_classes.print_(children)

    def ifelse(self, children):
        children = remove_none(children)
        return ast_classes.ifelse(children)

    def while_loop(self, children):
        children = remove_none(children)
        return ast_classes.while_loop(children)

    def for_loop(self, children):
        children = remove_none(children)
        return ast_classes.for_loop(children)

    def tryelse(self, children):
        children = remove_none(children)
        return ast_classes.tryelse(children)
    
    def varna(self, children):
        children = remove_none(children)
        values = children
        indices_to_remove = [1, 2, 3]
        values = [values[i] for i in range(len(values)) if i not in indices_to_remove]
        values = values[:-1]
        return values

    def function(self, children):
        children = remove_none(children)
        return ast_classes.function(children)

    def closure(self, children):
        children = remove_none(children)
        return ast_classes.closure(children)
    
    def return_(self, children):
        children = remove_none(children)
        return ast_classes.return_(children)
    
    def ed(self, children):
        children = remove_none(children)
        return ast_classes.ed(children)

    def dict_body(self, children):
        children = remove_none(children)
        return ast_classes.dict_body(children)

    def dict_temp(self, children):
        children = remove_none(children)
        if len(children)==0:
            return None
        else:
            children = [children[1]]
            return children

    def dict_element(self, children):
        children = remove_none(children)
        return ast_classes.dict_element(children)

    def key(self, children):
        children = remove_none(children)
        return children

    def value(self, children):
        children = remove_none(children)
        return children
    
    def list_body(self, children):
        children = remove_none(children)
        return ast_classes.list_body(children)

    def list_temp(self, children):
        children = remove_none(children)
        if len(children)==0:
            return None
        else:
            children = [children[1]]
            return children

    def list_element(self, children):
        children = remove_none(children)
        return children
    
    def et(self, children):
        children = remove_none(children)
        return ast_classes.et(children)

    def temp(self, children):
        children = remove_none(children)
        return children

    def access_temp(self, children):
        children = remove_none(children)
        return ast_classes.access_temp(children)

    def a_temp(self, children):
        children = remove_none(children)
        if len(children)==0:
            return None
        else:
            children = [children[1]]
            return children

    def num_temp(self, children):
        children = remove_none(children)
        return ast_classes.num_temp(children)
        
    def n_temp(self, children):
        children = remove_none(children)
        if len(children)==0:
            return None
        else:
            children = [children[1]]
            return children

    def all_equal(self, children):
        children = remove_none(children)
        return ast_classes.all_equal(children)


    def print_body(self, children):
        children = remove_none(children)
        return ast_classes.print_body(children)

    def print_temp(self, children):
        children = remove_none(children)
        if len(children)==0:
            return None
        else:
            children = [children[1:]]
            return children
    
    def input(self, children):
        children = remove_none(children)
        return ast_classes.input_(children)
    
    def let(self, children):
        children = remove_none(children)
        return ast_classes.let(children)
    
    def ifelse(self, children):
        children = remove_none(children)
        return ast_classes.ifelse(children)
    
    def magar_temp(self, children):
        children = remove_none(children)
        return ast_classes.magar_temp(children)
    
    def nahitoh_temp(self, children):
        children = remove_none(children)
        return ast_classes.nahitoh_temp(children)
    
    def update_temp(self, children):
        children = remove_none(children)
        if len(children)==0:
            return None
        else:
            children = [children[1]]
            return children
    
    def update(self, children):
        children = remove_none(children)
        return ast_classes.update(children)
    
    def condition(self, children):
        children = remove_none(children)
        return ast_classes.condition(children)
    
    def arguments(self, children):
        children = remove_none(children)
        return ast_classes.arguments(children)

    def args(self, children):
        children = remove_none(children)
        if len(children)==0:
            return None
        else:
            children = [children[1], children[3]]
            return children
    
    def func_data_types(self, children):
        children = remove_none(children)
        return children

    def return_func(self, children):
        children = remove_none(children)
        return ast_classes.return_func(children)

    def return_type(self, children):
        children = remove_none(children)
        return children
    
    def function_call_arguments(self, children):
        children = remove_none(children)
        return ast_classes.function_call_arguments(children)
    
    def input_args(self, children):
        children = remove_none(children)
        if len(children)==0:
            return None
        else:
            return children
        