from Token import *
from TokenClass import *

class Line:

    KeyWords = {
    "in" : TokenClass.IN,
    "num" : TokenClass.NUM,
    "bool" : TokenClass.BOOL,
    "str" : TokenClass.STR,
    "var" : TokenClass.VAR,
    "Sahi" : TokenClass.SAHI,
    "Galat" : TokenClass.GALAT,
    "dict" : TokenClass.DICT,
    "list" : TokenClass.LIST,
    "tup" : TokenClass.TUP,
    "arr" : TokenClass.ARR,
    "int" : TokenClass.INT,
    "float" : TokenClass.FLOAT,
    "print" : TokenClass.PRINT,
    "input" : TokenClass.INPUT,
    "agar" : TokenClass.AGAR,
    "magar" : TokenClass.MAGAR,
    "nahitoh" : TokenClass.NAHITOH,
    "niklo" : TokenClass.NIKLO,
    "keliye" : TokenClass.KELIYE,
    "jabtak" : TokenClass.JABTAK,
    "karya" : TokenClass.KARYA,
    "vapas" : TokenClass.VAPAS,
    "void" : TokenClass.VOID,
    "kholiye" : TokenClass.KHOLIYE,
    "let" : TokenClass.LET,
    "koshish" : TokenClass.KOSHISH,
    "varna" : TokenClass.VARNA,
    "len" : TokenClass.LEN,
    "slice" : TokenClass.SLICE ,
    "count" : TokenClass.COUNT ,
    "access" : TokenClass.ACCESS ,
    "append" : TokenClass.APPEND ,
    "insert" : TokenClass.INSERT ,
    "join" : TokenClass.JOIN ,
    "sum" : TokenClass.SUM ,
    "pop" : TokenClass.POP ,
    "keys" : TokenClass.KEYS ,
    "val" : TokenClass.VAL ,
    "copy" : TokenClass.COPY
    }

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
        self.has_error = False
    
    def print_lexemes(self):
        print("line",self.line_number,"indent block",self.indentation,":")
        for token in self.token_list:
            print("\t", "<",token.content,",",token.type,",",token.parent_type,">")
        print()

    def find_indentation(self):
        char = self.advance()
        while char==' ' or char=='\t':
            if char==' ':
                self.indentation+=1
            else:
                self.indentation+=4
            char = self.advance()
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
    
    def add_token(self, content, token_type, parent_type):
        new_token = Token(content, token_type, parent_type)
        self.token_list.append(new_token)

    def string_handler(self):
        content = '"'
        new_char = self.advance()
        while not self.is_end() and (new_char != '”' and new_char!='"'):
            content+=new_char
            new_char = self.advance()
        content += '"'
        if self.is_end():
            if new_char=='"' or new_char=='”':
                self.add_token(content, TokenClass.STRING, "String")
            else:
                self.error = "Expected closing double quotation mark."
                self.has_error = True
            return 
        self.add_token(content, TokenClass.STRING, "String")
        
    def char_handler(self):
        content = "'"
        if self.is_end():
            self.error = "Expected closing single quotation mark"
            self.has_error = True
            return 
        new_char = self.advance()
        content += new_char
        if new_char=="'":
            self.add_token(content, TokenClass.STRING, "String")
        else:
            if self.is_end():
                self.error = "Expected closing single quotation mark"
                self.has_error = True
                return 
            new_char = self.advance()
            if new_char == "'":
                content+=new_char
                self.add_token(content, TokenClass.STRING, "String")
            else:
                self.error = "Expected closing single quotation mark"
                self.has_error = True
                return 
    
    def is_digit(self, char):
        return char >= '0' and char <= '9'
    
    def is_alpha(self, char):
        return  (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z') or char == '_'
    
    def number(self, digit):
        content = digit
        new_char = ""
        while not self.is_end(): 
            new_char =  self.advance()
            if self.is_digit(new_char):
                content+=new_char
            else:
                self.back()
                break
        if new_char==".":
            content+=new_char
            self.advance()
            while not self.is_end():
                new_char =  self.advance()
                if self.is_digit(new_char):
                    content+=new_char
                else:
                    self.back()
                    break
            self.add_token(content, TokenClass.NUMBER, "Number")
        else:
            self.add_token(content, TokenClass.NUMBER, "Number")
    
    def identifier_keyword(self, char):
        content = char
        new_char = ""
        while not self.is_end(): 
            new_char =  self.advance()
            if self.is_digit(new_char) or self.is_alpha(new_char):
                content+=new_char
            else:
                self.back()
                break
        if content in list(self.KeyWords.keys()):
            self.add_token(content, self.KeyWords[content], "Key Word")
        elif content[0]!='_':
            self.add_token(content, TokenClass.IDENTIFIER, "Identifier")
        else:
            self.error = "Any identifier name should not start with num or underscore (_)."
            self.has_error = True
    
    def single_line_comment(self):
        char =  self.advance()
        content = ""
        while not self.is_end():
            content+=char
            char = self.advance()
        content+=char
        self.add_token(content, TokenClass.COMMENT, "Comment")

    def multi_line_comment(self):
        content = ""
        while not self.is_end():
            char = self.advance()
            if char=='$':
                if not self.is_end():
                    if self.advance()=='$':
                        if not self.is_end():
                            if self.advance()=='$':
                                self.comment_on = False
                                break
                            else:
                                self.back()
                                self.back()
                        else:
                            self.back()
                    else:
                        self.back()
            content+=char
        self.add_token(content, TokenClass.COMMENT, "Comment")
        if not self.comment_on:
            self.add_token("$$$", TokenClass.COMMENT_MARKER, "Comment Marker")         

                    
    def scan_tokens(self):
        if self.comment_on : 
            self.multi_line_comment()
        while not self.is_end() and not self.has_error:
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
                    elif self.advance()=='=':
                        self.add_token("<=", TokenClass.LESS_EQUAL, "Conditional Operator")
                    else:
                        self.back()
                        self.add_token(c, TokenClass.LESS, "Conditional Operator")
                case '>':
                    if self.token_list[len(self.token_list)-1].parent_type == "Key Word":
                        self.add_token(c, TokenClass.SPECIFIER_END, "Type Specifier Mark")
                    elif self.advance()=='=':
                        self.add_token(">=", TokenClass.GREATER_EQUAL, "Conditional Operator")
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
                case "$":
                    if self.advance() == '$':
                        if self.advance() == '$':
                            #Multi Line Comment
                            self.comment_on = True
                            self.add_token("$$$", TokenClass.COMMENT_MARKER, "Comment Marker")
                            self.multi_line_comment()
                        else:
                            #Single Line Comment
                            self.back()
                            self.add_token("$$", TokenClass.COMMENT_MARKER, "Comment Marker")
                            self.single_line_comment()
                    else:
                        self.back()
                        self.error = "Invalid Syntax."
                        self.has_error = True
                case _:
                    if self.is_digit(c):
                        self.number(c)
                    elif self.is_alpha(c):
                        self.identifier_keyword(c)
                    else:
                        if c=='"' or c=='“':
                            self.string_handler()
                        elif c=='\'':
                            self.char_handler()
                        else:
                            self.error = "Invalid Syntax."
                            self.has_error = True
                