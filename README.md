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
Run The following commend to use the Parser_CodeSangam.py to parse the code and see the tree: `python Parser_CodeSangam.py <file_path>`.  
In order to generate the tree pictorial representation use the following comand where the image_file_path is the location you want to save the tree image: `python Parser_CodeSangam.py <file_path> <image_file_path>`.   
The images of the test cases have been stored in the folder `Parse_Trees`.

