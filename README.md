# our-own-compiler-comparsers

Group 4:
    Dhruv Gupta | 
    Disha Chopra | 
    Hirva Patel | 
    Shubh Singhal 
    
This repo contains content developed as we build our own compiler for our custom language CodeSangam

# Instructions for running the programs

## Lexer_CodeSangam.py

This file identifies the different tokens in the program file line by line and classify them in different categories. Categories and its members can be seen in `Documents/TokenClass.md`.  

Run the following command to use Lexer_CodeSangam.py to classify the lexems: `python Lexer_CodeSangam.py <file_path>`.  

## Parser_CodeSangam.py
This file has the code for the parser that uses Lark LALR parser to for the tree.
  
Run The following command to use the Parser_CodeSangam.py to parse the code and see the tree: `python Parser_CodeSangam.py <file_path>`.  
  
In order to generate the tree pictorial representation use the following command where the image_file_path is the location you want to save the tree image: `python Parser_CodeSangam.py <file_path> <image_file_path>`. 
    
The images of the test cases have been stored in the folder `Parse_Trees`.

## AST_CodeSangam.py
This file has code for AST generation from the parse tree. However, we call the contents of this file now in Parser_Codesangam.py itself, so no need to run any other file.

You can just run the following command to classify the generate AST: `python Parser_CodeSangam.py <file_path>`.  (NOTE: with progressing assignments we are not printing the generated AST with this command, but it is still being utilised in this command)

## Semantic_Analyzer.py
This file has code for semantic analysis of the generated AST and for returning the scope tree after analyzing and type checking. However, we call the contents of this file also now in Parser_Codesangam.py itself, so no need to run any other file. (NOTE: We are not printing the scope_tree currently, if you wish to see its output add a print statement after analyze statement called in Parser_Codesangam file)

## WAT_Generator.py
This is the final code for our compiler to generate Web Assembly Text (WAT) code. We are calling its convert_program function to generate WAT code in the Parser_Codesangam.py file itself, so it is the only file you need to run to compile your test cases.

Run The following command to compile the code completely and generate WAT code for it: `python Parser_CodeSangam.py <file_path>`.

The above command saves the WAT code in the WAT_code folder. You can generate wasm code from this WAT code using wat2wasm functionality in [wabt](https://github.com/WebAssembly/wabt). You first need to build their tools then you can run the command `bin/wat2wasm <testfile>.wat -o <outputfile>.wasm`.
