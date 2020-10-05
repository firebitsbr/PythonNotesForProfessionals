#1. Variables names must start with a letter or an underscore.
x = True    # valid
_y = True   # valid

#9x = False  # starts with numeral
#SyntaxError: invalid syntax

#$y = False # starts with symbol
#SyntaxError: invalid syntax

#2. The remainder of your variable name may consist of letters, numbers and underscores.
has_0_in_it = "Still Valid"

#3. Names are case sensitive.
x = 9
#y = X*5
#Exception has occurred: NameError
#name 'X' is not defined

#Even though there's no need to specify a data type when declaring a variable in Python, while allocating the
#necessary area in memory for the variable, the Python interpreter automatically picks the most suitable built-in
#type for it:
a = 2
print(type(a))
#Output: <class 'int'>

b = 9223372036854775807
print(type(b))
#Output: <class 'int'>

pi = 3.14
print(type(pi))
#Output: <class 'float'>

c = 'A'
print(type(c))
#Output: <class 'str'>

name = 'John Doe'
print(type(name))
#Output: <class 'str'>

q = True
print(type(q))
#Output: <class 'bool'>

x = None
print(type(x))
#Output: <class 'NoneType'>



