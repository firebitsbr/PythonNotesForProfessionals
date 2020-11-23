#Converting between datatypes
#Conversão entre tipos de dados

#You can perform explicit datatype conversion.
#Você pode realizar a conversão explícita de tipo de dados.

#For example, '123' is of str type and it can be converted to integer using int function.
#Por exemplo, '123' é do tipo str e pode ser convertido para inteiro usando a função int.

a = '123'   # variável a recebe '123'
b = int(a)  # variavel b recebe o valor de a convertido de inteiro
print(b)    # exibir conteudo de b

#Converting from a float string such as '123.456' can be done using float function.
#A conversão de uma string float como '123.456' pode ser feita usando a função float.

a = "123.456"   #variavel a recebe "123.456"
b = float(a)    #variavel b recebe variavel a 
#c = int(a)      #ValueError: invalid literal for int() with base 10: '123.456'
d = int(b)      #variavel d recebe variavel b

print(a)        #exibir a
print(b)        #exibir b