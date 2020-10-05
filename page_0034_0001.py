#You can also assign a single value to several variables simultaneously.
a = b = c = 1
print(a,b,c)
#Output: 1 1 1

#When using such cascading assignment, it is important to note that all three variables a , b and c refer to the same
#object in memory, an int object with the value of 1. In other words, a , b and c are three different names given to the
#same int object. Assigning a different object to one of them afterwards doesn't change the others, just as expected:
a = b = c = 1   #all three names a,b and c refer int object with value 1
print(a,b,c)
#Output: 1 1 1
b = 2           #b now refers to another int object, one with a value of 2
print(a,b,c)
#Output: 1 2 1  #so output is as expected.

