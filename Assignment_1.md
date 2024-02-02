# CS 327: Assignment 1
## Topic: CodeSangam Language Syntax

**Instructor:** Prof. Abhishek Bichhawat  
**Group:** Comparsers

| Name          | Roll number |
| ------------- | ----------- |
| Dhruv Gupta   | 21110070    |
| Hirva Patel   | 21110154    |
| Shubh Singhal | 21110206    |
| Disha Chopra  | 21110057    |

## Definition of Different Data Types

Variable names must start from an alphabet and can contain only alphanumeric characters and underscore (`_`).
We are hosting three different datatypes:
- Number (int and float): `num`
- Boolean: `bool`
- String: `str`

Declaration statements:
```codesangam
num a = 99
str c = "exp"
bool x = Sahi/Galat
var v = "string"  // to assign datatype based on expression (to include " in str use \")
var v = 23        // num/bool 
```
Redeclaration of variables is not allowed, and a variable, once assigned to one data type, can’t be assigned to a different datatype.

## Compound Structures
### Dictionary 
```codesangam
dict<num,num> d = [2:3, 3:4, 5:6, 7:8 ]		//keys can num and str only
dict<num,dict<num,num>> d2 = [2:[3:4,4:5], 0:[1:2, 2:3]]
```
Functions:
```codesangam
d[key] = “Camel”  		//if str
d[key] = 2346 				//if num/bool
d.keys()					    //returns a list of keys
d.pop(key)					  //remove the given key-value pair
d.val()					      //returns a list of values
dict d3 = d.copy()		//makes a copy of dictionary
d.len()					      //returns the number of keys
```

### List
```codesangam
list<str> l = [“Hirva”, “Disha”, “Dhruv”, “Shubh”]
```
Functions: 
```codesangam
l.append(123)			  //if num/bool/var
l.append(“str”)			//if str
l.insert([0],24)		//inserts 24 at 1st position
l.join(l2)				  //adds l2 after of l
num x  = sum(l)			//returns sum if list datatype is num
l.len()				      //returns the size of l
l.count(1)				  //counts the occurrences of 1
l.index(4)				  //returns element at 5th position
l.slice(1:5)			  //takes 2nd, 3rd, 4th and 5th element
l.index(34) 			  //returns the first occurrence index of 34
```

### Tuple 
```codesangam
tup<var> t = [“abc”,Galat,79] (tuple<var> allows different datatypes in its content)
tup<num> t = [12,0,79]        (tuple can only contain one type of datatype)
```
Functions:
```codesangam
t.count(1)				//counts occurrences of 1
t.index(43)			  //returns index of 43
t.len()				    //returns the length of the tuple
t(3) 					    //accesses 4th element
```

### Array
```codesangam
arr<num> a[3] = [12, 34, 56, 78]
arr<num> b[3]				creates an array of length 3 containing zeros
```
Functions:
```codesangam
a.len()				                  //returns length of array
a.count(3)				              //counts frequency of 3 in arrays
a.index(56)			                //returns index of first 56 in array or else returns -1
arr<num> b[1] = a.slice(1:2)    //stores array with elements on index 1 in b
a.(2)					                  //accesses third element of array 
```

## Operators
Number Operations: 
```codesangam
num x			      //garbage values
y = int(x)	    //will assign integer value of x to y, the datatype will remain num
x = y+z         //addition
x = y*z         //multiplication
x = y-z         //subtraction
x = y/z         //division
x += y          //unary operator
x = y//z		    //integer divide
x = y**2		    //exponent (raised to the power 2) 
x = y%z		      //returns remainder
x++			        //pre increment			
x—-              //pre decrement
++x              //post increment
—-x              //post decrement
```                             
Logical Operators:
```codesangam
&&			  //and
||			  //or 
~ or !		//not
```	
Bitwise Operations:
```codesangam
&			    //Bitwise and
|			    //Bitwise or
^			    //Bitwise xor
```
String Operations: 	
```codesangam
str c = a+b		    //concatenate
str c = a[1:5]		//slicing
```
Conditional Operators:  Used for comparison between 2 operands/ expressions.
```codesangam
​<	: less than
>	: greater than
>=	: greater than or equal
<=	: less than or equal to
==	: is equal?
!=	: not equal to
```

## Print Statement
It is the keyword print itself, with all functionalities like Python, where we don’t have to specify the variable's data type to be printed explicitly.
Prints in new line every time.
```codesangam
str name = “Dhruv”
print(“Hello ”,name)						//Hello Dhruv
print(“hello”,end=””)						//ends with “”
```

## User Input
Input must be simple data types (num, string, bool), not compound datatypes like list tuples or dictionaries. 
```codesangam
x = input(“Input message: ”, data_type) 
```

## Conditional Statement
Keyword for if is agar, elif is magar and else is nahitoh. Each conditional is followed by a colon. Further, no brackets are required instead only indentation works.
```codesangam
agar (marks>80):
	print(“Pass”)
magar (marks>30 && marks<=80):
	print(“Re-exam”)
nahitoh :
	print(“Fail”)
```
An alternative for the break keyword is `niklo`.

## Loops: For and While
The keyword for “for” is “keliye” and “ while” is “jabtak”. No brackets are required instead indentation has to be followed. The loop syntax comprises the loop keyword followed by brackets having the information regarding how and till where the loop would be run separated by semicolon. 
```codesangam
num count=0
keliye (num i=1; i<9;  i++):
	statements
nahitoh:			(code enters this when loop exits normally)
	statements
```
If multiple statements need to be changed with every iteration, Every change should be separated with a comma(,)
```codesangam
keliye (num i=1; i<9;  i++, j++):
  statements
```
```codesangam
jabtak ((condition) == Sahi):
	grade++
nahitoh:
	Statements
```

## Function definition
The keyword for defining a function is “karya”. Also, a function declaration is done by keyword followed by the function name, brackets and colon.
```codesangam
karya int complierProject(bool: works):
	num grade
	agar (works==Sahi):
		grade = 11
	nhitoh:
		grade = 9
	vapas grade
```
Return type of the function is written after the keyword karya. If it's a void function, void would be written after karya keyword.

## Closures
The Syntax for the closures is as follows:
```codesangam
var add = kholiye num (num: num1, num: num2):
  vapas num1 + num2

num result = add(7, 9)
```	
This would store a value of 16 in result. 

`kholiye` is the keyword representing the beginning of a closure definition


## Mutable variables
Lists and dictionaries are mutable type objects. 

## Let Statements
We can use variables inside print statements using let functions. Let supports all the built in data types.
```codesangam
print((let num a = 5 in a) * (let num a = 6 in 2*a))
```
This statement will print 60.
```codesangam
print(let str name = “Dhruv” in (“My name is “+name))
```
This statement will print “My name is Dhruv”

## Exceptions
Similar to try-except for python	
```codesangam
koshish:
	compilerProject()
warna:
	gradedown()
```

## Comments
Add  `//` before every line to consider it as a comment line.

For multi line comment, add `/*` at start and `*/` at end of the comment.
