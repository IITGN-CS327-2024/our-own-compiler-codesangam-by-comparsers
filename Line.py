from Token import *
from TokenClass import *

KeyWords = {
    "in": TokenClass.IN,
    "num": TokenClass.NUM,
    "str": TokenClass.STR
}

class Line:
    def __init__(self, line_number, line_content, comment_on, current = 0):
        self.line_number = line_number
        self.line_content = line_content
        self.comment_on = comment_on
        self.token_list = []
        self.current = current
        self.indentation = 0
        self.find_indentation()
        self.length = len(line_content)
        self.error = ""
        self.scan_tokens()
    
    def print_lexemes(self):
        print("line",self.line_number,"indent block",self.indentation,end=": ")
        for token in self.token_list:
            print("<",token.content,",",token.type,",",token.parent_type,">",end=", ")
        print()

    def find_indentation(self):
        char = self.advance()
        while char==' ' or char=='\t':
            if char==' ':
                self.indentation+=1
            else:
                self.indentation+=4
        self.back()

    def is_end(self):
        if self.current>=self.length:
            return True
        else:
            return False

    def advance(self):
        self.current+=1
        return self.line_content[self.current - 1]

    def back(self):
        self.current-=1
        return 
    
    def add_token(self, token_type, parent_type):
        new_token = Token(token_type, parent_type)
        self.token_list.append(new_token)

    def string_handler(self):
        content = '"'
        new_char = self.advance()
        while not self.is_end() and new_char != '"':
            content+=new_char
            new_char = self.advance()
        content += '"'
        if self.is_end():
            self.error = "Expected closing double quotation mark."
            return 
        self.add_token(content, TokenClass.STRING, "String")
        
    def char_handler(self):
        content = "'"
        new_char = self.advance()
        if self.is_end():
            self.error = "Expected closing single quotation mark"
            return 
        content += new_char
        if new_char=="'":
            self.add_token(content, TokenClass.STRING, "String")
        else:
            new_char = self.advance()
            if self.is_end():
                self.error = "Expected closing single quotation mark"
                return 
            if new_char == "'":
                content+=new_char
                self.add_token(content, TokenClass.STRING, "String")
            else:
                self.error = "Expected closing single quotation mark"
                return 
    
    def is_digit(self, char):
        return char >= '0' and char <= '9'
    
    def is_alpha(self, char):
        return  (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z') or char == '_'
    
    def number(self, digit):
        content = digit
        new_char = self.advance()
        while not self.is_end() and self.is_digit(new_char): 
            content+=new_char
            new_char =  self.advance()
        if self.is_end():
            self.add_token(TokenClass.NUMBER, "Number")
        elif new_char==".":
            content+=new_char
            new_char = self.advance()
            while not self.is_end() and self.is_digit(new_char):
                content+=new_char
                new_char = self.advance()
            self.add_token(TokenClass.NUMBER, "Number")
            if not self.is_end():
                self.back()
        else:
            self.add_token(TokenClass.NUMBER, "Number")
            self.back()
    
    def identifier_keyword(self, char):
        new_char = self.advance()
        content = char
        while not self.is_end() and self.is_alpha(new_char):
            content+=new_char
            new_char = self.advance()
        if not self.is_end():
            self.back()
        if content in list(KeyWords.keys()):
            self.add_token(content, TokenClass.KeyWords[content], "Key Words")
        elif content[1]!='_':
            self.add_token(content, TokenClass.IDENTIFIER, "Identifier")
        else:
            self.error = "Any identifier name should not start with and underscore (_)."
    
    def single_line_comment(self):
        char =  self.advance()
        content = ""
        while not self.is_end():
            content+=char
            char = self.advance()
        self.add_token(content, TokenClass.COMMENT, "Comment")

    def multi_line_comment(self):
        char = self.advance()
        content = ""
        while not self.is_end():
            if char=='$':
                if self.advance()=='$':
                    if self.advance()=='$':
                        break
                    else:
                        self.back()
                        self.back()
                else:
                    self.back()
            content+=char
        self.add_token(content, TokenClass.COMMENT, "Comment")
        if not self.is_end():
            self.comment_on = False
            self.add_tokent("$$$", TokenClass.COMMENT_MARK, "Comment Marker")         

                    
    def scan_tokens(self):
        if self.comment_on : 
            self.multi_line_comment()
        while not self.is_end() and self.error=="":
            c = self.advance()
            match c:
                case '(':
                    self.add_token(c, TokenClass.LEFT_PAREN, "Parenthesis")
                case ')':
                    self.add_token(c, TokenClass.RIGHT_PAREN, "Parenthesis")
                case '{':
                    self.add_token(c, TokenClass.LEFT_BRACE, "Parenthesis")
                case '}':
                    self.add_token(c, TokenClass.RIGHT_BRACE, "Parenthesis")
                case '[':
                    self.add_token(c, TokenClass.LEFT_SQUARE, "Parenthesis")
                case ']':
                    self.add_token(c, TokenClass.RIGHT_SQUARE, "Parenthesis")
                case '.':
                    self.add_token(c, TokenClass.DOT, "Punctuation")
                case ',':
                    self.add_token(c, TokenClass.COMMA, "Punctuation")
                case ';':
                    self.add_token(c, TokenClass.SEMI, "Punctuation")
                case ':':
                    self.add_token(c, TokenClass.COLON, "Punctuation")
                case ' ':
                    pass
                case '\t':
                    pass
                case '\n':
                    pass
                case '=':
                    if self.advance()=='=':
                        self.add_token("==", TokenClass.EQUAL_EQUAL, "Conditional Operator")
                    else:
                        self.back()
                        self.add_token(c, TokenClass.EQUAL, "Assignment Operator")
                case '<':
                    if self.token_list[len(self.token_list)-1].parent_type == "Key Word":
                        self.add_token(c, TokenClass.SPECIFIER_START, "Type Specifier Mark")
                    elif self.advance=='=':
                        self.add_token("<=", TokenClass.LESS_EQUAL, "Conditional Operator")
                    else:
                        self.back()
                        self.add_token(c, TokenClass.LESS, "Conditional Operator")
                case '>':
                    if self.token_list[len(self.token_list)-1].parent_type == "Key Word":
                        self.add_token(c, TokenClass.SPECIFIER_END, "Type Specifier Mark")
                    elif self.advance()=='=':
                        self.add_token(">=", TokenClass.GREATER_EQUAL_EQUAL, "Conditional Operator")
                    else:
                        self.back()
                        self.add_token(c, TokenClass.GREATER, "Conditional Operator")
                case '^':
                    self.add_token(c, TokenClass.EXP, "Bitwise Operator")
                case '&':
                    if self.advance()=='&':
                        self.add_token("&&", TokenClass.AND_AND, "Logical Operator")
                    else:
                        self.back()
                        self.add_token(c, TokenClass.AND, "Bitwise Operator")
                case '|':
                    if self.advance()=='|':
                        self.add_token("||", TokenClass.OR_OR, "Logical Operator")
                    else:
                        self.back()
                        self.add_token(c, TokenClass.OR, "Bitwise Operator")
                case '!':
                    if self.advance()=='=':
                        self.add_token("!=", TokenClass.BANG_EQUAL, "Conditional Operator")
                    else:
                        self.back()
                        self.add_token(c, TokenClass.BANG, "Logical Operator")
                case '~':
                    if self.advance()=='=':
                        self.add_token("~=", TokenClass.BANG_EQUAL, "Conditional Operator")
                    else:
                        self.back()
                        self.add_token(c, TokenClass.BANG, "Logical Operator")
                case '+':
                    next_char = self.advance()
                    if next_char == '=':
                        self.add_token("+=", TokenClass.PLUS_EQUAL, "Binary Operator")
                    elif next_char == '+':
                        self.add_token("++", TokenClass.PLUS_PLUS, "Unary Operator")
                    else:
                        self.back()
                        self.add_token(c, TokenClass.PLUS, "Binary Operator")
                case '-':
                    next_char = self.advance()
                    if next_char == '=':
                        self.add_token("-=", TokenClass.MINUS_EQUAL, "Binary Operator")
                    elif next_char == '-':
                        self.add_token("--", TokenClass.MINUS_MINUS, "Unary Operator")
                    else:
                        self.back()
                        self.add_token(c, TokenClass.MINUS, "Binary Operator")
                case '/':
                    next_char = self.advance()
                    if next_char == '=':
                        self.add_token("/=", TokenClass.DIV_EQUAL, "Binary Operator")
                    elif next_char == '/':
                        self.add_token("//", TokenClass.INT_DIV, "Binary Operator")
                    else:
                        self.back()
                        self.add_token(c, TokenClass.DIV, "Binary Operator")
                case '*':
                    next_char = self.advance()
                    if next_char == '=':
                        self.add_token("*=", TokenClass.MULT_EQUAL, "Binary Operator")
                    elif next_char == '*':
                        self.add_token("**", TokenClass.EXP, "Binary Operator")
                    else:
                        self.back()
                        self.add_token(c, TokenClass.MULT, "Binary Operator")
                case '%':
                    self.add_token(c, TokenClass.MODULO, "Binary Operator")
                case '"':
                    self.string_handler()
                case "'":
                    self.char_handler()
                case "$":
                    if self.advance == '$':
                        if self.advance == '$':
                            #Multi Line Comment
                            self.comment_on = True
                            self.add_token("$$$", TokenClass.COMMENT_MARKER, "Comment Marker")
                            self.multi_line_commet()
                        else:
                            #Single Line Comment
                            self.add_token("$$", TokenClass.COMMENT_MARKER, "Comment Marker")
                            self.single_line_comment()
                    else:
                        self.error = "Invalid Syntax."
                case "-":
                    new_char = self.advance()
                    if self.is_digit():
                        self.number(c+new_char)
                    else:
                        self.error = "Invalid Syntax."
                case _:
                    if self.is_digit():
                        self.number(c)
                    elif self.is_alpha():
                        self.identifier_keyword(c)
                    else:
                        self.error = "Invalid Syntax."
                