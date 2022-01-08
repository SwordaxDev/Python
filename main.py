# Python About
"""
    - Python is a server-side programming language.
    - Python can be used for many things: {
        * Web Development (server-side)
        * Software Development
        * Machine Learning
        * AI
        * Mathematics
        * System Scripting
    }
    - This documentation is about Python 3
    - Python files have the file extension .py (filename.py)
"""




# Intro [1]
# getting started [1.1]
"""
    - To use python, you will need to install the language interpreter from 
    python's official site, and you will need an IDE, text editor to write 
    python.
    - You might already have python installed in your device, to check if so, 
    run the following command in your cmd or terminal: python --version
    - To run python files, run the following in your terminal: python filename.py
    - You can test small amounts of python code in your terminal by using the python command: {
        python
        >>> print("Hello world from terminal!")
    } or if that didn't work, you can use: {
        py
        >>> print("Hello world from terminal!")
    }
    - To exit the testing mode in the terminal, run the following command: exit()
"""


# Syntax [1.2]
"""
    - Python uses new line to complete a command, unlike other languages that use semi-colons
    - Python uses indentation to contain a block scope, unlike other languages that use curly-brackets
    - Indentation size doesn't matter, as long as all the code from the same block is on the same level
"""
def first_function():
    lang = "Python"
    print("This is my first code in " + lang + "!")
    # notice how end of command was just a new line rather than semi-colons
    # notice how the block scope of the function is just defined using indentation
first_function()


# Comments [1.3]
"""
    - Commented code is ignored when run.
    - Comments are used to add documentation to your code, explain a code, or comment out a code 
    temporarily or for testing purposes.
    - In python, there are two types of comments: {
        1- Single line comments using hashtags
        2- Multi-line comments using triple quotes
    }
"""
# this is a single line comment
eee = 5  # this is a single line comment after some uncommented code
""" this is a multi-line comment """
"""
    Multi-line comment actually being multi-line
    would look like this
"""




# Variables [2]
# intro to variables [2.1]
"""
    - Variables in programming are used to store data values.
    - Unlike other languages, python doesn't have a keyword for declaring variables, 
    you declare variables by just defining the name, then = sign, then the value.
"""
# defining variables
my_first_variable = "This is my first variable"  # defining a variable storing a string value
# a string is a text value, will be explained in details in a later lesson
num_var = 2022  # defining a variable named "num_var" and setting it's value to be a number value (2022)

# casting [2.2]
# you can specify the data type of a variable using casting
name = str("Swordax")  # specifying that variable (name) value will be a string using str()
age = int(2022)  # specifying that variable (age) value will be an integer using int()
weight = float(1.2)  # specifying that variable (weight) value will be a float using float()
# there are more data types, those will be listed for now
# an integer is a whole number (no decimals), float numbers are numbers with decimals
# if you do float(1) the value will be 1.0

# overwriting variables [2.3]
# you can overwrite variables original value and set a new value to it
overwriting_variables = "Original Variable Value"
print(overwriting_variables)  # this will print: "Original Variable Value" as it's original value defined above
overwriting_variables = "Overwritten Variable Value"  # we can overwrite variables values
print(overwriting_variables)  # this will print: "Overwritten Variable Value"

# get variable value data type [2.4]
string_var = "This is a string value"
integer_var = 100
float_var = 3.14
print(type(string_var))  # this will print: <class 'str'> which means it's a string
print(type(integer_var))  # this will print: <class 'int'> which means it's an integer
print(type(float_var))  # this will print: <class 'float'> which means it's a float

# string variable declaration [2.5]
"""
    - When you define a string variable value, you have to contain it inside quotes '' or ""
    - You can use single OR double quotes when defining the value of a string variable, choice is yours!
    - If you want to contain quotes inside your text, use the other type of quotes, example: {
        "My name is 'Swordax' and I am a programmer"
        'My name is "Swordax" and I am a programmer'
    }
"""
single_quotes = 'This text is contained inside single quotes'
double_quotes = "This text is contained inside double quotes"
nested_quotes_1 = "This text contains 'single' quotes"
nested_quotes_2 = 'This text contains "double" quotes'

# variable naming rules [2.6]
"""
    - When naming variables, there are rules you need to follow: {
        1- variable name must start with a letter or an underscore
        2- variable name CANNOT start with a number
        3- variable name can only contain alpha-numeric characters and underscores (a-z, A-Z, 0-9, _)
        4- variable names are case-sensitive, so (age, AGE, Age) are three different variables
    }
"""
varexample = "valid"
VAREXAMPLE = "valid"
VarExample = "valid"
varExample = "valid"
var_example = "valid"
var0example = "valid"

# multi-name variable naming style [2.7]
"""
    You can name a variable whatever you want (as long as the name follows the rules mentioned in lesson 2.6), 
    but it's a common good practice to name it using one of the popular naming styles, just as a good habit.
"""
camelCase = "variable named using the camel case naming style"
PascalCase = "variable named using the pascal case naming style"
snake_case = "variable named using the snake case naming style"

# assigning multiple values to variables [2.8]
a, b, c = "a value", "b value", "c value"  # defining and assigning three variables at a time
x = y = z = "single value for x, y, and z"  # assigning the same value for 3 variables at a time
fruits = ["apple", "banana", "cherry"]  # declaring a list (you will learn about lists more in later lessons)
q, w, e = fruits  # unpacking the list into separate separate variables

# outputting variables [2.9]
my_name = "Swordax"
print("My name is " + my_name)  # combining text with a variable
sentence = "My name is "
print(sentence + my_name)  # printing two variables (combining them)
his_name = "Swordy Man"
her_name = "Swordy Woman"
their_names = his_name + " " + her_name # notice combining variables and texts in a single variable
print(their_names)  # printing the variable that combines the other variables
"""
    As you can see in the previous examples, using "+" between string values concatenates and joins them, 
    but when using it between number values, it will actually operate addition on them.
"""
one = 1
two = 2
print(one + two)  # this will print 3
_one = "1"
_two = "2"
print(_one + _two)  # this will print "12"
"""
    - If you try to join a string value with a number value, you will get an error, so the following: {
        text = "Hello world!"
        number = 12
        print(text + number)
    } will result in an error
"""

# variables scope [2.10]
"""
    - Variables are accessible only inside their scope. Almost all the variables that we have created 
    in the previous lessons (excluding lesson 1.2) are global variables, because they all were created 
    and declared on the top level scope in the code.
    - Global Variables: a variable that is accessible everywhere in the code.
    - Scope: a scope can be defined as the current block of code and it's whole content of code and blocks.
    - Function Scope: the scope of a function code block (functions will be explained in details in later lessons)
"""
global_variable = "this can be accessible everywhere in the code"
def scope_demo():
    print(global_variable)  # this would work because global_variable is a global variable
    local_variable = "this variable is only accessible inside the scope of scope_demo() function"
    if True:
        print(global_variable)  # this would work
        print(local_variable)  # this would work
        # the previous line would work because the local_variable is still inside the scope of scope_demo() function
scope_demo()
# print(local_variable) <- this code would make an error as local_variable is not in the scope of it's function
print(global_variable)  # this would work
"""
    You can overwrite a global variable inside a function only while reserving its original value outside the function
"""
global_var = "Original"
def overwriting_demo():
    global_var = "Overwritten"
    print(global_var)  # prints: "Overwritten"
overwriting_demo()
print(global_var)  # prints: "Original" notice how it wasn't overwritten outside the function scope
"""
    You can make a local variable inside a function global by using the "global" keyword
"""
def scope_demo_2():
    global global_keyword
    global_keyword = "Hello world!"
scope_demo_2()
print(global_keyword)
# ^ this would work even though the global_keyword variable was defined inside a function because of the global keyword
"""
    If you want to overwrite a global variable inside a function, you will need to use the global keyword
"""
global_variable_2 = "Hello world!"
def scope_demo_3():
    global global_variable_2
    print(global_variable_2)  # prints: "Hello world!"
    global_variable_2 = "Hello universe!"
    print(global_variable_2)  # prints: "Hello universe!"
print(global_variable_2)  # prints: "Hello world!"
scope_demo_3()
print(global_variable_2)  # prints: "Hello universe!"




# Data Types [3]
# intro to data types [3.1]
"""
    - Data types in programming can be defined as the type of data ( silly definition isn't it :/ )
    - Variables can store data from different types, and different types can do different things
    - There are many built-in data types in python, and this is a list of them in categories: {
        Text Type:       str
        Number Types:    int, float, complex
        Sequence Types:  list, tuple, range
        Mapping Type:    dict
        Set Types:       set, frozenset
        Boolean Type:    bool
        Binary Types:    bytes, bytearray, memoryview
    }
    - As mentioned in previous lessons, you can get the data type of a value using type() built-in function: {
        string = "Text"
        print(type(string))  # this will print the data type of string variable
    }
"""

# data types in real code [3.2]
string_type = "str"
integer_type = 4
float_type = 12.4
complex_type = 1j
list_type = ["Swordax", "Swordy", "Sword"]
tuple_type = ("Swordax", "Swordy", "Sword")
range_type = range(4)
dict_type = {
    name: "Swordax",
    age: 2022
}
set_type = {"Swordax", "Swordy", "Sword"}
frozenset_type = frozenset({"Swordax", "Swordy", "Sword"})
bool_type = True
bytes_type = b"Swordax"
bytearray_type = bytearray(4)
memoryview_type = memoryview(bytes(4))

# setting specific data type (casting) [3.3]
"""
    - When creating a variable, you can specify what data type you want it to be by using a constructor function.
    - Data type constructor functions come with the exact same naming of the data types listed in lesson 3.1
    - Examples to build your understanding around: {
        _string = str("String data type")
        _integer = int(4)
        _float = float(4.2)
        _complex = complex(1j)
        _list = list(("Swordax", "Swordy", "Sword"))
        _tuple = tuple(("Swordax", "Swordy", "Sword"))
        _range = range(6)
        _dict = dict(name = "Swordax", age = 2022)
        _set = set(("Swordax", "Swordy", "Sword"))
        _frozenset = frozenset(("Swordax", "Swordy", "Sword"))
        _bool = bool(4)
        _bytes = bytes(4)
        _bytearray = bytearray(4)
        _memoryview = memoryview(bytes(4))
    }
"""




# Numbers [4]
# numeric data types [4.1]
"""
    - Python contains three numeric data types: {
        - int:      integers, whole numbers, positive or negative, without decimals, of unlimited length.
        - float:    floating point numbers, positive or negative, containing one or more decimals.
        - complex:  complex numbers, written with a "j" character as the imaginary part.
    }
"""
# int
int_1 = 100
int_2 = -123
int_3 = 8375829075983
# float
float_1 = 1.12
float_2 = -42.24323
float_3 = 1.0
float_4 = 29e4
float_5 = -234E39
# complex
complex_1 = 5j
complex_2 = -5j
complex_3 = 2+6j

# numeric type conversion [4.2]
"""
    You can convert between data types using the int(), float(), complex() built-in methods
"""
print(int(float_1))       # prints: 1
print(float(int_1))       # prints: 100.0
print(complex(float_3))   # prints: (1+0j)
# NOTE: you cannot convert complex numbers into other numeric data types

# random numbers [4.3]
"""
    - You can generate a random number in python!
    - Python does not have a function that generates random numbers, but it has a built-in 
    modules that does that for us, and its called "random"
    - To use modules in python, you will first have to import them.
    - Usually you would have to install external modules, but since the random module 
    is built in the language itself, you wont have to install anything, just directly import the module.
"""
import random
random_number = random.randrange(1, 10)  # this will generate a random number between 1 and 9 (10 is excluded)
print(random_number)  # this will print the generated random number




# Strings [5]
# basic strings [5.1]
"""
    - In python, strings are text values, they are surrounded by quotes, either single or double.
    - "Hello world!" is the same as 'Hello world!'
"""
string_ex_1 = "This is a string"
string_ex_2 = 'This is another string'
string_ex_3 = """
You can create multi-line string variables by using triple double quotes, 
or triple single quotes, as easy as that!
"""
string_ex_4 = '''
Another example of multi-line string variables, 
but this time created using triple single quotes
'''
# NOTE: in multi-line strings, the breaks in the line are included in the outputs

# get a specific character in a string [5.2]
"""
    - you can get a specific character inside your string using square brackets
    - if your familiar with other programming languages, you should be familiar with this information. In 
    programming, we don't start counting from 1, but we start counting from 0, get used to that!
    - you get the nth-character in the string by counting from 0, so the 0th character is the 1st character.. etc..
"""
string_ex_5 = "Hello world!"
print(string_ex_5[0])  # prints: "H"
print(string_ex_5[1])  # prints: "e"
# etc..

# the len() method [5.3]
# you can get the length of a string (number of characters in a string) by using the len() method
print(len(string_ex_5))  # prints: 12 (since the number of characters inside string_ex_5 is 12 characters)
# a trick that can help you get the last character in a string:
string_ex_6 = "The last character here is Z"
print(string_ex_6[len(string_ex_6) - 1])
"""
    Explanation: {
        - we had to get the last character in the string, so we got the nth (string length - 1) character.
        - the -1 is because as you know, we start counting from 0 and not from 1
    }
"""

# the in keyword [5.4]
"""
    - we can check if a certain character or phrase is present inside a string by using the "in" keyword
    - the result of this check will be a boolean value, which is either True or False
    - note that the check is case sensitive, so you should make sure to get the letter casing right
"""
string_ex_7 = "Swordax"
print("S" in string_ex_7)    # prints: True (since character "S" is present inside the string "Swordax")
print("s" in string_ex_7)    # prints: False (since character "s" is not present inside the string "Swordax")
print("dax" in string_ex_7)  # prints: True (since the phrase "dax" is present inside the string "Swordax")
print("da x" in string_ex_7) # prints: False (since the phrase "da x" is not present inside the string "Swordax")
# you can check if character or phrase is NOT present in a string by adding the "not" keyword (logical operator)
print("ZZZ" not in string_ex_7) # prints: True (as "ZZZ" is not present in "Swordax")
# etc..

# slicing strings [5.5]
"""
    - sometimes you might need to slice a string (crop a string) to get a specific part of it
    - in python, its very easy to slice a string
"""
my_sentence = "Hello world!"
hello_word = my_sentence[0:5]  # this contains "Hello" which is from character 0 to character 4 (5 excluded)
world_word = my_sentence[6:11]  # this contains "world" which is from character 6 to character 10 (11 excluded)
exclamation = my_sentence[11:12]  # this contains "!" which is from character 11 to character 12 (12 excluded)
print(hello_word + " " + world_word + exclamation)  # prints: "Hello world!"
# slice from start by leaving the first index empty
print(my_sentence[:5])  # prints: "Hello"
# slice to the end by leaving the last index empty
print(my_sentence[6:])  # prints: "world!"
# negative indexing (cut from the end of the string backwardly)
print(my_sentence[-5:-2])  # prints: "orl" (from index -5 backwardly to index -2 backwardly (excluded))

# string modification [5.6]
"""
    - Python has a set of built-in methods and functions that can be used to modify strings
"""
lowercased_str = "hello"
uppercased_str = "HELLO"
padded_str = "   Hello   "
test_str = "My name is Zwordax!"
names_str = "Swordax, Vazox, Sword"
print(lowercased_str.upper())  # prints an upper-cased version of the string
print(uppercased_str.lower())  # prints a lower-cased version of the string
print(padded_str.strip())  # prints a stripped/trimmed version of the string (removes white spaces around the string)
print(test_str.replace("Z", "S"))  # prints a version of the string where all "Z" characters are replaced with "S"
# notice that the replacing is case-sensitive, so the previous example will only replace the "S" letters not the "s"
print(names_str.split(","))  # prints a list (array), breaks and separates at commas
# the split() method changes the string into a list and separates words depending on the passed separator

# string format() method [5.7]
"""
    - The format() method allows us to insert dynamic values into a string, and concatenate strings.
    - In the main string, we will use curly-brackets to define where the inserting should take place.
    - In the format() function, we should pass into the parenthesis the values we want to insert.
    - Make sure the number of curly-brackets is euil to the number of items inserted in the format() function.
    - Note: as you know, we normally cannot concatenate/join strings and numbers together without convering them, 
    but when using the format() method, we can do that!
"""
template = "My name is {}, I am {} years old, I am from {}"
final_txt = template.format("Swordax", 2022, "CLASSIFIED")
print(final_txt)  # prints: "My name is Swordax, I am 2022 years old, I am from CLASSIFIED"
# you can always do it differently! for example, you can pass variables instead of direct strings
_name = "Swordax"
_age = 2022
_nationality = "CLASSIFIED"
print(template.format(_name, _age, _nationality))  # this should print the same result as the previous example
# you can change the order of the inserted items by passing indexing into the curly-brackets in the template
template_2 = "My name is {2}, I am {0} years old, I am from {1}"
print(template_2.format(2022, "CLASSIFIED", "Swordax"))  # this should print the same result as previous examples

# escape characters [5.8]
"""
    - Sometimes you might need to use illegal characters in a string that you normally can't use, well, you 
    can do that using the escape character (back-slash) + (escaped character)
"""
txt = "My name is \"Swordax\""
"""
    - As you can see in the previous example, we created a string with double quotes, and we had to use 
    double quotes inside the string. doing that without using the escape characters will cause errors because 
    python won't know which quotes are closing the string and which are inside the string.
    - You can use double quotes inside double-quoted strings using the escape character (back-slash) + (double quote).
    -The escape character allows you to use illegal characters inside strings.
    - In the previous example, we could have just used single quotes to include the string, but its just 
    an example, and you will sometimes be in situations where you will really need the escape character.
"""
"""
    - Escape Characters: {
        \' : escape single quotes
        \" : escape double quotes
        \\ : escape backslashes
        \n : break to a new line
        \r : carriage return
        \t : tab
        \b : backspace
        \f : form feed
        \ooo : octal value
        \xhh : hex value
    }
"""

# string methods [5.9]
"""
    - We have previously seen a number of string methods in the previous lessons, but here is a 
    bigger list of them.
"""
s = "this is a string"
# methods
s.capitalize()      # converts the first character to upper case
s.casefold()        # converts string to lower case
s.center()          # returns a centered string (length, character)
s.count()           # returns the number of times a specified value occurs in a string (word)
s.encode()          # returns an encoded version of the string (encoding)
s.endswith()        # returns true if the string ends with the specified value (value)
s.expandtabs()      # sets the tab size of the string (amount)
s.find()            # searches the string for a specified value and returns the position of where it was found (word to find)
s.format()          # formats specified values in a string (words)
s.format_map()      # formats specified values in a string
s.index()           # searches the string for a specified value and returns the position of where it was found (word to find)
s.isalnum()         # returns true if all characters in the string are alphanumeric
s.isalpha()         # returns true if all characters in the string are in the alphabet
s.isdecimal()       # returns true if all characters in the string are decimals
s.isdigit()         # returns true if all characters in the string are digits
s.isidentifier()    # returns true if the string is an identifier
s.islower()         # returns true if all characters in the string are lower case
s.isnumeric()       # returns true if all the characters in the string are numeric
s.isprintable()     # returns true if all characters in the string are printable
s.isspace()         # returns true if all characters in the string are whitespaces
s.istitle()         # returns true if the string follows the rules of a title
s.isupper()         # returns true if all characters in the string are upper case
s.join()            # joins the elements of an iterable to the end of the string (list)
s.ljust()           # returns a left justified version of the string (length, character)
s.lower()           # converts a string into lower case
s.lstrip()          # returns a left trim version of the string
s.maketrans()       # returns a translation table to be used in translations
s.partition()       # returns a tuple where the string is parted into three parts (word)
s.replace()         # returns a string where a specified value is replaced wth a specified value (replace, replace with)
s.rfind()           # searches the string for a specified value and returns the last position of where it was found (word to find)
s.rindex()          # searches the string for a specified value and returns the last position of where it was found (word to find)
s.rpartition()      # returns a tuple where the string is parted into three parts (word)
s.rsplit()          # splits the string at the specified separator, and returns a list (separator, maxsplit)
s.rstrip()          # returns a right trim version of the string
s.split()           # splits the string at the specified separator, and returns a list (separator)
s.splitlines()      # splits the string at line breaks and returns a list (should line break be included, default false)
s.startswith()      # returns true of the string starts with the specified value (value)
s.strip()           # returns a trimmed version of the string
s.swapcase()        # swaps cases, lower case becomes upper case and vice versa
s.title()           # converts the first character of each word to upper case
s.translate()       # returns a translated string
s.upper()           # converts a string into upper case
s.zfill()           # fills the string with a specified number of 0 values at the beginning (number)




# Booleans [6]
# intro to booleans [6.1]
"""
    - A boolean is a data type in programming languages
    - A boolean can have 2 possible values only, True or False
    - The value of a boolean is not contained inside quotes, its dealt with as a keyword
    - Booleans have a constructor function of bool()
"""

# evaluating expressions [6.2]
print(12 > 4)   # prints: True (because 12 is more than 4)
print(12 == 4)  # prints: False (because 12 is not equal to 4)
print(12 < 4)   # prints: False (because 12 is not less than 4)
# don't worry about the comparison operators now, they will be discussed in details in later lessons

# booleans in conditional statements [6.3]
v_one = 100
v_two = 200
if v_one > v_two:  # the condition in the if statement is either True or False, which decides if the code runs or not
    print("Value one is more than value two")  # the if condition evaluated to False, so the print statement wont run
if True:  # we manually passed a static True, so the if statement will always run
    print("Value is true")
if False: # we manually passed a static False, so the if statement will never run
    print("Value is true")

# evaluate values [6.4]
# the bool() function allows you to evaluate any value, and give a True or False in return
print(bool("Hello world"))  # prints True
print(bool(2022))  # prints True
bool_one = "Hello world"
bool_two = 2022
print(bool(bool_one))  # prints True
print(bool(bool_two))  # prints False
"""
    - Almost any value is evaluated as True as it exists
    - Empty strings evaluate as False
    - All numbers evaluate as True, even negative numbers, except for 0 which evaluates as False
    - Lists, dictionaries, tuples, and sets, all evaluate as True, except for empty ones
"""
# all the following evaluates to False
print(bool({}))
print(bool([]))
print(bool(()))
print(bool(""))
print(bool(0))
print(False)
print(None)  # this is similar to "null" in JS, it basically says that the value is None, it evaluates to False

# functions returning booleans [6.5]
"""
    - Functions can return booleans, this could be useful when using a function to determine if something is True or not
"""
def booleanFunction_T():
    return True
def booleanFunction_F():
    return False
# you can then use this function in conditional statements
if booleanFunction_T(): # since this function returns a boolean, its a valid condition in if statements
    print("that is true!")
else:
    prit("that is false!")
# don't worry about if statements and functions for now, they are just for demo. will be explained in later lessons




# Python Operators [7]
# intro to operators [7.1]
"""
    - Operators are used to perform operations on values and variables
    - There are many kinds of operators, can be listed as: {
        * Arithmetic operators
        * Assignment operators
        * Comparison operators
        * Logical operators
        * Identity operators
        * Membership operators
        * Bitwise operators
    }
"""
# a simple example of an operator we have used alot in the past lessons, the + operator to add numbers together
print(12 + 4)  # performs a mathematical operation and prints 16

# arithmetic operators [7.2]
"""
    - Arithmetic operators are used with numeric values to perform common mathematical operations: {
        + : addition operator : used to add values together (used also for string concatenation)
        - : subtraction operator : used to subtract values from each other
        * : multiplication operator : used to multiply values with each other
        / : division operator : used to divide values from each other
        % : modulus operator
        ** : exponential operator
        // : floor division operator
    }
"""
# popular operators in use
print(12 + 4)  # addition operator
print(12 - 4)  # subtraction operator
print(12 * 4)  # multiplication operator
print(12 / 4)  # division operator

# assignment operators [7.3]
"""
    - Assignment operators are used to assign values to variables: {
        = : equal sign : used to assign a value to a variable
        += : increment operator : used to increment a variable value by a specific number
        -= : decrement operator : used to decrement a variable value by a specific number
        *= : multiply by operator : used to multiply a variable by a specific number
        /= : divide by operator : used to divide a variable by a specific number
    }
    note: there are more operators that are not mentioned as they aren't that popular and widely used
"""
val = 1  # variable assigned with value of 1
val += 1  # incremented by 1
val -= 1  # decremented by 1
val *= 1  # multiplied by 1
val /= 1  # divided by 1

# comparison operators [7.4]
"""
    - Logical operators are used to combine conditional statements: {
        and : returns True if both statements are True
        or : returns True if one of the statements is True
        not : reverses the result of the condition, so returns False if True, vice versa
    }
"""
if 1 == 1 and 2 == 2:  # can be compared to && in JavaScript
    print("both conditions are true")
if 1 == 1 or 2 == 1:  # can be cmopared to || in JavaScript
    print("one of the conditions is true")
if not 1 == 2:  # can be compared to ! in JavaScript
    print("the condition was not true but it was reversed so evaluated as true")

# identity operators [7.5]
"""
    - Identity operators are used to compare objects, not for the equality of their values, but if 
    they are actually the same object with the same memory location: {
        is : returns True if both variables are the same object
        is not : returns True if both variables are NOT the same object
    }
"""
first_object = ["Hello", "World"]
second_object = ["Hello", "World"]
third_object = first_object
print(first_object is third_object)         # prints True
print(first_object is second_object)        # prints False
print(first_object is not second_object)    # prints True
print(first_object == second_object)        # prints True

# membership operators [7.6]
"""
    - Membership operators are used to test if a sequence is presented in an object: {
        in : returns True if a sequence with the specified value is present in the object
        not in : returns True is a sequence with the specified value is NOT present in the object
    }
"""
food = ["Apple", "Banana", "Tomato"]
print("Apple" in food)  # prints True
print("Humus" in food)  # prints False
print("Pineapple" not in food) # prints True

# NOTE, the bitwise operators lesson will be skipped for now




# Lists [8]
# intro to lists [8.1]
"""
    - Lists are used to store multiple items in a single variable
    - Lists can be compared to arrays in JavaScript
    - There are 4 data-types that can store collections of data in python, lists are one of them, others 
    are tuples, sets, and dictionaries, each with its different qualities
    - Lists are created using square brackets
"""
# creating a simple list
first_list = ["red", "green", "blue"]  # created a list that contains three items
print(first_list)  # prints ['red', 'green', 'blue']
# finding the length of a list (number of items in a list)
my_list = ["one", "two", "three", "four"]  # a list with four items
print(len(my_list))  # the len() function can be used to find the length of a list, or the number of items inside it
# lists can contain any data-type, it can even contain other lists
list_of_names = ["Python", "JavaScript", "PHP", "Java"]
list_of_numbers = [12, 4, 2022, 0, 999]
list_of_bools = [True, False, False, True]
list_of_mixed = ["Heya!", 2022, 3.14, True]
nested_list = [["Python", 1991], ["JavaScript", 1995], ["PHP", 1994]]  # even more nesting is possible
# printing list type
print(type(my_list))  # this will print <class 'list'> as we learned in previous lessons
# the list() constructor
"""
    Lists can be created using the list() constructing function
"""
constructed_list = list(("House", "School", "Hospital"))  # notice how we used parenthesis and not square brackets

# properties of lists [8.2]
"""
    - Each collection type has its own properties, the list properties are: {
        1- ordered: they have a defined order that will not change unless we change it, lists are indexed
        2- changeable: list items can be added, removed, or modified after creating a list
        3- allows duplicate values: since lists are indexed, they can have items with identical values
    }
"""
# ordered
list_1 = ["Apple", "Banana", "Watermelon"]  # "Apple" is always the first item, "Watermelon" is always the last
# changeable as in later lessons we will learn how to add, remove, or modify list items in a list
# allows duplicate values
list_2 = ["Apple", "Banana", "Apple", "Watermelon", "Banana", "Apple"]  # this is a valid list

# accessing list items [8.3]
"""
    - As we learned before, lists are ordered and indexed
    - Each list item has an index that you can use to access the item and get it or change it
    - Remember how we accessed string characters using square brackets, same applies with lists but this time 
    we will be accessing items instead of characters
    - Remember, in programming, counting indexes starts from 0 and not from 1
"""
access_list = ["Item one", "Item two", "Item three"]
print(access_list[0])  # prints the first list item "Item one"
print(access_list[1])  # prints the second list item "Item two"
print(access_list[2])  # prints the third list item "Item three"
# accessing items backwardly (negative indexing)
print(access_list[-1])  # prints the last item
print(access_list[-2])  # prints the second last item
# range of indexes (getting a group of list items)
long_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(long_list[2:5])  # gets and prints a list of items from item of index 2 to item of index 4 (5 is excluded)
print(long_list[:4])  # by leaving out the first index, the range will start at the first item
print(long_list[2:])  # by leaving out the last index, the range will end at the last item
# you can use negative values to start the cut from the end of the list (backwardly)
print(long_list[-4:-1])  # this is a valid example
# you can use the "in" keyword to check if an item exists in a list
print("apple" in long_list)  # this prints True
print("joemama" in long_list)  # this prints False

# changing list items [8.4]
"""
    - Consider the list items normal variables, can't you overwrite variable's values?
    - The same way you can overwrite variable's values, you can overwrite list items, remember to refer to their index
"""
cars_list = ["Nissan", "Toyota", "BMW", "Mercedes"]
cars_list[0] = "Ferrari"  # this will overwrite "Nissan" to "Ferrari"
# you can also change a range of items
cars_list[0:3] = ["Kia", "Bugatti", "Honda"]  # like this, we modified the first 3 items in the list
"""
    - If you insert more items than you replaced, the new items will be inserted here you specified, and 
    tge remaining items will move accordingly, so their indexes will change, and the length of the list will increase.
    - You might also insert less items than you replaced, so the remaining items will also move accordingly, 
    and the length of the list will decrease.
"""
cars_list[1:2] = ["Hyundai", "Jeep"]  # we replaced one item with 2 items

# adding list items [8.5]
"""
    - There are multiple ways you can use to add list items, each with its own abilities.
"""
# append()
append_list = ["one", "two", "three"]
append_list.append("four")  # this will add item "four" to the end side of the list
# insert()
insert_list = ["1", "2", "3"]
insert_list.insert(1, "1/2")  # this will add the item in the specified index, so you can control where to add
# extend()
extend_list1 = ["one", "two", "three"]
extend_list2 = ["four", "five", "six"]
extend_list1.extend(extend_list2)  # this will add the items of extend_list2 to the end side of extend_list1
"""
    Note: the extend() method does not have to add lists, it can add any iterable object (tuples, sets, dictionaries)
"""

# removing list items [8.6]
"""
    - There are multiple methods you can use to remove list items as well
"""
# remove()
remove_list = ["apple", "banana", "tomato"]
remove_list.remove("apple")  # this will remove the first occurrence of "apple" item from the list
# pop()
pop_list = ["one", "two", "three", "imposter", "four"]  # remove the imposter using it's index
pop_list.pop(3)  # this will remove the item of index 3 in the list
pop_list.pop()  # if you did not specify the index in the pop() method, it will remove the last item in the list
# del
del_list = ["Swordax", "Sy"]
del del_list[0]  # the del keyword can remove the specified list item through its index
del del_list  # the del keyword can also delete the whole list completely if no index was specified
# clear()
clear_list = ["filled list", "list is filled"]
clear_list.clear()  # the clear() method clears out he list and empties it, the list is still there but with no content

# looping through lists [8.7]
"""
    - We can loop through lists by using the for loop (for loops will be discussed in details in later lesosns)
"""
# looping using the "in" keyword
loop_list = ["Swordax", "Swordy", "Sword", "SRDX", "SRD"]
for item in loop_list:
    print(item)
# the previous example will print each item inside the list
"""
    Explanation: {
        - declared the for loop using the "for" keyword
        - specified the variable name that we will be using for each item, in this example we named it "item"
        - used the "in" keyword and then specified the list we will loop through
        - inside the for statement block, we will do whatever we need to do
        - throughout the iterations, we can access the current item we are iterating through using the 
        variable we specified in the for statement, "item" in our case
    }
"""
# looping through index numbers
for i in range(len(loop_list)):
    print(loop_list[i])
# the previous example will print each item inside the list
"""
    - Another way of looping through lists with having access to the current iterated item index is by using 
    the range(), (will be explained more in details in later lessons)
    - Explanation: {
        - declared the for loop using the "for" keyword
        - specified the variable name that we will be using for each item, in this example we named it "i"
        - used the "in" keyword and then used a range() to provide a list of numbers to loop through
        - there numbers we will be looping through will represent the index of each item in the list
        - we will have access to the current number (index) we are looping through using the variable "i"
        - we passed in the range() the length of the list we want to loop through to know how many times to iterate
        - we can now access the indexes of the list items inside the for loop block by using the variable "i"
    }
"""
# looping through list using a while loop
ind = 0  # a variable that will represent the current index of the item inside the loop
while ind < len(loop_list):  # declaring a while loop and setting the condition to be (if ind is less than list length)
    print(loop_list[ind])  # printing the current iterated item (accessing items through their indexes using "ind")
    i += 1  # incrementing the value of "ind" variable to complete the loop logic
# we will learn more about the while loops in later lessons

# list comprehension [8.8]
"""
    - List comprehension offers shorter syntax when you want to create a new list based on the values of an existing one
    - Syntax: {
        new_list = [*expression* for *item* in *iterable* if *condition* == True]
    }
    - List comprehension will create a new list, the original list wont be affected
    - *condition* is like a filter that only accepts items that valuate to True
    - The condition is optional and can be omitted, this would result in making an exact copy of the original list
    - *iterable* can be any iterable object, like a list, tuple, set, etc..
    - *expression* is like a variable containing the current item we are iterating through
"""
# example: you want to create another list containing the items of another list, the ones that contain letter "a" only
existing_list = ["apple", "banana", "melon", "avocado", "kiwi"]
new_list = [x for x in existing_list if "a" in x]  # list comprehension (this would do the job)
# the expression can be manipulated before going through the list comprehension
list_example = [1, 2, 3]
newlist = [x * 2 for x in list_example]  # this would make a new list with items from the original list all timed by 2
# you can even specify the expression as a static value
list_example_2 = [1, 2, 3]
newlist2 = ["yes" for x in list_example_2]  # this would make a new list with 3 items all being "yes"
# you can even do this:
list_example_3 = ["apple", "banana", "orange"]
newlist3 = [x if x != "orange" else "imposter" for x in list_example_3]  # guess what it does!
# the expression in the example above states: return the item if its not "orange" otherwise return "imposter"

# sorting lists [8.9]
"""
    - You can use the sort() method to sort a list alphanumerically, ascending by default
"""
sort_list = ["orange", "mango", "kiwi", "pineapple", "apple", "banana"]  # un-sorted list
sort_list.sort()  # this will sort the list alphanumerically
sort_list2 = [100, 60, 40, 50, 20, 10, 30]  # un-sorted list
sort_list2.sort()  # this will sort the list numerically (since its made of numbers only)
# in case you wanted to sort in a descending order:
sort_list3 = ["Boy", "Apple", "Cat", "Zoo", "Milk"]
sort_list3.sort(reverse=True)  # pass this argument in the sort() method to reverse the sorting (descending order)
# same as the above applied to numeric sorting (numbers will sort in a descending order)
"""
    - You can do your own sorting logic by passing a key argument in the sort() method
"""
def myCustomSortFunc(n):
    # you can pass your own sorting logic in here
    return n
sort_list4 = [1, 2, 3, 4, 5, 6, 7, 8]
sort_list4.sort(key=myCustomSortFunc)
"""
    - the sort() method by default sorts lists case sensitively, returning all capital letters before lower case letters
    - sometimes you might want to do case-insensitive sorting, you can use a built in function as a key argument 
    in the sort() method to achieve that, which is the str.lower built in function
"""
sort_list5 = ["Hello", "hi", "Hide", "Sort me", "sorting process", "small s"]
sort_list5.sort(key=str.lower)  # this will perform a case-insensitive sorting
"""
   - you can reverse the order of the list items in python using the reverse() method
   - the reverse() method will reverse the list regardless of the alphabet
"""
reverse_list = ["a", "b", "c", "d"]
reverse_list.reverse()  # this will sort the list as the following: ["d", "c", "b", "a"]

# copying lists [8.10]
"""
    - you cannot copy a list by saying "list1 = list2" in python, because that will just create an instance 
    of list1 under the name of list2, and changes on list2 will apply on list1 as well.
    - there are multiple valid ways to copy a list in python, here they are:
"""
copy_list = ["Swordax", "Sword", "Axe"]  # original list to be copied
copy_list2 = copy_list.copy()  # using the copy() method
copy_list3 = list(copy_list)   # using the list() method

# joining lists in python [8.11]
"""
    - you might sometimes need to join/concatenate lists together
    - in python, there are many ways to achieve that, here they are:
"""
# using the + operator
list1 = ["a", "b", "c"]
list2 = ["d", "e", "f"]
list3 = list1 + list2  # joining 2 lists in a 3rd one
# using a for loop and the append() method
_list1 = ["a", "b", "c"]
_list2 = ["d", "e", "f"]
for x in _list2:
    _list1.append(x)  # appending all the _list2 items inside _list1
# using the extend() method
list1_ = ["a", "b", "c"]
list2_ = ["d", "e", "f"]
list1_.extend(list2_)  # extending items of list2_ inside list1_

# list methods reference [8.12]
"""
    - As seen in the previous lessons, there are many methods that you can use with lists to do various things, 
    and here is a full reference of them.
"""
l = ["a", "b", "c"]
# list methods
l.append()      # adds an item at the end of the list (item)
l.clear()       # removes all items from the list
l.copy()        # returns a copy of the list
l.count()       # returns the number of items with the specified value (value)
l.extend()      # adds the items of a list or any iterable object to another list (iterable)
l.index()       # returns the index of the first item with the specified value (value)
l.insert()      # adds an element t the specified position (element, position)
l.pop()         # removes the element at the specified position (position)
l.remove()      # removes the item with the specified value (value)
l.reverse()     # reveres the order of the list
l.sort()        # sorts the array




# Tuples [9]
# intro to tuples [9.1]
"""
    - Tuples in python are used to store multiple items in a single variable
    - Tuples are like lists but with differences in behaviour, quality, and usage
    - Unlike lists, tuples are created using parenthesis instead of square brackets
"""
my_first_tuple = ("apple", "banana", "cherry")  # this how to create a tuple
print(my_first_tuple)  # prints: ('apple', 'banana', 'cherry')
# like lists, tuples items are ordered, and they have indexes (count starting from 0)
# so the first item has the index [0], the second has the index [1] .. etc..

# properties of tuples [9.2]
"""
    - Like lists, tuples have their own properties: {
        1- ordered: tuple items have a defined order, and that order will not change, tuple items are indexed
        2- unchangeable: tuples are unchangeable, meaning that we cannot change, add, or remove items inside a tuple
        3- allow duplicates: like lists, since items are indexed, then duplicate items with similar values are allowed
    }
"""
ordered_tuple = ("one", "two", "three")  # this defined order of items will not change
unchangeable_tuple = ("static value", "static item")  # trying to change, add, or remove items will result in an error
duplicatable_tuple = (True, False, True, False)  # tuples can have items with identical values
# you can use the len() method to find the number of items inside a tuple
three_items = ("item one", "item two", "item three")
print(len(three_items))  # this should print 3
"""
    - If you want to create a tuple with one item only, you will have to add a comma after the item, otherwise 
    python will not recognize it as a tuple.
"""
single_item = ("single item",)  # this is how to create a tuple with a single item
# like lists, tuples can contian any data type, or even a mix of them
datatypes_tuple = ("string", 2022, True, ["lists"], ("other tuples",))
# using the type() function with a tuple will return the following: <class 'tuple'>
print(type(datatypes_tuple))  # prints: <class 'tuple'>
# using the tuple() constructor
"""
    - Like lists and any other data-type, you can use constructors to create tuples.
    - A tuple constructor function is: tuple()
"""
constructed_tuple = tuple(("apple", "orange", "banana"))  # created a tuple using a tuple() constructor
# looping through tuples
"""
    - You can loop through tuples the exact same way you loop thorugh lists
"""

# accessing tuple items [9.3]
"""
    - You can access the tuple items exactly as you do in lists, by referring to their index in a square bracket
    - Remember to start counting from 0
"""
access_tuple = ("first", "second", "third")
print(access_tuple[0])  # this will print the first item in the tuple
print(access_tuple[-1])  # this will print the last item in the tuple (indexing backwardly)
# range of indexes (just like in lists)
print(access_tuple[0:2])  # from index 0 to index 1 (2 excluded) prints: ('first', 'second')
print(access_tuple[:1])  # skipping the first index, the range will start from the first item
print(access_tuple[2:])  # skipping the last index, the range will at the last item
# negative range of indexes work too, its just identical to lists!
# check if item exists in a tuple:
print("i dont exist" in access_tuple)  # prints: False
print("first" in access_tuple)  # prints: True

# updating tuples [9.4]
"""
    - As we mentioned before, tuples are unchangeable, means you cannot straight-forwardly add, remove, or change 
    items, but there are some workarounds to update tuples in various ways.
    - Remember that we can always overwrite a variable and give it a whole new value, even if it was a tuple.
"""
# change an item in a tuple
tup = ("apple", "banana", "cherry")
lst = list(tup)
lst[2] = "orange"
tup = tuple(lst)
"""
    - Hopefully its easy to understand.
    - What happened is basically we created a list with the exact same content as the tuple, then we modified 
    the list, which is legal, and then we overwrote the tuple with a tuple that has the exact same content as the list
    - Smart ain't it ;)
"""
# add items
"""
    - As we just introduced the idea of creating lists, modifying them, and then replacing the old tuple with the 
    modified list, then it should be easy to understand how we can use all the list methods on the copy list, and 
    then overwrite the tuple with the list.
    - Here is an example of how we can add items to a tuple by using the list method append()
"""
my_tup = ("chocolate", "juice", "milk")
my_lst = list(my_tup)
my_lst.append("water")
my_tup = tuple(my_lst)  # how easy :)
# join tuples
"""
    - Another way of adding items into a tuple, is my joining two tuples together, which is legal with tuples.
"""
tup_ = ("one", "two", "three")
_tup = ("four",)  # don't forget to add a comma after the item in a single item tuple!
tup_ += _tup  # this works fine!
"""
    - As you have seen in the previous examples, we can create a list copy of the tuple, use all the available 
    list methods we can use, and then overwrite the tuple with a new tuple containing the copy list.
    - You can use this idea to remove items, add items, or change items in a tuple.
"""
# delete a tuple using del keyword
"""
    - Remember the del keyword that we used to delete a list? it can be used to completely delete a tuple
"""
delete_tuple = (True, False)
del delete_tuple  # this will delete the tuple completely
# unpacking tuples

# unpacking tuples [9.5]
"""
    - Remember taking the unpacking idea in the variables lesson in chapter 2? it was demonstrated using a list, 
    but you should know that we can do that with tuples as well!
"""
unpack_tup = ("yes", "no", "maybe")
(confirm, refute, unsure) = unpack_tup
print(contirm)  # prints "yes"
print(refute)  # prints "no"
print(unsure)  # prints "maybe"
# remember that the number of variables used in unpacking should be identical to the number of items in the tuple
"""
    - If the number of variables was less than the number of values in the tuple, you can use the * sign with 
    one of the variables to identify that this variable will be a list that will collect all the left items
"""
unpack_tuple = ("blood", "grass", "sky", "ocean", "bluish eyes")
(red, green, *blue) = unpack_tuple
print(red)  # prints: "blood"
print(green)  # prints: "grass"
print(blue)  # prints: ['sky', 'ocean', 'bluish eyes']
unpack_tp = ("Mercedes", "Airbus", "Boeing", "Samsung")
(cars, *airplanes, mobiles) = unpack_tp
print(cars)  # prints: "Mercedes"
print(airplanes)  # prints: ['Airbus', 'Boeing']
print(mobiles)  # prints: "Samsung"

# joining tuples [9.6]
"""
    - It is legal to join/concatenate two tuples with each other using the + operator, as shown previously
"""
tup_1 = ("hello",)
tup_2 = ("world",)
tup_3 = tup_1 + tup_2
print(tup_3)  # prints: ('hello', 'world')
# multiplying tuples (can be done with lists too)
tup1 = ("apple", "banana", "orange")
print(tup1 * 2)  # prints: ('apple', 'banana', 'orange', 'apple', 'banana', 'orange')

# tuple methods [9.7]
"""
    - two methods you can use with tuples: {
        count() : returns the number of times a specified value occurs in a tuple (value)
        index() : returns the index where a specified value was found in a tuple
    }
"""




# Sets [10]
# intro to sets [10.1]
"""
    - Sets are another data-type that allows use to store multiple items in a single variables.
    - Sets are similar to lists and tuples in the idea of storing multiple items in a single variable, 
    but it has a different behaviour, quality, and usage.
    - Sets are created using curly-brackets {}, unlike lists [] and tuples ()
"""
my_first_set = {"apple", "banana", "cherry"}  # as simple as that, we created a set

# set properties [10.2]
"""
    - As every other collection data-type, set has its own properties: {
        - unordered: unlike previous collection data-types we took, sets are unordered, which means un-indexed as well
        - unchangeable: items in a set cannot be changed just like in tuples, but unlike tuples, set items can be 
        added or removed
        - duplicates not allowed: since sets are not indexed, set items cannot have the same value
    }
"""
my_set = {"apple", "orange", "banana", "apple"}
print(my_set)  # prints: {'orange', 'banana', 'apple'} (order is not static and could be different if code runs again)
# as you can notice, it only prints one "apple" and ignores the other
# since sets are not ordered, you cannot be sure on what order the items will appear when printing them
print(len(my_set))  # we can use the len() function on sets as well, prints: 3 (duplicates count as 1)
"""
    - Similar to lists and tuples, sets can also contain any data type, like strings, integer, floats, booleans, 
    lists, tuples, or even other sets, and any other data type
"""
set_of_numbers = {1, 2, 3, 3, 4, 5}
set_of_booleans = {True, False}
set_of_mixed = {1, 3.14, "Swordax"}
# get et type
print(type(my_set))  # prints: <class 'set'>
# sets can also be created using the set() constructor
constructed_set = set(("apple", "banana", "cherry", "orange"))
print(constructed_set)  # prints: {'cherry', 'banana', 'orange', 'apple'}

# accessing set items [10.3]
"""
    set items cannot be accessed using an index or a key, but as a workaround, you can loop though a set and 
    check for the value to get it
"""
access_set_item = {"Swordax", "Sword", "Axe", "Swordy"}
for x in access_set_item:
    if x == "Swordax":
        print("I found Swordax!")
# check if an item exists in the set
print("Swordax" in access_set_item)  # prints: True
print("NULL" in access_set_item)  # prints: False
"""
    - Important rule of sets: as a set is created, items cannot be changed/modified, but only added or removed
"""

# add set items [10.4]
"""
    - As you studied in previous set lessons, set items cannot be changed or modified, but only added or removed
"""
# set() method
# we can add an item to a set by using the set() method
add_set = {"water", "milk", "juice"}
add_set.add("ice")
print(add_set)  # prints: {'ice', 'milk', 'juice', 'water'} (remember, non static un-predicted order, could change)
# update() method
# we can add items from another set to a set by using the update() method
update_set1 = {"old", "historic", "before"}
update_set2 = {"new", "modern", "after"}
update_set1.update(update_set2)
print(update_set1)  # prints: {'old', 'modern', 'after', 'historic', 'new', 'before'}
# note: the object passed in the update() method doesn't have to be another set, could be any iterable object, ex: list

# remove set items [10.5]
"""
    - We can also delete items from a set by using multiple methods
"""
# remove() method
remove_set = {"Swordax", "Sword", "Axe", "Imposter"}
remove_set.remove("Imposter")  # deletes the "Imposter" item from the set
# note: if the item passed in the remove() method doesn't exist in the set, remove() will raise an error
# discard() method
discard_set = {"Swordax", "Sword", "Axe", "Imposter"}
discard_set.discard("Imposter")  # deletes the "Imposter" item from the set
# note: if the item passed in the discard() method doesn't exist in the set, discard() wont raise an error like remove()
# pop() method
pop_set = {"Swordax", "Sword", "Axe"}
pop_set.pop()  # deletes the last item in the set
# note: since sets are unordered and the order cannot be expected, the pop() method will delete an unknown item
# clear() method
clear_set = {"Swordax", "Sword", "Axe"}
clear_set.clear()  # clears out the whole set and empties it
# del keyword
del_set = {"Swordax", "Sword", "Axe"}
del del_set  # deletes the whole set completely

# joining sets [10.6]
"""
    - There is a number of methods that can be used to join sets in different ways
    - note: the following variables set1 and set2 will be used in many examples using many methods that will 
    all affect them throughout the examples, so if you ran the code, expect to see a mess
"""
set1 = {"Swordax", "Sword", "Axe"}
set2 = {"Swordax", "Swordy", "SRDX"}
# union() method: returns a new set with all items from both sets
set3 = set1.union(set2)
# update() method: inserts items from set2 into set1
set1.update(set2)
# intersection_update() method: keeps only the items that are present in both sets
set1.intersection_update(set2)
# intersection() method: returns a new set containing the items that are present in both sets
set4 = set1.intersection(set2)
# symmetric_difference_update() method: keeps only the elements that are NOT present in both sets
set1.symmetric_difference_update(set2)
# symmetric_difference() method: returns a new set containing the items that are NOT present in both sets
set5 = set1.symmetric_difference(set2)

# set methods [10.7]
"""
    - We have studied a number of set methods in the previous lesson, here is a reference to them: {
        add(): adds an item to the set
        clear(): removes all the items from the set
        copy(): returns a copy of the set
        difference(): returns a set containing the difference betwen two or more sets
        difference_update(): removes the items in this set that are also included in another
        discard(): removes the specified item
        intersection(): returns a set that is the intersection of two other sets
        intersection_update(): removes the items in this set that are not present in other specified set(s)
        isdisjoint(): returns whether two sets have a intersection or not
        issubset(): returns whether another set contains this set or not
        issuperset(): returns whether this set contains another set or not
        pop(): removes the last item from the set
        remove(): removes the specified item from the set
        symmetric_difference(): returns a set with the symmetric difference from this set and another
        symmetric_difference_update(): inserts the symmetric differences from this set and another
        union(): returns a set containing the union of sets
        update(): update the set with the union of this set and others
    }
"""




# Dictionaries [11]
# intro to dictionaries [11.1]
"""
    - Dictionaries is another data-type used to store multiple values in a single variable
    - A dictionary stores data values in a key:value pairs
    - A dictionary is an object in JavaScript
"""
my_first_dictionary = {
    "name": "Swordax",  # can contain strings
    "name_length": 7,   # can contain numbers
    "married": False,   # can contain booleans
    "languages": ["Arabic", "English"],  # can contain collections
    "cars": {           # can contain nested dictionaries
        "mercedes": 2022,
        "bmw": 2022,
        "isTrue": False
    }
}
# you can determine how many items the dictionary has by using the len() function
print(len(my_first_dictionary))  # prints: 5

# properties of dictionaries [11.2]
"""
    - As other collection data-types, dictionaries have properties too: {
        - ordered: items in a dictionary have a defined order that will not change
        - changeable: items in a dictionary can be changed, added, or removed
        - duplicates not allowed: dictionary items cannot share the same key, but can have the same value
    }
"""
# dictionary items can be from any data-type, like string, integers, floats, lists, etc..
mycar = {
    "brand": "BMW",     # strings
    "model": "M5",
    "year": 2022,       # integers
    "used": False,      # booleans
    "kilometers": 0.0,  # floats
    "colors": ["white", "black"]  # lists
}
# getting a dictionary type:
print(type(mycar))  # prints: <class 'dict'>

# access dictionary items [11.3]
"""
    - you can access/get a dictionary item value by referring to its key name in two main ways: {
        - square-brackets: dictname["keyname"]
        - get() method: dictname.get("keyname")
    }
"""
langs = {
    "arabic": "middle-east",
    "english": "america",
    "german": "germany",
    "russian": "russia"
}
# square brackets
arabic_area = langs["arabic"]
# get() method
english_area = langs.get("english")
"""
    - You can get a list of all the keys available inside a dictionary using the keys() method
    - the list of the keys is a view of the dictionary, which means that any change that occurs to the dictionary 
    will be reflected in the keys list
"""
keys_list = langs.keys()  # any change will be reflected in the variable
print(keys_list)  # prints: dict_keys(['arabic', 'english', 'german', 'russian'])
"""
    - you can get a list of all the values inside a dictionary by using the values() method
    - the list of values is a view of the dictionary, which means that any change that occurs to the dictionary 
    will be reflected in the values list
"""
values_list = langs.values()
print(values_list)  # prints: dict_values(['middle-east', 'america', 'germany', 'russia'])
"""
    - you can get a list if all the items inside a dictionary by using the items() method
    - the list if items is a view of the dictionary, which means that any change that occurs to the dictionary 
    will be reflected in the items list
    - the items list will be in the following syntax: [("key", "value"), ("key", "value")] which means that its a 
    list containing a collection of tuples, each tuple contains the key and the value as items
"""
items_list = langs.items()
print(items_list)
# prints: dict_items([('arabic', 'middle-east'), ('english', 'america'), ('german', 'germany'), ('russian', 'russia')])
"""
    - you can get if a key exists in a dictionary by using the "in" operator
    - this information then can be used in if statements to check if a key exists in a dictionary or not
    - note: you will learn about if statements and conditionals in later lessons
"""
print("arabic" in langs)  # prints: True
print("NULL" in langs)  # prints: False

# change dictionary items [11.4]
"""
    - you can change the value of a specific item by referring to its key name and overwrite its value
    - check the following example:
"""
car = {
    "brand": "BMW",
    "model": "M4",
    "year": 2022
}
car["model"] = "M5"  # this will change the value if the "brand" key in the "car: dictionary to "M5"
print(car["model"])  # prints: "M5"
"""
    - you can update a dictionary using the update() method
    - the argument to that method (what you pass in the parenthesis) should be a dictionary, or an iterable object 
    with key:value pairs
"""
car.update({"model": "M3"})  # this will change the value of "model" to "M3"
changes = {
    "brand": "Mercedes",
    "model": "S300",
    "year": 2020
}
car.update(changes)  # this will change all the "car" dictionary content

# add dictionary items [11.5]
"""
    - you can add an item to the dictionary the same way you update items in it, thing is, when updating you 
    are just overwriting an existing one, but when creating, since there isn't one, it wont be overwriting but will be 
    setting a new one.
"""
my_car = {
    "brand": "BMW"
}
# using the square brackets
my_car["model"] = "M5"  # created a new item inside the dictionary with the key "model" and a value of "M5"
# using the update() method
my_car.update({"year": 2022})  # created a new item inside the dictionary with the key "year" and a value of 2020

# removing dictionary items [11.6]
"""
    - there are several methods to remove items from a dictionary
"""
cars_dict = {
    "mercedes": 2016,
    "bmw": 2018,
    "toyota": 2006,
    "honda": 2021,
    "nissan": 2019
}
# removing methods
cars_dict.pop("honda")      # pop() method removes the item with the specified key name
cars_dict.popitem()         # popitem() method removes the last inserted item
del cars_dict["nissan"]     # del keyword removes the item with the specified key name
cars_dict.clear()           # clear() method empties the whole dictionary
del cars_dict               # del keyword can also delete a whole dictionary completely

# looping through dictionaries [11.7]
"""
    - you can loop through a dictionary using a for loop
    - when looping through the dictionary itself, we will get the keys of the items inside it, but there are 
    other ways we could get the values of the items
"""
ex_dict = {
    "name": "somedude",
    "age": "123",
    "nationality": "mars"
}
# loop through keys
for x in ex_dict:
    print(x)  # printing the keys inside the dictionary
    print(ex_dict[x])  # printing the value of the current key
# loop through values
for x in ex_dict.values():
    print(x)  # printing the values inside the dictionary
# loop through keys and values
for x, y in ex_dict.items():
    print(x)  # printing the keys inside the dictionary
    print(y)  # printing the values inside the dictionary

# copy dictionaries [11.8]
"""
    - you cannot make a copy of a dictionary by doing dict2 = dict1 because that will just create a reference to the 
    original dictionary and not a copy of it
    - one way to copy a dictionary, use the copy() method
    - another way to copy a dictionary, use the dict() function
"""
my_dict = {
    "name": "Swordax",
    "type": "human"
}
my_dict_copy1 = my_dict.copy()
my_dict_copy2 = dict(my_dict)

# dictionary methods [11.9]
"""
    - there is a number of built-in functions and methods that can be used with dictionaries, and here is a 
    list of them as.
"""
dct = {"happy": False}
# dictionary methods
dct.clear()         # removes all the elements form the dictionary
dct.copy()          # returns a copy of a dictionary
dct.fromkeys()      # returns a dictionary with the specified keys and values
dct.get()           # returns the value of the specified key
dct.items()         # returns a list containing a tuple for each key value pair
dct.keys()          # returns a list containing all the keys inside the dictionary
dct.pop()           # removes the elements with the specified key
dct.popitem()       # removes the last inserted element
dct.setdefault()    # returns the value of the specified key, if doesn't exist, inserts the key with the specified value
dct.update()        # updates the dictionary with the specified key-value pairs
dct.values()        # returns a list of all the values in the dictionary




# Conditional If Statement [12]
# intro to python conditionals [12.1]
"""
    - In programming, a very popular concept is the conditional statements.
    - In this chapter, we will be studying about the python's if..else statements.
    - Python supports the usual logical conditions used in mathematics: {
        a == b  : Equals
        a != b  : Not Equal
        a < b   : Less Than
        a > b   : More Than
        a <= b  : Less Than or Equal
        a >= b  : More Than or Equal
    }
    - These operators will be used most commonly in conditional if statements
    - A conditional if statement is declared using the "if" keyword
    - Syntax: {
        if True:
            # run code block
        # rest of code
    }
    - The indentation specifies the if statement's code block, all lines inside the block should have same indent.. size
"""
# example one
if True:
    print("If the condition evaluates to true, I will be printed!")
# example two
val_a = 100
val_b = 200
if val_a < val_b:
    print("val_a is less than val_b")

# the elif statement [12.2]
"""
    - the elif statement stands for "else if"
    - the elif statement basically says, if the previous condition wasn't true, try this one
    - the elif statement will only run if the previous conditions evaluated to false
"""
_a == 1
if _a > 1:
    print("_a is more than 1")
elif _a < 1:    # if the condition above me wasn't true, I will be tried
    print("_a is less than 1")
elif a == 1:    # if the condition above me wasn't true, I will be tried
    print("_a is equal to 1")

# the else statement [12.3]
"""
    - we learned that if condition is true, do this, else, do that
    - we also have a keyword that says, else, do that
    - the "else" keyword catches anything which isn't caught by the preceding conditions
    - if the condition was true in any of the preceding conditions, else doesn't run, otherwise, it runs
    - if all the previous conditions evaluated to false, the else statement block of code will always run
"""
# example one
_b = 1
if _b == 4:
    print("_b is equal to 4")
elif _b == 3:
    print("_b is equal to 3")
elif _b == 2:
    print("_b is equal to 2")
else:
    print("_b is not 4, not 3, not 2")
# example two
_c = 20
_d = 40
if _c > _d:
    print("_c is greater thn _d")
else:
    print("_c is NOT greater than _d")

# shorthands and ternary operators [12.4]
"""
    - shorthand if
    - the shorthand if is a way to simplify an if statement if you had only one statement to execute inside the block
"""
if _a > _b: print("_a is more than _b")
"""
    - shorthand if else (ternary operator)
    - another way to simplify your code if you had only one if and one else, and only one statement to run for each
"""
print("1 is greater than 2") if 1 > 2 else print("1 is NOT greater than 2")
# this is known as a ternary operator, it could be more complex and nested with more conditions
print("1 is greater than 2") if 1 > 2 else print("1 is equal to 2") if 1 == 2 else print("1 is less than 2")
# the above could be more nested with more conditions as much as you want/need it to be

# logical operators in conditionals [12.5]
"""
    - you might need more checks in a single conditional statement
    - you can use python's logical operators to add more logic to your condition: {
        and: the "and" operator/keyword can be used to check if *condition* and *condition* are true
        or: the "or" operator/keyword can be used to check if *condition* or *condition* is true
    }
"""
j = True
k = True
if j and k:
    print("j and k evaluated to True!")
if j or k:
    print("j or k evaluated to True!")
"""
    you can use the "not" keyword to reverse your condition's result
"""
if not j:
    print("j is False but the not keyword reversed the result")

# nested if statement [12.6]
"""
    - Sometimes you will need to write deeper and more complex logic, there is when you will need nesting
    - You can always nest programming statements and logic, including the if statements, which will be shwon here
"""
mynum = 100
if mynum > 10:
    print("above 10!")
    if mynum > 20:
        print("above 20!!")
        if mynum > 30:
            print("above 30!!!")
        else:
            print("not above 30")
"""
    * fast information!
    - An if statement code block cannot be empty, but if you sometime for some reason ever needed to create 
    an empty if statement, you should use the "pass" keyword to avoid getting errors 
"""
if 1 == 1:
    pass  # this wont do anything, it just lets you have an empty if statement code block




# While Loops [13]
# intro to loops in python [13.1]
"""
    - Loops are another core and main subject in programming
    - Python has two primitive loop commands: {
        1- while loops
        2- for loops
    }
    - A loop is a block of code that will keep running over and over till it's job is done
    - The code that comes after the loop will not run until the loop is completed
"""
while 1 == 2:
    print("Life is broken")  # this would never run because 1 is not equal to 2

# what are while loops [13.2]
"""
    - the while loop is declared using the "while" keyword
    - the while loop should be provided with a condition
    - as long as the condition evaluates to True, the code inside the while block will keep running over and over
    - the code that comes after the while statement will not run until the loop is completed and finished
    - as soon as the loop condition evaluates to false, the code will continue
    - the while loop can be used to do a task a number of times
"""
# example one
while_condition = True
while while_condition:  # if while_condition evaluates to true, the while block will run, otherwise, it will be skipped
    print("worked!")  # this is a part of the while statement code block
    while_condition = False  # as soon as the loop starts, the condition will be turned to false
# because of the previous logic, the loop will only run ones and then it will be finished
# example two
_a_ = 0
while _a_ < 10:
    # this block of code will run 10 times
    print(_a_)  # on each loop run, the current value of _a_ will be printed
    _a_ += 1  # on each loop run, the value of _a_ will be incremented by 1
# understanding the above code should be easy

# break statement [13.3]
"""
    - the break statement can be used in any kind of loops, whether while or for loops
    - the break statement ends the loop even if the condition provided is still true
"""
_b_ = 0
while _b_ < 6:
    print(_b_)
    if _b_ == 3:
        break  # so when _b_ is 3, the loop will finish, even though the while condition is still True
    _b_ += 1

# the continue statement [13.4]
"""
    - the continue statement can be used in any kind of loops, whether while or for loops
    - the continue statement skips the current iteration and moves to the next one
"""
_c_ = 0
while _c_ < 6:
    _c_ += 1
    if _c_ == 3:
        continue
    print(_c_)
# the previous code will print numbers from 1 to 6 BUT number 3 wont be printed because it was skipped by "continue"

# the while else statement [13.5]
"""
    - remember the else statement in the conditionals? it can be used in while loops
    - the else statement code will run as soon as the while condition is no longer true
    - the else statement will NOT run if the while loop was cut by a break statement
"""
_d_ = 0
while _d_ < 6:
    _d_ += 1
    print(_d_)
else:
    print("_d_ is no longer less than 6, loop ended and a break statement was NOT used!")

# the pass statement in while loops [13.6]
"""
    - Remember the "pass" statement we learned about in the last chapter with if statements?
    - A pass statement can also be used in while loops when we want to create an empty one
"""
while False:
    pass




# For Loops [14]
# intro to for loops [14.1]
"""
    - The second type of loops in python, the for loops
    - A for loop is declared using the "for" keyword
    - A for loop is used to iterate over a sequence
    - A for loop can be used to iterate through collections (lists, tuples, sets, dictionaries) or even strings
    - Using a for statement, we can execute a block of code once for each item in a collection, or for each 
    character inside a string
"""
# example one
loop_through_string = "Hello world!"
for char in loop_through_string:  # "char" is a variable that contains the current character we are looping through
    print(char)  # we can do operations on each character in the string using the "char" variable
# the previous code will iterate through each character inside the string and print it
# example two
loop_through_list = ["Swordax", "SRDX", "SRX"]
for name in loop_through_list:  # "name" is a variable that contains the current item we are looping through
    print(name)  # we can do operations on each item in the list using the "name" variable
# the previous code will iterate through each item in the list and print it
"""
    - Note: the variable used to represent the current iterated value is a local variable and 
    cannot be accessed outside the loop statement block, so you can re-use it outside the loop 
    or in other loops for example.
    - Some popular naming traditions when programming and using a for loop statement: {
        1- using "i" as a variable name when iterating through numbers
        2- using "x" as a variable name when iterating through items in a list
        3- using "j" as a variable name when iterating through numbers when "i" is taken by a parent loop
    } * at the end its just a name and you can use whatever name you wish to use
"""

# break, continue, pass, and else statements in for loops [14.2]
"""
    - The break, continue, and pass statements that were mentioned in the "while" chapter 
    can be used in for loops as well!
"""
for name in loop_through_list:
    if name == "SRDX":
        break
    print(name)
"""
    - The previous code will end the loop and cancel looping if the current iterated value is "SRDX"
    - The continue statement can be used the same way, tho as you know, the continue statement will not 
    end and cancel the loop, it will just skip the current iteration and go for the next one, and the 
    code that comes after the "continue" statement inside the loop block will not run for the current iteration
    - The pass statement can also be used in for loops the same way we learned about it before, it should be 
    used if you ever wanted to create an empty loop block
"""
"""
    - Remember how we used the else statement with the while loops? we can do the same with for loops
    - The else statement block after the for loop will run after the loop is completed, however, it 
    will not run if the statement was cut by a break statement
"""
for name in loop_through_list:
    print(name)
else:
    print("The loop is completed and a break statement was NOT applied")

# looping through a sequence of numbers [14.3]
"""
    - You might sometimes need to loop a number of times and have access to that specific number
    - You can do that by creating a list of numbers and then iterating through that list, but that is 
    a very bad and un-efficient way of doing things obviously
    - To iterate through a sequence of numbers, you can use the range() function
    - The range() function provides a sequence of numbers that you can iterate through
    - The range() function starts from 0 (by default), and throughout the loop, on each iteration the number 
    will increment by 1 (by default)
"""
for i in range(6):
    print(i)
# the previous code will print numbers from 0 to 5 (6 excluded)
"""
    - The range() function starts from 0 by default, but its possible to start from a custom number 
    by adding a parameter to specify that number
"""
for i in range(2, 6):
    print(i)
# the previous code will print the numbers from 2 to 5 (6 excluded)
"""
    - The range() function increments the counter variable by 1 on each iteration by default, but its possible 
    to increment by a custom specified number by adding another parameter to specify the incrementing value
"""
for i in range(2, 11, 2):
    print(i)
# the previous code will print the even numbers from 2 to 11 (11 excluded) : (2, 4, 6, 8, 10)




# Functions [15]
# intro to functions [15.1]
"""
    - Functions, another fundamental and basic subject to learn in programming
    - Functions can be defined as a container of code that won't run unless it was called to run
    - A function can take data into it, called parameters or arguments
    - A function can return data as a result
    - A function in python can be defined using the keyword "def"
    - The code inside the function can be grouped using indentation as we are used to in loops and if statements
"""
def my_first_function():
    # this is the content of the function
    print("This print statement will not run until the function is called to work")
my_first_function()  # this is how to call a function, you can call it anywhere you want (after function declaration)

# function arguments [15.2]
"""
    - An argument [arg] (aka: parameter [param]) are data passed into a function
    - You can deal with args as variables but inside a function, args cannot be accessed outside the function block
    - Args can be declared/defined inside the parenthesis after the function name
    - You can add as many args as you want, separated with commas
    - When calling a function, pass the values of the args inside the parenthesis when calling the function
    - The number of defined args should be the same as the number of passed args when calling the function
"""
def add_two_numbers(a, b):
    print(a + b)
add_two_numbers(1, 2)  # this should print 3
def subtract_two_numbers(a ,b):  # notice how we used the same argument names as the previous function
    print(a - b)
# this function wont run because it was not called

# advanced arguments [15.3]
"""
    * Arbitrary Arguments *
    - If you don't know how many args will be passed, you can group all the args in a tuple by using the 
    arbitrary args* (using the star character *)
"""
def get_second_name(*names):
    print(names[1])  # 1 as in 2 .. remember counting from 0
get_second_name("Swordax", "SRDX", "SRX")  # prints: "SRDX"
"""
    * Keyword Arguments *
    - You can pass args into a function using the key:pair syntax, like that, args wont have to be 
    ordered parallel to the receiving names in the function
    - This approach can be referred as "Keyword Args" or "kwargs"
"""
def get_last_name(name1, name2, name3):
    print(name3)
get_last_name(name2 = "SRDX", name3 = "SRX", name1 = "Swordax")  # prints: "SRX"
"""
   * Arbitrary Keyword Arguments *
   - You might not know how many keyword args you will be receiving, you can use the arbitrary arguments 
   concept here to collect the args in a collection as well, but since it will be a key:pair syntax, you 
   don't want them to be grouped in a tuple, but in a dictionary.
   - To do that you can use the arbitrary keyword args approach, by using two ** stars instead of one
"""
def get_first_name(**names):
    print(names["fname"])
get_first_name(lname = "SRX", fname = "Swordax")  # prints: "Swordax"
"""
    * Default Parameter Value *
    - You might sometimes not receive an argument value from the function call
    - To prevent errors, you can provide a default value for such cases
    - The default value will be used if no value was listed when function was called
"""
def print_welcome(name = "Anonymous"):
    print("Welcome Mr " + name)
print_welcome("Swordax")  # prints: "Welcome Mr Swordax"
print_welcome()  # prints: "Welcome Mr Anonymous"
"""
    - An argument data-type doesn't have to be a string, it can be from any data type, could be an integer, 
    a float, or even a collection (list, tuple, set, dictionary)
"""
def print_welcome_with_gender(data):
    for person in data:
        print("Welcome " + person[0] + ", you're a " + person[1])
    # notice how we dealt with the passed arg as a list
persons = [["Swordax", "Boy"], ["Swordia", "Girl"]]
print_welcome_with_gender(persons)  # passed a list as an arg to the function

# the return statement [15.4]
"""
    - As mentioned in lesson 15.1, a function can return outputs
    - You can return a value from a function by using the "return" statement inside the function
    - A return statement ends the function, so the code that comes after the return statement won't run
"""
def add_nums(a, b):
    return a + b
add_nums(1, 2)  # this won't print anything since a print statement wasn't used inside the function
print(add_nums(1, 2))  # prints: 3
number_three = add_nums(1, 2)  # we declared a variable that contains the value of 1 + 2
print(number_three)  # prints: 3
# the pass statement should be used if your function contains no code for some reason
def empty_func():
    pass

# recursion [15.5]
"""
    - Recursion is not a keyword or a statement, but a very popular mathematical and programming concept
    - Recursion is a way of doing things
    - Recursion is basically a function that can call itself
    - When working with recursion, you need to be very careful as any mistake can cause a function 
    that keeps calling itself forever, or a function that calls itself to a point that uses excess amounts 
    of device memory and processor power
"""
# demo to recursion
def recursion_demo(n):
    if n > 0:
        result = n + recursion_demo(n - 1)
        print(result)
    else:
        result = 0
    return result
recursion_demo(6)
# recursion could be confusing for new developers, don't worry if you don't understand it right away!

# lambda function [15.6]
"""
    - A lambda function is a small anonymous function
    - A lambda function can take any number of arguments, but it can only have one expression
    - Basically, a lambda is a shorthand to a small function
    - Lambda function syntax: function_name = lambda arguments: expression
    - You can call a lambda function the same way you call any other function
"""
lam_func = lambda a: print(a)
lam_func("Hello world!")  # prints: "Hello world!"
# lambda function can take as many arguments, just as a normal function
lam_add = lambda a, b: print(a + b)
lam_add(1, 2)  # prints: 3
lam_mult = lambda a, b, c: print(a * b * c)
lam_mult(1, 2, 3)  # prints: 6




# Object-Oriented Python [16]
# intro to object-oriented programming (OOP) [16.1]
"""
    - Welcome to chapter 16, I would like to introduce you to the world of object-oriented programming! you have 
    officially passed the beginner chapters and started going deep.
    - Python is an object-oriented programming language.
    - Object-oriented programming is a style of programming, a way of building stuff that is all around objects
    - An object has properties and methods, like a human with properties such as name, height, weight.. and methods 
    such as speak, hold, move.
    - Almost everything in python is an object, with its properties and methods.
"""

# classes & objects [16.2]
"""
    - A class is like an object constructor, a "blueprint", or a template for creating objects.
    - You can create a class using the "class" keyword
"""
class MyFirstClass:  # notice the traditional way of naming classes using the PascalCase
    x = 5
# the above code creates a class named MyFirstClass and contains a single property called x
# now you can create objects and store them in variables
my_first_object = MyFirstClass()
print(my_first_object.x)  # prints: 5
"""
    * __init__ function *
    - All classes have a built-in function called __init__(), which is always executed when a class is being initiated
    - The __init__() function is used to assign values to object properties
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person_1 = Person("Swordax", 123)
print(person_1.name)  # prints: "Swordax"
print(person_1.age)  # prints: 123
# the __init__() function is called everytime the class is being used to create a new object
"""
    * Object Methods *
    - Objects can also contain methods, methods in objects are functions that belong to the object
"""
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def move(self):  # you can define a method in an object like defining any other function we learned about previously
        print("The " + self.brand + " car moved!")  # this method prints a sentence
myBmw = Car("BMW", 2022)  # created a new object with properties (brand = "BMW" and year = 2022)
myBmw.move()  # prints: "The BMW car moved!"
"""
    * The self Parameter *
    - The self parameter is a reference to the current instance of the class, its used to access the properties that 
    belong to the class.
    - It doesn't have to be called "self", it can be called whatever you want, but it has to be the first parameter 
    of any method in the class.
"""
class Airplane:
    def __init__(joemama, brand, model):
        joemama.brand = brand
        joemama.model = model
    def fly(hahay):
        print("The " + hahay.brand + " plane flew!")
my_airbus = Airplane("Airbus", "A 350")
my_airbus.fly()  # prints: "The Airbus plane flew!"
"""
    - You can always modify object properties by overwriting them
"""
my_airbus.model = "A 380"
print(my_airbus.model)  # prints: "A 380" even though when the object was created it was set to be "A 350"
"""
    - You can also delete object properties by using the "del" keyword
    - You can even delete the whole object completely by using the "de" keyword
"""
del my_airbus.model  # deletes the "model" property of the "my_airbus" object
del my_airbus  # deletes the whole "my_airbus" object
"""
    - A class cannot be empty, but if you ever needed an empty class, you should use the pass keyword
"""
class EmptyClass:
    pass

# inheritance [16.3]
"""
    - Inheritance allows us to define a class that inherits properties and methods of another class
    - We need to know two definitions when working with inheritance: {
        Parent Class: the class being inherited from (aka: base class)
        Child Class: the class that inherits from another class (aka: derived class)
    }
"""
# create a parent class and an object from it
class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printname(self):
        print("This person's name is " + self.name)
thefather = Father("Abo", 30)
# create a child class and an object from it
class Son(Father):  # you can inherit all properties and methods from another class by passing it in parenthesis
    pass
theson = Son("Eben", 10)
theson.printname()  # notice how we can use the printname() method even tho it wasn't defined inside the Son class
"""
    - You might need to add an __init__() function inside the child class to add more properties
    - If you added an __init__() function to the child class, the inherited __init__() will be overwritten, but you 
    might probably still need to inherit the parent's properties in the __init__() function, so, you can keep the 
    inheritance of the parent's __init__() function by calling the paren't __init__() function inside the children's 
    __init__() function
"""
class Daughter(Father):
    def __init__(self, name, age, isHijabi):
        Father.__init__(self, name, age)
        self.isHijabi = isHijabi
thedaughter = Daughter("Ebna", 8, True)
thedaughter.printname()
"""
    - A better approach instead of re-calling the parent's __init__() function to keep it's inheritance, is to use the 
    super() function.
    - By using the super() function, you wont have to use the name of the parent class, and you wont have to include 
    the "self" parameter inside parenthesis in the parent's __init__() function calling
"""
class Grandson(Father):
    def __init__(self, name, age, isBaby):
        super().__init__(name, age)
        self.isBaby = isBaby
thegrandson = Grandson("Hafeed", 2, True)
thegrandson.printname()
"""
    - You can add methods to child classes normally as you would with the parent class and any other class
"""
class Granddaughter(Father):
    def __init__(self, name, age, hasHair):
        super().__init__(name, age)
        self.hasHair = hasHair
    def talk(self):
        print("The grand-daughter " + self.name + " has spoke!")
thegranddaughter = Granddaughter("Hafeeda", 3, True)
thegranddaughter.talk()




# Iterators [17]
# what are iterators [17.1]
"""
    - An iterator is an object that contains a countable number of values
    - An iterator is an object that can be iterated upon, meaning that you can traverse through all the values
    - In python, an iterator is an object which implements the iterator protocol, which consists of the methods 
    __iter__() and __next__()
    - Lists, tuples, dictionaries, and sets are all iterable objects, they are iterable containers that you can 
    get an iterator from
    - All these objects have an iter() method, which is used to get an iterator
"""
my_colors = ("red", "green", "blue")
my_iter = iter(my_colors)
print(next(my_iter))  # prints: "red"
print(next(my_iter))  # prints: "green"
print(next(my_iter))  # prints: "blue"
# even strings are iterable objects, and can return an iterator
mystring = "yes"
myiter = iter(mystring)
print(next(myiter))  # prints: "y"
print(next(myiter))  # prints: "e"
print(next(myiter))  # prints: "s"

# create an iterator [17.2]
"""
    - You can create an object/class as an iterator, but to do that you will need to implement the __iter__() and 
    __next__() in your class
    - the __iter__() method acts similarly to the __init__() in terms of initializing things, it must return the 
    iterator object itself
    - the __next__() method also allows you to do operations, and should also return the iterator object itself
"""
# we will create an iterator that returns numbers counting from 0 and up
class MyIterator:
    def __iter__(self):
        self.x = 0
        return self
    def __next__(self):
        q = self.x
        self.x += 1
        return q
iterator_object = MyIterator()
iterator_obj_itr = iter(iterator_object)
print(next(iterator_obj_itr))  # prints: 0
print(next(iterator_obj_itr))  # prints: 1
print(next(iterator_obj_itr))  # prints: 2
print(next(iterator_obj_itr))  # prints: 3
# etc..

# stop iterator [17.3]
"""
    - Example in lesson 17.2 can go on iterating forever if you continued using the next(), maybe in a loop for example.
    - To prevent the iteration to go on forever, you can use the "StopIteration" statement.
    - You can use the "StopIteration" statement inside the __next__() method in a terminating condition, you can 
    block the iteration if it iterated for a specified number of times
"""
class HisIterator:
    def __iter__(self):
        self.x = 1
        return self
    def __next__(self):
        if self.x <= 10:
            q = self.x
            self.x += 1
            return q
        else:
            StopIteration
iterator_object2 = HisIterator()
iterator_obj_itr2 = iter(iterator_object2)
print(next(iterator_obj_itr2))  # prints: 1
print(next(iterator_obj_itr2))  # prints: 2
print(next(iterator_obj_itr2))  # prints: 3
# etc.. (if iterated 10 times, iteration is blocked and no more iteration is valid)




# Scope [18]
# what is scope [18.1]
"""
    - A variable is only available to use and accessible inside the region/block it was created in, this is called scope
    - Local scope: a variable created inside a function belongs to the local scope of that function, and can only be 
    used inside that function
    - Global scope: a variable created in the main body (top level block) of the code is a global variable and 
    belongs to the global scope, it is available and can be accessed anywhere across the code
"""
my_global_variable = "This is a global variable, can be accessed anywhere in the code"
def local_demo():
    my_local_variable = "This is a local variable that belongs to the local_demo() function"
    # the above variable can only be accessed inside the local_demo() function
    def nested_demo():
        print(my_local_variable)  # my_local_variable can be accessed here
        print(my_global_variable)  # my_global_variable can be accessed here

# variable naming in and out of blocks [18.2]
"""
    - If you used the same variable name inside and outside a function, python will treat them as two separate 
    variables, and the global one wont get overwritten
"""
varone = "Yay!"
def yayfunc():
    varone = "Noo!"
    print(varone)  # prints: Noo!
yayfunc()
print(varone)  # prints: Yay!

# the global keyword [18.3]
"""
    - You might sometimes need to create a global variable, but realize you're inside a scope! what a problem
    - You can bypass this issue by using the "global" keyword (remember it from chapter 2 ?)
    - The global keyword can be used to make a global variable inside a scope
"""
def useglobal():
    global isglobal
    isglobal = True
useglobal()  # you should call the function!
print(isglobal)  # works fine!
"""
    - You should also use the "global" keyword if you wanted to make a change to a global variable from inside a scope
"""
my_global = "Original"
def change_global():
    global my_global
    my_global = "Modified"
change_global()
print(my_global)  # prints: "Modified"




# Modules [19]
# what are modules [19.1]
"""
    - Modules are basically a set of pre-written code/functions that you can include and use in your code
    - Modules are libraries
    - If you're familiar with JavaScript, then modules are like libraries, and if you're familiar with Node.js, 
    then modules here are literally the same
    - You can use modules/libraries that other people wrote to make writing your own code easier, simpler, and faster
    - You can write your own modules to split your project files and organize things around
"""
# lets create a simple module
def greet(name):
    print("Hello " + name)
# now save the file as "greeting.py"
# congrats! you created your first module

# use/import a module [19.2]
"""
    - To use a module that you/other people created, you should import it
    - You can import modules by using the "import" keyword/statement
"""
# lets import the module we created in lesson 19.1
import greeting
greeting.greet("Swordax")  # prints: "Hello Swordax"
# to access the functions inside a module, use the following syntax: modulename.functioname()
# a module can also contain variables of all types! and those can be accessed outside the module as well
# lets create a module called people.py, and lets include the following inside it
person_1 = {
    "name": "Swordax",
    "age": 123,
    "nationality": "Mars"
}
# now lets import and use the module inside our project file
import people
print(people.person_1["name"])  # prints: "Swordax"
# as simple as that
"""
    - note: as you can tell, a module is a python file, so it should always have the extension of .py just like 
    any other python file
"""

# renaming modules [19.3]
"""
    - We learned how to use modules with their original names, but you should know that we can rename a module 
    inside our project file and use it with a different name
"""
import mymodule as newname  # like this, we renamed the "mymodule" module as "newname"
newname.usefunction()  # now we can use the module with its new name!

# built-in modules [19.4]
"""
    - Usually, to use an external module, you will need to install it first, but, python has a number of 
    built-in modules that you can directly import without having to install anything!
"""
import platform
my_system = platform.system()
print(my_system)  # this will print your system name (Windows, Mac, Linux, or whatever operating system you're using)
# there is a built-in functions in python that list all the function/variable names in a module, the dir() function
func_var_names = dir(platform)
print(func_var_names) # this will print all the functions/variables names present inside the platform module

# specified importing [19.5]
"""
    - As you know, a module can contain a number of functions and/or variables
    - Maybe you don't want to use all the functions/variables inside a module, maybe just one of them
    - You can do that by doing like the following:
"""
# lets create a demo module as an example
# module saved as demomod.py
def greet(name):
    print("Hello " + name)
def goodbye(name):
    print("Goodbye " + name + ", see you later!")
myinfo = {
    "name": "Swordax",
    "age": None,
    "nationality": "Mars",
    "isMarried": False
}
# now lets import te my_info variable only inside the following project file
from demomod import myinfo
print(myinfo)  # prints the "myinfo" dictionary




# Dates [20]
"""
    ...
"""















