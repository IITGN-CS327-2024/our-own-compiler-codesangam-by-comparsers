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

    #Punctuations
    COMMA =36 # ,
    DOT =37 # .
    COLON =40 # :
    SEMI = 41 # ;

    EOF = 43 # End of File

    #Binary Operators
    PLUS = 44 # +
    PLUS_EQUAL = 45 # +=
    MINUS = 46 # -
    MINUS_EQUAL = 47 # -=
    MULT = 48 # *
    MULT_EQUAL = 49 # *=
    DIV = 50 # /
    DIV_EQUAL = 51 # /=
    INT_DIV = 52 # //
    EXP = 53 # **
    MODULO = 54 # %

    #Unary Operator
    PLUS_PLUS = 55 # ++
    MINUS_MINUS = 56 # --

    #Logical Operator
    BANG = 57 # ! ~
    AND_AND = 58 # &&
    OR_OR = 59 # ||

    #Bitwise Operator
    OR = 60 # bitwise |
    XOR = 61 # bitwise ^
    AND = 62 # bitwise & 

    #Condiation Operator
    BANG_EQUAL = 63 # != ~=
    EQUAL_EQUAL = 64 # ==
    GREATER = 65 # >
    GREATER_EQUAL = 66 # >=
    LESS = 67 # <
    LESS_EQUAL = 68 # <=

    # Type Specifier Mark
    SPECIFIER_START = 69 # <
    SPECIFIER_END = 70 # >

    #Assignment Operator
    EQUAL = 71 # =
    
    #Identifier
    IDENTIFIER = 72

    STRING = 73 # Constant String
    NUMBER = 74 # Constant Number

    COMMENT_MARK = 75 # $$

    COMMENT = 76 # Comment Content