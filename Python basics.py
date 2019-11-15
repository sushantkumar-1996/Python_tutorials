''' Small Sections of overview of python Detailed  description Later
Variables and data structures in python--LIST --
List is mutable data structure where items can be added after its creation , Python program to illustrate list'''

nums = []  # creates an Empty List

nums.append(21)
nums.append(55)
nums.append("String")

# The above can also be declared as -->
nums = [21, 55, "String"]
print(nums)

'''Taking Input in Python using input() function'''
name = input("Enter Your Name:")
print("hello", name)

num1 = int(input("Enter num 1:"))
num2 = int(input("Enter num 2:"))
num3 = num1 * num2
print(num3)

'''Selection Statement in Python--> Made up of two keywords if and elif and else Program to illustrate'''

num1 = 23
if num1 > 12:
    print("num 1 is greater")
elif num1 < 12:
    print("num 1 is lesser")

'''Functions in Python'''


def hello():
    print("hello")
    print("Hello again")


hello()  # calling function


# Validate Function with main

def Integer():
    result = int(input("Enter Integer"))
    return result


def Main():
    print("Started")
    output = getInteger()
    print(output)


if __name__ == "__main__":
    Main()

'''Looping and Iteration in Python'''

for step in range(5):
    print(step)

'''Keywords in python-->>
TRUE,FALSE,NONE-->Special Constant used to denote a null value or void, '0' or any empty list does not compute to none
,AND,OR,NOT,ASSERT--> Used for debugging purposes, used to check the correctness of code,BREAK,CONTINUE,CLASS--> used to declare 
user defined classes,DEF--> used to declare user defined functions,IF,ELSE,ELIF

TRY-->used for exception handling code in try block is checked if there is any type of error except block is executed
EXCEPT-->This works together with try to catch exceptions
RAISE-->Used for exception handling to explicitly raise exceptions
FINALLY-->Always Executed whatever the code may be in try block
FOR,WHILE, PASS-->its a null statement used to prevent indentation errors and used as a placeholder
IMPORT,FROM--> used with Import,AS-->used to create the Alias for the module imported
LAMBDA-->used to make inline returning functions with no statements allowed internally 
RETURN, YIELD--> used like return but used to return a generator , WITH-->used to wrap the execution of block of code within methods
IN: CHeck if a container contains a value 
IS: This keyword is is used to test object identity ie to check if both the objects have same memory location or not
DEL: Del is used to delete a reference to an object. Any variable or list value can be deleted using del
'''

# Examples of Above Mentioned Keywords Python code to demonstrate True, False, None, and, or , not showing that None
# is not equal to 0 ,prints False as its false.
print(None == 0)  # False
x = None
y = None
print(x == y)  # True
print(True or False)  # True
print(False and True)  # False
print(not True)  # False

# Python code to demonstrate del and Assert
list1 = [1, 2, 3]  # initializing List
print(list1)
del list[1]
print(list1)

assert 5 < 3, "5 is not smaller than 3"

# python code to demonstrate working of global and non-local
a = 10  # initializing variable globally


def read():
    print(a)


def mod1():
    global a
    a = 5  # changing the value of globally defined variable


def mod2():
    a = 15  # changing value of local variable


read()  # reading initial value of a prints 10
mod1()  # calling mod 1 function to modify value modifies value of global a to 5
read()  # reading modified value prints 5
mod2()  # calling mod 2 function to modify value  modifies value of local a to 15, doesn't effect global value
read()  # reading modified value  again prints 5
