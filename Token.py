class Token:
    def __init__(self, content, type, parent_type):
        self.content = content
        self.type = type
        self.parent_type = parent_type
    
    def print(self):
        #Print the information of the token in a particular format.
        return 