"""Strings In Python--- Strings are array of bytes epresenting unicode charachters  Square brackets can be used to access elements
of a String , Single charachter is simply a String of length 1"""

"""Creating a String----"""

str1 = 'Hello World'  # Creating a string with single quotes
str2 = "Helllooo Worrlld"  # Creating a string with double quotes
str3 = '''Heeelooo Twoo Worldd'''  # Creating a string with triple quotes also allows to span the string multiple lines
print(str1, str2, str3)

"""Accessing charachters in Python-------
                            Indexing allows negative address references to access characters from the back of the String
                            -1 refers to the last charachter , -2 refers to second last charachter
    Accessing index out of range will cause an index error and integers are allowed to pass as an index, other types will
    cause a Type error                
"""
str3 = "My Collegues are very nice and Helpfull"
print(str3)
print(str3[1])
print(str3[0])
print(str3[-1])

"""String Slicing---Used for accessing a range of charachters it is done using colon(:)---EXAMPLE"""

str4 = "Hello World"
print(str4[3:12])  # sicing charachters from 3-12
print(str4[3:-2])  # slicing charachters between 3rd and 2nd last charachter

"""Deleating or Updating a String--Updation or Deleation of charachters from a string is not allowed , Whole String can be
deleated using the built in del keyword"""

str5 = "Hello"
print(str5)
str5 = "World"
print(str5)

del str5
print(str5)





"""Escape Sequencing in Python----
printing Strings with single and double quotes in it causes SyntaxError because String already contains Single and Double
 Quotes and hence cannot be printed with the use of either of these So to print such string either triple quotes or Escape
 sequences can be used
 """
# Initial String
String1 = '''I'm a "Geek"'''
print("Initial String with use of Triple Quotes: ") 
print(String1) 
  
# Escaping Single Quote  
String1 = 'I\'m a "Geek"'
print("\nEscaping Single Quote: ") 
print(String1) 
  
# Escaping Doule Quotes 
String1 = "I'm a \"Geek\""
print("\nEscaping Double Quotes: ") 
print(String1) 
  
# Printing Paths with the  
# use of Escape Sequences 
String1 = "C:\\Python\\Geeks\\"
print("\nEscaping Backslashes: ") 
print(String1)
      
      
      
"""Formatting of strings--can be formatted using format() method , contains curly braces as placeholders which can hold arguments 
according to position or keyword to specify the order"""

Str1 = "{} {} {}".format("Hello", "World", "Hi")
print(Str1)  # printing in default order

Str2 = "{2} {0} {1}".format("Geeks", "For", "Life")
print(Str2)  # printing in positional format

Str3 = "{a} {b} {c}".format(a="Geeks", b="For", c="Life")
print(Str3)

"""Formatting of Integers"""
strr1 = "{0:b}".format(16)
print("Binary representation of 16 is ")
print(strr1)

"""Formatting of Floats"""
strr2 = "{0:e}".format(165.7674)
print(strr2)

"""Rounding Off Integers"""
strr3 = "{0:.2f}".format(1/6)
print(strr3)

"""Different methods under Strings"""
"""String Capitalize() method --Capitalize method converts first character of the string into uppercase without 
altering the whole string , method signature- capitalize(), no parameter is required, returns the modified string
if the string contains any special character as first character no change is done to that character, if first character
is already capital then no change is done to the string
Example:-"""

print("Example for String capitalize method")
strcap = "hello world"
print(strcap)
print(strcap.capitalize())

"""Python Casefold() method--returns a lowercase copy of the string except it removes all case distinctions 
present in the string, method signature--casefold(), no parameters are required, returns lowercase string
Example:--"""
print("Exapmle for casefold method")
strcase = "HELLOWORLD"
strcase1 = "HELLOWORLD-β"
strcase2 = "HelloWorld"
print(strcase)
print(strcase.casefold())
print(strcase1.casefold())
print(strcase2.casefold())# β is equivalent to ss

"""Python String center() method -- Python center method alligns string to center by by filling paddings left and right
of string, signature--center(width[,fillchar]), parameters- width(required), fillchar(optional)-responsible for 
filling left and right padding of the string , return type- returns modified string, Example:--"""

print("Example for center method")
strcenter = "Hello World"
print(strcenter)
print(strcenter.center(10))  # by default fillchar is applied , we are passing only width
print(strcenter.center(20, '#'))  # fills the padding by #

"""Python String count() method-- returns the number of occurences of substrings in the specified range, parameters
sub(required) = substring, start(optional) = start index of range, end(optional) = last index of range
signature = count(sub[, start[, end]]), return number of occurences of substring in range, Example:"""

print("Example for count method")
strcount = "Helllo Worllld"
print(strcount)
print(strcount.count('l'))
print(strcount.count('l', 3))
print(strcount.count('l', 3, 7))




