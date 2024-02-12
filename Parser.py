from Lexer import *
from Line import *

class Parser:

    def __init__(self,file_path):
        self.file_path = file_path
        self.lexer = Lexer(file_path)

       

if __name__ == "__main__":
    file_path = sys.argv[1]
    parser = Parser(file_path)
    parser.lexer.classify_lexemes()
    parser.lexer.print_tokens()
