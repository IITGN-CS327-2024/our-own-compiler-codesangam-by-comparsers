from Line import *

class Lexer:

    def __init__(self, file_path, lines, line_start = 0, line_current = 0):
        self.file_path = file_path
        self.lines = []
        self.line_start = 0
        self.line_current = 0
    
    def classify_lexemes(self):
        try:
            with open(self.file_path, 'r') as file:
                file_contents = file.read()
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
        except Exception as e: 
            print(f"An error occurred: {e}")

        file_lines = file_contents.splitlines()
        result = []
        line_number = 1
        comment_continue = False
        for single_line in file_lines:
            if len(single_line)==0:
                line_number+=1
                continue
            if all(char.isspace() or char=='\t' for char in single_line):
                line_numer+=1
                continue
            
            line = Line(line_number, single_line, comment_continue)
            comment_continue = line.comment_on
            line_number+=1
            if line.error != "":
                print("ERROR:", line.error)
                break
            result.append(line)

    def print_lexemes(self):
        for line in self.lines:
            line.print_lexemes()



            
