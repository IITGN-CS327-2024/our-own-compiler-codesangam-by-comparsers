class Token:
    def __init__(self, content, type, parent_type):
        self.content = content
        self.type = type
        self.parent_type = parent_type