from Line import *
import sys

class Lexer_:

    def __init__(self, file_path, line_start = 0, line_current = 0):
        self.file_path = file_path
        self.lines = []
        self.line_start = 0
        self.line_current = 0
        self.has_error = False
    
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
        previous_indent = 0
        depth_indent = 0
        for single_line in file_lines:
            if len(single_line)==0:
                line_number+=1
                continue
            if all(char.isspace() or char=='\t' for char in single_line):
                line_number+=1
                continue
            
            line = Line(line_number, single_line, comment_continue, True)
            if line.indentation>previous_indent:
                new_token = Token("", TokenClass.START_INDENT, "Extras")
                line.token_list.insert(0, new_token)
                depth_indent+=1
            if line.indentation<previous_indent:
                new_token = Token("", TokenClass.END_INDENT, "Extras")
                line.token_list.insert(0, new_token)
                depth_indent-=1
            previous_indent = line.indentation
            comment_continue = line.comment_on
            if not comment_continue:
                line.add_token("", TokenClass.NEW_LINE, "Extras")
            line_number+=1
            if line.has_error:
                print("Error at [line", line.line_number, "]")
                print("ERROR:", line.error)
                self.has_error = True
                break
            self.lines.append(line)
        line = Line(line_number, "", comment_continue, False)
        if comment_continue:
            self.has_error = True
            line.error = "The multi line comment has not been ended."
            line.has_error = True
            print("Error at [line", line.line_number, "]")
            print("ERROR:", line.error)
        for i in range(depth_indent):
            line.add_token("", TokenClass.END_INDENT, "Extras")
        line.add_token("", TokenClass.EOF, "Extras")
        self.lines.append(line)

    def print_lexemes(self):
        for line in self.lines:
            line.print_lexemes()

if __name__ == "__main__":
    file_path = sys.argv[1]
    lexer = Lexer_(file_path)
    lexer.classify_lexemes()
    lexer.print_lexemes()

            
