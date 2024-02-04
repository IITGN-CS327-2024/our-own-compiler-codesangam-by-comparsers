from Line import *
import sys

class Lexer:

    def __init__(self, file_path, line_start = 0, line_current = 0):
        self.file_path = file_path
        self.lines = []
        self.line_start = 0
        self.line_current = 0
    
    def classify_lexemes(self):
        file_contents = ""
        try:
            with open(self.file_path, 'r', encoding="utf8") as file:
                file_contents = file.read()
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
        except Exception as e: 
            print(f"An error occurred: {e}")

        file_lines = file_contents.splitlines()
        line_number = 1
        comment_continue = False
        for single_line in file_lines:
            if len(single_line)==0:
                line_number+=1
                continue
            if all(char.isspace() or char=='\t' for char in single_line):
                line_number+=1
                continue
            
            line = Line(line_number, single_line, comment_continue)
            comment_continue = line.comment_on
            line_number+=1
            if line.error != "":
                print("Error at line", line.line_number)
                print("ERROR:", line.error)
                break
            self.lines.append(line)

    def print_lexemes(self):
        for line in self.lines:
            if len(line.line_content)==0:
                continue
            if all(char.isspace() or char=='\t' for char in line.line_content):
                continue
            line.print_lexemes()

if __name__ == "__main__":
    file_path = sys.argv[1]
    lexer = Lexer(file_path)
    lexer.classify_lexemes()
    lexer.print_lexemes()

            
