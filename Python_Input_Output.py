"""Two Functions in Python for taking user input in python
1. raw_input(prompt) ---works with older versions like python2.x..--This function takes exactly what is typed from the keyboard,
                        convert it to string and then return it to the variable in which we want to store
2. input(prompt)---  This function first takes the input from the user and then evaluates the expression, which means Python
                        automatically identifies whether user entered a string or a number or list. This function returns a String
Examples::
"""
val = input("Enter your value: ")
print(val)

'''Taking Inputs From Console and Typecasting'''
input1 = input()
print(input1)

print(int(input()))  # typeCasting into Integer
print(float(input()))  # typeCasting Into Float
print(str(input()))  # typeCasting Into String

'''Taking Multiple Inputs from User in Python-----Two Methods
    1. Using split() method-----Breaks the given input by the specified seperator. Syntax--input().split(separator, maxsplit)
    2. Using List Comprehension
    
Example using split() method--------
'''
x, y = input("Enter two values ").split()  # Taking Two inputs at a Time
print(x)
print(y)

a, b, c = input("Enter Three Values").split()  # Taking Three Inputs at a Time
print(a)
print(b)
print(c)

'''x = list(map(int, input("Enter a multiple value: ").split())) 
print("List of students: ", x)'''

'''Using List Comprehension to get Multiple inputs from user'''

e, f = [int(x) for x in input("Enter two values: ").split()]
print(e)
print(f)

g = [int(x) for x in input("Enter Multiple Values").split()]
print("Number of List is ", g)


'''Diffrent Python ways of taking Input'''
n = int(input())  # Inputting a variable
arr = [int(x) for x in input().split()]
summation = 0
for x in arr:
    summation += x
print(summation)

'''A little faster way for the above method to use inbuilt stdin,stdout
    sys.stdin----File Object, In this case file will be standard input buffer
    stdout.write(D) is faster than print(D) refer program in geeks for geeks
'''
'''input() function takes the value and type of the input you enter as it is without modifying the type wheras raw_input()
 function explicitly converts the input you give to the type String
 '''

'''print() function -----parameters-
        syntax-- print(value(s), sep= ‘ ‘, end = ‘\n’, file=file, flush=flush)
        value(s) : Any value, and as many as you like. Will be converted to string before printed
        sep=’separator’ : (Optional) Specify how to separate the objects example:print('G', 'F', 'G', sep ='') 
        end=’end’: (Optional) Specify what to print at the end.Default example:print("Python", end = '@')   
                                                                               print("GeeksforGeeks")   
        file : (Optional) An object with a write method. Default :sys.stdout
        flush : (Optional) A Boolean, specifying if the output is flushed (True) or buffered (False). Default: False
'''


'''OUTPUT FORMATTING ---
    1:Using Formatted string literals
    2:str.format method
    3:using string slicing and string concatenation 
'''
# 1: Using String %(modulo) Operator
print("Geeks : %2d, portal :% 5.2f" % (1, 05.333))  # he first placeholder “%2d” is used for the first component of
# our tuple, i.e. the integer 1. The number will be printed with 2 characters.
# As 1 consists only of one digits, the output is padded with 1 leading blanks.

# 2: Using format method
print('{0} and {1}'.format('Geeks', 'Portal'))  # Geeks and Portal
print('Number one portal is {0}, {1}, and {other}.'.format('Geeks', 'For', other ='Geeks'))  # Number one portal is Geeks, For, and Geeks.
print("Geeks :{0:2d}, Portal :{1:8.2f}".format(12, 00.546))  # Geeks :12, Portal :    0.55


# 3: Using String Method
cstr = "Hello World"
print(cstr.center(40, '#'))  # center aligned and rest spaces filled with '#'
print(cstr.ljust(40, '-'))   # left aligned and rest spaces filled with '-'
print(cstr.rjust(40, '&'))  # right aligned and rest spaces filled with '&'















