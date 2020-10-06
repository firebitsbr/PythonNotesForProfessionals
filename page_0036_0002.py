#In Python 2.x and in Python 3.x, a boolean is also an int . 
#The bool type is a subclass of the int type and True and
#False are its only instances:
issubclass(bool, int)   #True
isinstance(True, bool)  #True
isinstance(False, bool) #True

#If boolean values are used in arithmetic operations, 
#their integer values ( 1 and 0 for True and False ) 
#will be used to return an integer result:

True + False == 1 # 1 + 0 == 1
True * True == 1 # 1 * 1 == 1

print()
print()