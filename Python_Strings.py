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




