"""Python Program for  multiplying all the elements in a list-- 3 different ways
Method 1: Traversal--- Initialize the value of product to 1(not 0 as 0 multiplication by zero) traverse till the end of
the list, multiply every number with the product"""

def mulList(lst):
    result = 1
    for i in lst:
        result = result * i
    return result

lst = []
n = int(input("Enter Number of elements"))
for i in range(0, n):
    elements = int(input())
    lst.append(elements)
print(mulList(lst))

"""Method 2--Using numpy.prod()---use numpy.prod() from numpy module it returns an integer or a float value depending
 on the multiplication result"""

import numpy
print(numpy.prod(lst))


"""Method 3---using lambda function--Usiing numpy.array-- lambda function does not include a return statement it 
 always contain an expression which is returned we can put a lambda defination anywhere a function is expected 
 and we wont have to assign it to a variable at all.The reduce() function in python takes in a function and a list 
 as argument. The function is called a lambda function and a list and a new reduced result is returned """

from functools import reduce
print(reduce((lambda x, y: x*y)), lst)