''' Python in its language defines an inbuilt module “keyword” which handles certain operations related to keywords.
 A function “iskeyword()” checks if a string is keyword or not. '''

import keyword  # Importing Keyword for Keyword operations
# Initializing Strings For testing
s = "for"
s1 = "geeksforgeeks"
s2 = "elif"
s3 = "elseif"
s4 = "nikhil"
s5 = "assert"

if keyword.iskeyword(s):
    print(s + " is a Keyword")
else:
    print(s + " is not a Keyword")

if keyword.iskeyword(s1):
    print(s1 + " is a Keyword")
else:
    print(s1 + " is not a Keyword")

if keyword.iskeyword(s2):
    print(s2 + " is a Keyword")
else:
    print(s2 + " is not a Keyword")

if keyword.iskeyword(s3):
    print(s3 + " is a Keyword")
else:
    print(s3 + " is not a Keyword")

if keyword.iskeyword(s4):
    print(s4 + " is a Keyword")
else:
    print(s4 + " is not a Keyword")

if keyword.iskeyword(s5):
    print(s5 + " is a Keyword")
else:
    print(s5 + " is not a Keyword")

'''Printing List of all Keywords'''

print(keyword.kwlist)  # USing Kwlist to print all the keywords

#  Print without NewLine In Python
print("geeks", end=" ")
print("Geeks For Geeks")
a = [1, 2, 3, 4]
for i in range(4):
    print(a[i], end=" ")



''' One Liner If Else statement in Python Instead of conditional Operator(?) '''

a = 1 if 20 > 10 else 0
print(a)

'''Decision makig Statements in python::-- 
    if statement
    if..else statements
    nested if statements
    if-elif ladder
    
Examples:::::
'''
i = 10
if i < 15:
    print("Hello World")


j = 20
if (j < 15):
    print ("i is smaller than 15")
    print ("i'm in if Block")
else:
    print ("i is greater than 15")
    print ("i'm in else Block")
print ("i'm not in if and not in else Block")

i = 10
if i == 10:
    #  First if statement
    if i < 15:
        print("i is smaller than 15")  # Nested - if statement  Will only be executed if statement above it is true
    if i < 12:
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")

i = 20
if i == 10:
    print("i is 10")
elif i == 15:
    print("i is 15")
elif i == 20:
    print("i is 20")
else:
    print("i is not present")

