''' namespace is a system to have a unique name for each and every object in python, object can be variable or method
its just like a surname, python interpretor understands what exact method or variable one is trying to point to in
code , depending upon the namespace
Three types of namespaces--> Built In namespace , Global Namespace , Local Namespace
Lifetime of a Namespace-->Depends on scope of objects , if scope ends lifetime ends, not possible to access inner
namespace’s objects from an outer namespace.
-->>same object name can be present in multiple namespaces as isolation between the same name is maintained by their namespace.
'''

# var1 is in the global namespace
var1 = 5


def some_func():
    # var2 is in the local namespace
    var2 = 6

    def some_inner_func():
        var3 = 7  # var3 is in the nested local  namespace


''' Statement Indentation and Comment in Python
-->> Instructions written in the source code for execution are called statements.
-->> Statements in Python can be extended to one or more lines using parentheses (), braces {}, square brackets [], semi-colon (;), 
     continuation character slash (\).
-->> A block is a combination of all these statements. Block can be regarded as the grouping of statements for a specific purpose.
-->> Whitespace is used for indentation in Python.
-->> If a block has to be more deeply nested, it is simply indented further to the right.      
-->> Comments are the useful information that the developers provide to make the reader understand the source code.
-->> Python single line comment starts with hashtag symbol with no white spaces (#) and lasts till the end of the line
-->> Python multi-line comment is a piece of text enclosed in a delimiter (""") on each end of the comment    
'''

''' Structuring Python Programs ------- 
--> In general, the interpreter reads and executes the statements line by line i.e sequentially
--> The interpreter considers the ‘new line character’ as the terminator of one instruction.
'''
x = [1, 2, 3, 4]
x[1:3]  # Means that start from the index  1 and go upto the index 2

'''Types Of Line Continuation ----- Implicit Continuation, Explicit Continuation
Implicit Continuation---Any statement containing opening parentheses (‘(‘), brackets (‘[‘), or curly braces (‘{‘) is presumed to be 
incomplete until all matching parentheses, square brackets, and curly braces have been encountered.
Example---'''
a = [
    [1, 2, 3],
    [3, 4, 5],
    [5, 6, 7]
]

print(a)

'''Explicit Continuation--- use a character that helps the interpreter to understand that the particular statement is spanning more than
 one lines.Backslash (\) is used to indicate that a statement spans more than one line.  Example---'''
x = \
    1 + 2 \
    + 5 + 6 \
    + 10

print(x)



