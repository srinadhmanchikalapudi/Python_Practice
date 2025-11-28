if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
    print("Five is greater than two!") 

#This is a comment


"""
This is a multi line string, 
which can also be used as multi line comments.
python will read this string literal,
but will ignore it as it is not assigned to a variable.
"""
#Variables do not need to be declared with any particular type, 
# and can even change type after they have been set.
x = 4
x = "Sally"
print(x)

#Casting:
x = str(3) # cast x to a string
x = int(3) # cast x to an integer
x = float(3) # cast x to a float
print(x)
print(type(x))
#String variables can be created by both single and double quotes
# Variable names are case sensitive
"""
Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""
#https://www.w3schools.com/python/python_ref_keywords.asp

# Camel Case: myVariableName = "John"
# Pascal Case: MyVariableName = "John"
# Snake Case: my_variable_name = "John"

#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#Note: Make sure the number of variables matches the number of values,
# or else you will get an error.

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

x,y,z = "Orange", 3, 4
print(x)
print(y)
print(z)

#Unpack a Collection
#If you have a collection of values in a list, tuple etc. 
# Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
print(x,y,x)
print(x + y + z) #Concatenate

#Global Variables
#Variables that are created outside of a function (as in all of the examples above)
#Global variables can be used by everyone, both inside of functions and outside.

x = "Awesome"

def func():
   print("Python is ", x)
func()
#If you create a variable with the same name inside a function, this variable will be local, 
# and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

def myFunc():
   x = 'fantastic'
   print("Python is ", x)
myFunc()
print("Python is ", x)

#Define a global variable from inside a function
def myFunc1():
   global x
   x = 'fantastic four'

myFunc1()
print("Python is ", x)

#global keyword can also be used to change a global variable inside a function.
x = "awesome"

def myFunc2():
   global x
   x = 'fantastic five'
myFunc2()
print("Python is ", x)

"""
Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

"""
Example	        Data Type
x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType
"""

"""
Setting the Specific Data Type
If you want to specify the data type, you can use the following constructor functions:

Example	        Data Type
x = str("Hello World")	str	
x = int(20)	int	
x = float(20.5)	float	
x = complex(1j)	complex	
x = list(("apple", "banana", "cherry"))	list	
x = tuple(("apple", "banana", "cherry"))	tuple	
x = range(6)	range	
x = dict(name="John", age=36)	dict	
x = set(("apple", "banana", "cherry"))	set	
x = frozenset(("apple", "banana", "cherry"))	frozenset	
x = bool(5)	bool	
x = bytes(5)	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview
"""

x =1
y = 2.5
z = 1j

a =float(x)
b = int(y)
c = complex(x) #Type casting

print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
#Note: You cannot convert complex numbers into another number type.

#Random Number
import random
print(random.randrange(1,10))
print(random.randint(1,10))
print(random.random())
print(random.uniform(1,10))

"""
Specify a Variable Type
There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
"""
#Strings are immutable - they cannot be changed after they are created.

#Strings in Python are surrounded by either single quotation marks, or double quotation marks.
print("Hello")
print('Hello')
#You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = """This is a
multi line string
example"""
print(a) #line breaks in o/p are inserted at the same position as here.

a = '''This is a
multi line string
example'''
print(a)

#Strings are arrays
a = "Hello, World!"
print(a[1]) #Prints the character at position 1
#Note: The first character has index 0.
#You can use negative indexing to start the count from the end of the string:
print(a[-1]) #Prints the last character of the string

print("\n") #New Line


#Looping in a string
for x in "banana":
   print(x)

#String Length
a = "Hello World"
print(len(a)) #Prints the length of the string

#Check string - To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt) #Returns True if found
print("expensive" in txt) #Returns False if not found
#Use it in an if statement:
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

#Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt) #Returns True if NOT found
print("free" not in txt) #Returns False if NOT found

#Slicing - you can return a range of charecters using the slice syntax
b = "Hello, World!"
print(b[2:5]) #Prints characters from position 2 to 4 (5 not included)
#Note: The first character has index 0.
print(b[:5]) #Prints characters from the beginning to position 4 (5 not included)
print(b[7:]) #Prints characters from position 7 to the end
print(b[-5:-2]) #Prints characters from position -5 to -3 (-2 not included)

#Modify Strings
a = " Hello, World! "
print(a.upper()) #Converts to upper case
print(a.lower()) #Converts to lower case
print(a.strip()) #Removes any whitespace from the beginning or the end. can add char inside () to remove that char instead of whitespace
print(a.replace("H", "J")) #Replaces a string with another string for every occurrence
print(a.split(",")) #Splits the string into substrings if it finds instances of the separator and returns list
print(a.split(" ")) #Splits the string into substrings if it finds instances of the separator and returns list
print(a.split("o")) #Splits the string into substrings if it finds instances of the separator and returns list
print(a.split()) #Splits the string into substrings if it finds instances of the separator and returns list

#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)
#To add a space between them, add a " ":
c = a + " " + b
print(c)

#fstrings (formatted string literals) - we cannot combine numbers and strings like this. but, we can use fstrings or format() method to combine strings and numbers.
age =36
txt = "My name is John, and I am " + str(age) #age is converted to string. if not, it will give error - as it cannot concatenate str and int
print(txt)

#To specify a string as an fstring, add the letter f to the beginning of the string literal and add curly brackets { } around the variable name.
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
age = 36
txt = "My name is John, and I am {}".format(age)
print(txt)

#Placeholders and Modifiers - a place holder can contain variables, operators, functions, and modifiers to format the value.
#You can add placeholders by using index numbers {0} in the string and referring to the index number in the format() method.
quantity = 3
itemno = 567
txt = "I want {0} pieces of item {1}".format(quantity, itemno)
print(txt)

#You can use the same index number more than once:
quantity = 3
itemno = 567
price = 49.95
txt = "I want to pay {2} dollars for {0} pieces of item {1}.".format(quantity, itemno, price)
print(txt)

#Add a placeholder for the price variable in an fstring:

price = 39
txt = f"The price is {price} dollars"
print(txt)

#A placeholder can include a modifier to format the value:
#A modifier is included by adding a colon : followed by a legal formatting type like .2f which means fixed point number with 2 decimals.
price = 49
txt = f"The price is {price :.2f} dollars"
print(txt)

#The format specifier can be a number defining how many characters should be displayed, or it can be a format type like b, c, d, f, s, etc.
#Here are some common format types:
#b - Binary format
#c - Character format
#d - Decimal format
#f - Fixed-point format
#s - String format

#all ASCII value maps to characters - https://www.ascii-code.com/

#ASCII value for 'A' is 65
print(ord('A')) #ord() function returns the ASCII value of a character

# Convert integer 65 to ASCII
ascii_char = chr(65)
print(ascii_char)  # Output: A

#Binary format - 00000101 is calculated by 2 powers - 2^2(3rd position from right) + 2^0(1st position from right) = 4 + 1 = 5.

txt = f"The binary version of 5 is {5 :b}" #Binary format
print(txt)

#Hexadecmial format - 0-9 and A-F (A=10, B=11, C=12, D=13, E=14, F=15)
#perform calculation of 4C to decimal: 4C = 4 * 16^1 + 12 * 16^0 = 64 + 12 = 76
txt = f"The hexadecimal version of 76 is {76 :x}" #Hexadecimal format
print(txt)

#Octal format - 0-7
#perform calculation of 77 to decimal: 77 = 7 * 8^1 + 7 * 8^0 = 56 + 7 = 63

txt = f"The octal version of 63 is {63 :o}" #Octal format
print(txt)

#Examples in Python conversions between number systems

a = "1010"   # binary for 10
b = "0011"   # binary for 3

# Convert to integers, add, then convert back to binary
sum_binary = bin(int(a, 2) + int(b, 2))[2:] #to remove 0b prefix

print(sum_binary)  # Output: "1101"

#Convert octal to decimal
octal_str = '377'
decimal = int(octal_str, 8)

#Convert Octal to hexadecimal
octal = '17'  # Example octal number as string
decimal = int(octal, 8)       # Convert octal to decimal
hexadecimal = hex(decimal)    # Convert decimal to hexadecimal

print(hexadecimal)  # Output: '0xf'

print(hex(int('17', 8)))  # Output: '0xf' - one liner

print( int('10', 2))  # Output: 2 - binary to decimal

#Hexadecimal to octal - first convert hex to decimal, then decimal to octal

#perform calculation of 4C to decimal: 4C = 4 * 16^1 + 12 * 16^0 = 64 + 12 = 76
#perform division of 76 by 8 to get octal: 76 / 8 = 9 and remainder 4. So, we take these numbers top to bottom to get octal 94.
#validation: perform calculation of 76 to octal: 76 = 9 * 8^1 + 4 * 8^0 = 72 + 4 = 76 So, we take these numbers bottom to top to get decimal 76.

#if we have decimal 114 and want to convert to octal:
#If we know conversion from any number system to decimal ( multiplication)

#If we know conversion from decimal to any number system ( LCM looking division)

#We can convert any number system to any number system by using decimal as intermediate stage

txt = f"The octal version of 76 is {76 :o}" #Octal format
print(txt)

#Example for b, c, d, s, hexadecmal and octal
price = 49
txt = f"The price is {price :d} dollars" #Decimal format
print(txt)
txt = f"The price is {price :s} dollars" #String format
print(txt)
txt = f"The character for 65 is {65 :c}" #Character format - gives character for the ASCII value 65. corresponding to 'A'
print(txt)
txt = f"The hexadecimal version of 255 is {255 :x}" #Hexadecimal format
print(txt)
txt = f"The octal version of 8 is {8 :o}" #Octal format
print(txt)

#For example, if you want to display a number as a binary value, you can use the format specifier b:
txt = f"The binary version of 10 is {10:b}"
print(txt)

#A placeholder can contain python code , like math operations.
txt = f"The price is {20*50} dollars"
print(txt)

#Escape Characters
#To insert characters that are illegal in a string, use an escape character. An escape character is a backslash \ followed by the character you want to insert.
#An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
#txt = "We are the so-called "Vikings" from the north"
#The solution to this problem is to use the escape character \"
txt = "We are the so-called \"Vikings\" from the north" #This escapes quotations "" from the string and lets it be part of the string.
print(txt)

#Other escape characters used in Python:
#\'	Single Quote
#\\	Backslash
#\n	New Line
#\r	Carriage Return
#\t	Tab
#\b	Backspace
#\f	Form Feed
#\ooo	Octal value
#\xhh	Hex value
txt = "Newline: Hello\nWorld!" #New Line -  adds a new line
print(txt)
txt = "Tab: Hello\tWorld!" #Tab - adds a tab space
print(txt)
txt = "Backslash: Hello\\World!" #Backslash - to insert a backslash
print(txt)
txt = "Backspace: Hello\bWorld!" #Backspace - removes the character before backspace
print(txt)
txt = "Carriage Return: Hello\rWorld!" #Carriage Return - overwrites Carria with World! Carriage return () is used to move the cursor back to the beginning of a line without advancing to the next line. 
print(txt)
txt = "Form Feed: Hello\fWorld!" #Form Feed - adds a form feed
print(txt)
txt = "Single Quote: Hello\'World!" #Single Quote - to insert single quote
print(txt)
txt = "Double Quote: Hello\"World!" #Double Quote - to insert double quote
print(txt)
txt = "Hex value: Hello\x48World!" #Hex value - to insert hex value
print(txt)
txt = "Octal value: Hello\110World!" #Octal value - to insert octal value
print(txt)


#String Methods
#Note: All string methods return new values. They do not change the original string.

a = " Hello, World! "
print(a.join(["Hello", "World"])) #Important for leet code - Joins the elements of an iterable (tuples, lists, etc.) to the end of the string
#convert string to a list of characters
print(list(a))
#convert list to a string 
print("".join(list(a)))

print(a.split(",")) #Important for leet code - Splits the string at the specified separator, and returns a list

print(a.capitalize()) #Converts the first character to upper case and all others to lowercase
print(a.casefold()) #Converts string into lower case
print(a.center(50)) #Centers the string within a certain width
print(a.count("o")) #Returns the number of times a specified value occurs in a string
print(a.encode()) #Returns an encoded version of the string. ex: string.encode(encoding='utf-16', errors='strict')
print(a.endswith("! ")) #Returns true if the string ends with the specified value
print(a.find("W")) #Searches the string for a specified value and returns the position - only gives first result
print(a.index("W")) #Searches the string for a specified value and returns the position of where it was found - only gives first result
print(a.isalnum()) #Returns True if all characters in the string are alphanumeric and no spaces and . are present
print(a.isalpha()) #Returns True if all characters in the string are in the alphabet and no spaces and . are present
print(a.isdecimal()) #Returns True if all characters in the string are decimals
print(a.isdigit()) #Returns True if all characters in the string are digits
print(a.islower()) #Returns True if all characters in the string are lower case
print(a.isupper()) #Returns True if all characters in the string are upper case
print(a.isspace()) #Returns True if all characters in the string are whitespaces
print(a.istitle()) #Returns True if the string follows the rules of a title
print(a.lstrip()) #Returns a left trim version of the string without leading spaces
print(a.rstrip()) #Returns a right trim version of the string without trailing spaces
print(a.lower()) #Converts a string into lower case
print(a.upper()) #Converts a string into upper case
print(a.replace("H", "J")) #Returns a string where a specified value is replaced with a specified value
print(a.strip()) #Returns a trimmed version of the string
print(a.title()) #Converts the first character of each word to upper case
print(a.swapcase()) #Swaps cases, lower case becomes upper case and vice versa
print(a.zfill(50)) #Fills the string with a specified number of 0 values at the beginning
print(a.partition(" ")) #Returns a tuple where the string is parted into three parts - reads string from left side and partitions at first occurrence of space
print(a.rpartition(" ")) #Returns a tuple where the string is parted into three parts - reads string from right side and partitions at first occurrence of space
print(a.splitlines()) #Splits the string at line breaks and returns a list
print(a.startswith(" ")) #Returns true if the string starts with the specified value
print(a.translate(a.maketrans("H", "J"))) #Returns a translated string
print(a.rfind("o")) #Searches the string for a specified value and returns the last position of where it was found
print(a.rindex("o")) #Searches the string for a specified value and returns the last position of where it was found
print(a.rjust(50)) #Returns a right justified version of the string - pads the string with spaces on the left to make the string of length 50
print(a.ljust(50)) #Returns a left justified version of the string - pads the string with spaces on the right to make the string of length 50
print(a.expandtabs()) #Sets the tab size of the string - default tab size is 8 spaces
print(a.isnumeric()) #Returns True if all characters in the string are numeric
print(a.isprintable()) #Returns True if all characters in the string are printable
print(a.isascii()) #Returns True if all characters in the string are ascii characters
print(a.encode()) #Returns an encoded version of the string
print(a.format()) #Formats specified values in a string
print(a.format_map({"H": "J"})) #Formats specified values in a string
print(a.maketrans("H", "J")) #Returns a translation table to be used in translations
print(a.count("o")) #Returns the number of times a specified value occurs in a string
print(a.expandtabs()) #Sets the tab size of the stringprint(a.zfill(50)) #Fills the string with a specified number of 0 values at the beginning
print(a.isidentifier()) #Returns True if the string is an identifier

"""
Python has a set of built-in methods that you can use on strings.

Method	Description
capitalize()	Converts the first character to upper case and all others to lowercase
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric. false if there are . and spaces
isalpha()	Returns True if all characters in the string are in the alphabet. false if there are . and spaces
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning

"""

#Python Booleans
#Booleans represent one of two values: True or False.
print(10 > 9) #Returns True
print(10 == 9) #Returns False
print(10 < 9) #Returns False
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")  

#Evaluating Values and Variables
print(bool("Hello")) #Returns True
print(bool(15)) #Returns True
print(bool("")) #Returns False
print(bool(0)) #Returns False
print(bool(None)) #Returns False. by default, the bool() method returns True if the object is defined, and False if the object is not defined.
print(bool(False)) #Returns False

print(bool("Srinadh" <"Sriz"))
#True - because capital letters have lower ASCII values than small letters. Also, it is compared character by character from left to right.

#Most Values are True
#Almost any value is evaluated to True if it has some sort of content.
#Any string is True, except empty strings.
#Any number is True, except 0.
#Any list, tuple, set, and dictionary are True, except empty ones.

#Some values are False
#In fact, there are not many values that evaluate to False.

#The following values are evaluated to False:
#False
#None
#0
#"" (empty string)
#() (empty tuple)
#[] (empty list)
#{} (empty dictionary)
#set() (empty set)
#range(0) (empty range)

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
bool(set())
bool(range(0))

#Functions can Return a Boolean

#One more value, or object in this case, evaluates to false, and that is if you have an object that is made from a class
#with a __len__ function that returns 0 or False:
class myclass():
   def __len__(self):
      return 0
myobj = myclass()
print(bool(myobj)) #Returns False

#Functions can Return a Boolean
def myFunction():
   return 1
print(myFunction()) #Returns True

def myFunction1():
   return True
if myFunction1():
   print("YES!")
else:
   print("NO!")

#Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x, int)) #Returns True
print(isinstance(x, float)) #Returns False


#Python Operators
#Python divides the operators in the following groups:
#Arithmetic operators
#Assignment operators
#Comparison operators
#Logical operators
#Identity operators
#Membership operators
#Bitwise operators

#https://www.w3schools.com/python/python_operators.asp

#Arithematic Operators - Arithmetic operators are used with numeric values to perform common mathematical operations:

print("Addition:", 10 + 5) #Addition
print("Subtraction:", 10 - 5) #Subtraction
print("Multiplication:", 10 * 5) #Multiplication
print("Division:", 10 / 5) #Division - quotient when remainder is zero
print("Modulus:", 10 % 3) #Modulus - Remainder of division
print("Exponentiation:", 10 ** 2) #Exponentiation
print("Floor Division:", 10 // 3) #Floor Division - Rounds the result down to the nearest whole number

#Assignment Operators - Assignment operators are used to assign values to variables:

x = 5
print("x =", x)
x += 3
print("x += 3:", x)
x -= 3
print("x -= 3:", x)
x *= 3
print("x *= 3:", x)
x /= 3
print("x /= 3:", x)
x %= 3
print("x %= 3:", x)
x //= 3
print("x //= 3:", x)
x **= 3
print("x **= 3:", x)
x=5
x &= 3
print("x &= 3:", x)
x |= 3
print("x |= 3:", x)
x ^= 3
print("x ^= 3:", x)
x >>= 3
print("x >>= 3:", x)
x <<= 3
print("x <<= 3:", x)
print(x := 3) #Walrus operator - assigns values to variables as part of a larger expression

"""

Bit operations are always performed at bit level, meaning that they operate on the binary representations of integers.
x &= 3  → Bitwise AND assignment: sets x to the result of x & 3.
           Clears bits in x where 3 has 0s. Often used to mask specific bits.
            Masking: A technique to isolate or clear specific bits in a binary number.
            to get the unmasked number we need to perform an 'OR'(|) operation between the result of mask with a unique value called restore which can be calculated as 'A' and not B;
            where A is the original number and B is the mask.
            restore = A | (~B)

x |= 3  → Bitwise OR assignment: sets x to the result of x | 3.
           Sets bits in x where 3 has 1s. Useful for enabling specific flags.
x ^= 3  → Bitwise XOR assignment: sets x to the result of x ^ 3.
           If the inputs are same, the result is 0 and when different, the result is 1. Useful for toggling flags.

x >>= 3 → Right shift assignment: shifts bits of x right by 3 places.
           Effectively divides x by 8 (2^3), discarding lower bits.

x <<= 3 → Left shift assignment: shifts bits of x left by 3 places.
           Effectively multiplies x by 8 (2^3), adding zero bits on the right.

"""

#Python Comparison Operators - Comparison operators are used to compare two values:
print(10 == 9) #Not Equal
print(10 != 9) #Not Equal
print(10 > 9)  #Greater Than
print(10 < 9)  #Less Than
print(10 >= 9) #Greater Than or Equal
print(10 <= 9) #Less Than or Equal

#Python Logical Operators - Logical operators are used to combine conditional statements:
print(10 > 9 and 5 < 10) #and - Returns True if both statements are true
print(10 > 9 or 5 > 10) #or - Returns True if one of the statements is true
print(not(10 > 9 and 5 < 10)) #not - Reverse the result, returns False if the result is true
# result, returns False if the result is true and True if the result is false
print(not(10 > 9 or 5 > 10)) #not - Reverse the result, returns True if the result is false

#Python Identity Operators - Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
#is - Returns True if both variables are the same object
#is not - Returns True if both variables are not the same object
x = ["apple", "banana", "cherry"]
y = ["apple", "banana", "cherry"]
z = x #Shallow copy - x and z point to the same object in memory
w = x.copy() #x and y have the same content, but are different objects in memory. so, is a deep copy.
#check address of each variable
print(id(x))
print(x is z) #is - Returns True if both variables are the same object
print(x is y) #is - Returns False if both variables are not the same object
print(x == y) #== - Returns True if the values of both variables are equal
print(x is not z) #is not - Returns False if both variables are the same object
print(x is not y) #is not - Returns True if both variables are not the same object
print(x != y) #!= - Returns False if the values of both variables are equal

#Python Membership Operators
x = ["apple", "banana", "cherry"]
print("banana" in x) #in - Returns True if a sequence with the specified value is present in the object
print("pineapple" in x) #in - Returns False if a sequence with the specified value is not present in the object
print("banana" not in x) #not in - Returns False if a sequence with the specified value is present in the object
print("pineapple" not in x) #not in - Returns True if a sequence with the specified value is not present in the object

#Python Bitwise Operators - Bitwise operators are used to compare (binary) numbers:
print(10 & 3) #AND - Sets each bit to 1 if both bits are 1
print(10 | 3) #OR - Sets each bit to 1 if one of two bits is 1
print(10 ^ 3) #XOR - Sets each bit to 1 if only one of two bits is 1. If both bits are 0 or both are 1, the result is 0.
## Bitwise XOR can be used as a simple encryption method. By applying XOR with a key, data can be encrypted and decrypted.
#For example, to encrypt a message, you can XOR each character's ASCII value with a key. To decrypt, you simply XOR the encrypted value with the same key again.
print(~10) #NOT - Inverts all the bits
print(10 << 3) #Zero fill left shift - Shift left by pushing zeros in from the right and let the leftmost bits fall off
print(10 >> 3) #Signed right shift - Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off


#Operator Precedence
#Operator precedence describes the order in which operations are performed in an expression.
#For example, in the expression 2 + 3 * 4, the multiplication is performed before the addition,
#so the result is 14, not 20.

#The following table lists the operators from highest precedence to lowest precedence:
#Operator	Description
#()	Parentheses
#**	Exponentiation
#+x, -x	Unary plus and minus, and bitwise NOT (~)
#*, /, //, %	Multiplication, division, floor division, and modulus
#+, -	Addition and subtraction
#<<, >>	Bitwise left and right shift operators
#&	Bitwise AND
#^	Bitwise XOR
#|	Bitwise OR
#in, not in, is, is not, <, <=, >, >=, !=, ==	Membership and identity operators, and comparison operators
#not	Logical NOT
#and	Logical AND
#or	Logical OR
#=, +=, -=, *=, /=, %=, //=, **=,
#&=, |=, ^=, >>=, <<=	Assignment operators
#lambda	Lambda expression
#https://www.w3schools.com/python/python_operators_precedence.asp

#If two operators have the same precedence, the expression is evaluated from left to right.


#Python Lists
#Lists are used to store multiple items in a single variable.
#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
#Lists are created using square brackets:
thislist = ["apple", "banana", "cherry"]
print(thislist)

print(len(thislist)) #Print the number of items in the list

#List Items - List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0], the second item has index
#[1] etc.
#List items can be of any data type:
list1 = ["apple", "banana", "cherry"] #String
list2 = [1, 5, 7, 9, 3] #Integer
list3 = [True, False, False] #Boolean
list4 = ["abc", 34, True] #Mixed
print(list1)
print(list2)
print(list3)
print(list4)


"""
Lists - Lists are ordered, changeable (Mutable), and allow duplicate values.

Python Collections (Arrays)
There are four collection data types in the Python programming language:
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.

Sets and Tuples are faster than lists. If you have a collection of data that does not need to be changed, consider using Python Tuples.

Python Tuples
Well organized and easy to understand.

*Set items are unchangeable, but you can remove and/or add items whenever you like.
**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

Change a Range of Item Values
To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
Example
Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
 
If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
Example
Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]

thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
 
Insert Items
To insert a new list item, without replacing any of the existing values, we can use the insert() method.
The insert() method inserts an item at the specified index:
Example
Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]

thislist.insert(2, "watermelon")
print(thislist)
Python List insert() Method
The insert() method inserts the specified value at the specified position.

"""
# is list built in data type in python
mylist = ["apple", "banana", "cherry"]

print(type(mylist)) #Print the data type of the list

#lists can store several data types in a single object.

mylist = ["apple", 1, True, 3.14]
print(mylist)  

#list operations like slicing, indexing, etc. are similar to strings.

#slicing; time complexity O(k) where k is number of elements in the slice
print(mylist[1:3]) #Output: ['1', 'True']

#indexing
print(mylist[0]) #Output: apple

#negative indexing; time complexity O(1)
print(mylist[-1]) #Output: 3.14
#looping
for item in mylist:
    print(item)      

#Check if Item Exists; time complexity O(n)
if "apple" in mylist:
    print("Yes, 'apple' is in the list")        

#Change Item Value; time complexity O(1)
mylist[1] = "blackcurrant"       
print(mylist)

#Insert Items - O(n)
mylist.insert(2, "watermelon") #Inserts "watermelon" at index

print(mylist)

#Add Items
mylist.append("orange") #Adds "orange" at the end of the list, and takes only one argument, but we can append another list as an item. Matter of fact adds any one object.
print(mylist)
"""
>>> mylist.append(["orr","ddd"])     
>>> mylist
['apple', 1, True, 3.14, ['orr', 'ddd']]
"""
mylist.extend(["mango", "grapes"]) #Adds multiple items to the end of the list, even though we are adding a list, it adds each item individually
print(mylist)
"""
>>> mylist.extend("mango")           
>>> mylist
['apple', 1, True, 3.14, ['orr', 'ddd'], 'm', 'a', 'n', 'g', 'o']
"""
#You can also use the list() constructor to make a list.
thislist = list(("apple", "banana", "cherry")) #We can pass any iterable object (tuples, sets, etc.) to the list() constructor to make a list.
print(thislist)
thislist = list({"apple", "banana", "cherry"}) #set
print(thislist)
#Remove Items
mylist.remove("banana") #Removes first occurance of "banana" from the list
print(mylist)
mylist.pop() #Removes the last item from the list, if we pass index inside (), it removes the item at that index
print(mylist)
mylist.pop(1) #Removes the item at index 1
print(mylist)
del mylist[0] #Removes the item at index 0
print(mylist)
del mylist #Deletes the entire list, erases the variable completely from memory
#print(mylist) #This will raise an error because the list no longer exists.
mylist = ["apple", "banana", "cherry", "orange"]
mylist.clear() #Empties the list 
print(mylist)
print("\n") #New Line

# List comprehensions
# List comprehensions provide a concise way to create lists.
# syntax: [expression for item in iterable if condition]

# Example: Create a list of squares
squares = [x**2 for x in range(10)]
print(squares)

# Example: Filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]

#flatten a nested list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [item for row in matrix for item in row]  # [1, 2, 3, 4, 5, 6]

# multiple conditions
filtered = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]  # [0, 6, 12, 18]
print(filtered)

#Cartesian Product with Filtering: 
pairs = [(x, y) for x in range(3) for y in range(3) if x != y]

# Advanced Example: Conditional Expressions
nums = [1, 2, 3, 4, 5]
result = ['even' if n % 2 == 0 else 'odd' for n in nums]  # ['odd', 'even', 'odd', 'even', 'odd']
print(result)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#Shallow copy - creates a new reference to the original list =
thislist = ["apple", "banana", "cherry"]
mylist = thislist
print(mylist)
mylist.append("orange")
print("Original List:", thislist)
print("Copied List:", mylist)
#Copy a List - Deep copy
#You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
mylist.append("orange")
print("Original List:", thislist)
print("Copied List:", mylist)

#Use the list() method - Deep copy
#Another way to make a copy is to use the built-in method list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
mylist.append("orange")
print("Original List:", thislist)
print("Copied List:", mylist)

# Use the slice Operator - Deep copy
# You can also make a copy of a list by using the : (slice) operator.
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
mylist.append("orange")
print("Original List:", thislist)
print("Copied List:", mylist)

"""
Python List methods
Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

"""

"""
Dictionary in  Python
Dictionaries are used to store data values in key:value pairs. 
Disctionaries are ordered, changeable, and do not allow duplicates.
Keys are unique within a dictionary while values may not be.

c = list({'baka':1, 'baka2': 2 })
c
['baka', 'baka2']
c = list({'baka':1, 'baka2': 2 }.values())
c
[1, 2]
c = list({'baka':1, 'baka2': 2 }.keys())  
c
['baka', 'baka2']
c = list({'baka':1, 'baka2': 2 }.items())
c
[('baka', 1), ('baka2', 2)] #List of tuples


"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict) #o/p - year: 2020

print(thisdict["brand"]) #Accessing Items
print(thisdict.get("model")) #Accessing Items
thisdict["year"] = 2020 #Changing Values
print(thisdict)
thisdict["color"] = "red" #Adding Items
print(thisdict)
thisdict.pop("model") #Removing Items
print(thisdict)
del thisdict["year"] #Removing Items
print(thisdict)
thisdict.clear() #Removing All Items
print(thisdict)
print("\n") #New Line

#Dictionary Methods
#Python has a set of built-in methods that you can use on dictionaries.
#Method	Description
#clear()	Removes all the elements from the dictionary
#copy()	Returns a copy of the dictionary
#fromkeys()	Returns a dictionary with the specified keys and value
#get()	Returns the value of the specified key
#items()	Returns a list containing a tuple for each key value pair
#keys()	Returns a list containing the dictionary's keys
#pop()	Removes the element with the specified key
#popitem()	Removes the last inserted key-value pair
#setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#update()	Updates the dictionary with the specified key-value pairs
#values()	Returns a list of all the values in the dictionary


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {'I': 1,
                            'V': 5,
                            'X': 10,
                            'L': 50,
                            'C': 100,
                            'D': 500,
                            'M': 1000}

        s = s.replace('IV', 'IIII') \
             .replace('IX', 'VIIII') \
             .replace('XL', 'XXXX') \
             .replace('XC', 'LXXXX') \
             .replace('CD', 'CCCC') \
             .replace('CM', 'DCCCC')
        
        return sum(map(roman_to_integer.get, s))