from enum import Enum

class TokenClass(Enum):
    #Keywords
    IN=1
    NUM=2
    BOOL=3
    STR=4
    VAR=5
    SAHI=6
    GALAT=7
    DICT=8
    LIST=9
    TUP=10
    ARR=11
    INT=12
    FLOAT=13
    PRINT=14
    INPUT=15
    AGAR=16
    MAGAR=17
    NAHITOH=18
    NIKLO=19
    KELIYE=20
    JABTAK=21
    KARYA=22
    VAPAS=23
    VOID=24
    KHOLIYE=25
    LET=26
    KOSHISH=27
    VARNA=28
    LEN=29
    SLICE = 30
    COUNT = 31
    ACCESS = 32
    APPEND = 33
    INSERT = 34
    JOIN = 35
    SUM = 36
    POP = 37
    KEYS = 38
    VAL = 39
    COPY = 40

    #Paranthesis
    LEFT_PAREN = 41 # (
    RIGHT_PAREN = 42 # )
    LEFT_BRACE = 43 # {
    RIGHT_BRACE = 44 # }
    LEFT_SQUARE = 45 # [
    RIGHT_SQUARE = 46 # ]
    DICT_LEFT = 88 # \[
    DICT_RIGHT = 89 # \]

    #Punctuations
    COMMA =47 # ,
    DOT =48 # .
    COLON =49 # :
    SEMI = 50 # ;

    #Extras
    EOF = 51  # End of File
    INDENT = 85
    DEDENT = 86
    NEW_LINE = 87

    #Binary Operators
    PLUS = 52 # +
    PLUS_EQUAL = 53 # +=
    MINUS = 54 # -
    MINUS_EQUAL = 55 # -=
    MULT = 56 # *
    MULT_EQUAL = 57 # *=
    DIV = 58 # /
    DIV_EQUAL = 59 # /=
    INT_DIV = 60 # //
    EXP = 61 # **
    MODULO = 62 # %

    #Condiation Operator
    BANG_EQUAL = 63 # != ~=
    EQUAL_EQUAL = 64 # ==
    GREATER = 65 # >
    GREATER_EQUAL = 66 # >=
    LESS = 67 # <
    LESS_EQUAL = 68 # <=

    #Unary Operator
    PLUS_PLUS = 69 # ++
    MINUS_MINUS = 70 # --

    #Logical Operator
    BANG = 71 # ! ~
    AND_AND = 72 # &&
    OR_OR = 73 # ||

    #Bitwise Operator
    OR = 74 # bitwise |
    XOR = 75 # bitwise ^
    AND = 76 # bitwise & 

    # Type Specifier Mark
    SPECIFIER_START = 77 # <
    SPECIFIER_END = 78 # >

    #Assignment Operator
    EQUAL = 79 # =
    
    #Identifier
    IDENTIFIER = 80

    STRING = 81 # Constant String
    NUMBER = 82 # Constant Number

    COMMENT_MARKER = 83 # $$

    COMMENT = 84 # Comment Content