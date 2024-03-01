# Token Classes in CodeSangam:

1. **Keywords:**
   - IN, NUM, BOOL, STR, VAR, SAHI, GALAT, DICT, LIST, TUP, ARR, INT, FLOAT, PRINT, INPUT, AGAR, MAGAR, NAHITOH, NIKLO, KELIYE, JABTAK, KARYA, VAPAS, VOID, KHOLIYE, LET, KOSHISH, VARNA, LEN, SLICE, COUNT, ACCESS, APPEND, INSERT, JOIN, SUM, POP, KEYS, VAL, COPY
   - **Regular Language:** `IN|NUM|BOOL|STR|VAR|SAHI|GALAT|DICT|LIST|TUP|ARR|INT|FLOAT|PRINT|INPUT|AGAR|MAGAR|NAHITOH|NIKLO|KELIYE|JABTAK|KARYA|VAPAS|VOID|KHOLIYE|LET|KOSHISH|VARNA|LEN|SLICE|COUNT|ACCESS|APPEND|INSERT|JOIN|SUM|POP|KEYS|VAL|COPY`

2. **Paranthesis:**
   - LEFT_PAREN, RIGHT_PAREN, LEFT_BRACE, RIGHT_BRACE, LEFT_SQUARE, RIGHT_SQUARE
   - **Regular Language:** `\(|\)|\{|\}|\[|\]`

3. **Punctuations:**
   - COMMA, DOT, COLON, SEMI
   - **Regular Language:** `,|\.|:|;`

4. **Extras:**
   - EOF(End of File), START_INDENT, END_INDENT, NEW_LINE

5. **Binary Operators:**
   - PLUS, PLUS_EQUAL, MINUS, MINUS_EQUAL, MULT, MULT_EQUAL, DIV, DIV_EQUAL, INT_DIV, EXP, MODULO
   - **Regular Language:** `\+|\+=|-|-=|\*|\*=|/|/=|//|\*\*|%`

6. **Condition Operators:**
   - BANG_EQUAL, EQUAL_EQUAL, GREATER, GREATER_EQUAL, LESS, LESS_EQUAL
   - **Regular Language:** `!=|==|>|>=|<|<=`

7. **Unary Operators:**
   - PLUS_PLUS, MINUS_MINUS
   - **Regular Language:** `\+\+|--`

8. **Logical Operators:**
   - BANG, AND_AND, OR_OR
   - **Regular Language:** `!|&&|\|\|`

9. **Bitwise Operators:**
   - OR, XOR, AND
   - **Regular Language:** `\||^|&`

10. **Type Specifier Mark:**
    - SPECIFIER_START, SPECIFIER_END
    - **Regular Language:** `<|>`

11. **Assignment Operator:**
    - EQUAL
    - **Regular Language:** `=`

12. **Identifier:**
    - IDENTIFIER
    - **Regular Language:** `[a-zA-Z_][a-zA-Z0-9_]*`

13. **String Constant:**
    - STRING
    - **Regular Language:** `"[^"]*"`

14. **Number Constant:**
    - NUMBER
    - **Regular Language:** `[0-9]+`

15. **Comment Marker:**
    - COMMENT_MARKER
    - **Regular Language:** `$$ |$$$`

16. **Comment Content:**
    - COMMENT
    - **Regular Language:** `.*`

