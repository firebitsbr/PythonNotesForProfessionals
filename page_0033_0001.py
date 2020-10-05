a,b,c = 1,2,3
print(a,b,c)
#Output: 1 2 3

#a, b, c = 1, 2
#Exception has occurred: ValueError
#not enough values to unpack (expected 3, got 2)

#a, b = 1, 2, 3
#Exception has occurred: ValueError
#too many values to unpack (expected 2)

#The error in last example can be obviated by assigning remaining values to equal number of arbitrary variables.
#This dummy variable can have any name, but it is conventional to use the underscore ( _ ) for assigning unwanted
#values:
a,b, _ = 1,2,3
print(a,b)

#Note that the number of _ and number of remaining values must be equal. Otherwise 'too many values to unpack
#error' is thrown as above:
#a, b, _ = 1,2,3,4
#Exception has occurred: ValueError
#too many values to unpack (expected 3)


