import sys

class Error:
    def __init__(self, line, msg, error_by):
        self.line = line
        self.msg = msg
        self.error_by = error_by
        self.print_error()
        if self.error_by!='Lexer':
            sys.exit(0)

    def print_error(self):
        print()
        print("Error at [ line: {} ] by {}".format(self.line, self.error_by))
        print("Description:", self.msg)
