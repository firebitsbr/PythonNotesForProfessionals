#list : An ordered collection of n values ( n >= 0 )
#lista: uma coleção ordenada de n valores (n> = 0)

a = [1,2,3]
b = ['a',1, 'python', (1,2),[1,2]]

print(a)
print(b)

#Not hashable; mutable.
#Não hashable; mutável.

#set : An unordered collection of unique values. Items must be hashable(https://docs.python.org/3.5/glossary.html).
#set: Uma coleção não ordenada de valores únicos. Os itens devem ser hashable(https://docs.python.org/3.5/glossary.html).

a = {1,2, 'a'}
print(a)

#dict: Uma coleção não ordenada de pares de valores-chave exclusivos; as chaves devem ser hashable.
#dict : An unordered collection of unique key-value pairs; keys must be hashable.

a = {1: 'one',
     2: 'two'}

b = {'a':[1,2,3],
    'b': 'a string'}

print(a)
print(b)

#An object is hashable if it has a hash value which never changes during its 
#lifetime (it needs a __hash__() method), and can be compared to other 
#objects (it needs an __eq__() method). Hashable objects which compare equality 
#must have the same hash value.

#Um objeto é hashble se tiver um valor hash que nunca muda durante sua vida 
#(ele precisa de um __hash __ () método), e pode ser comparado a outros 
#objetos (ele precisa de um método __eq __ ()). Objetos hashable que a igualdade 
#de comparação deve ter o mesmo valor de hash.

#Built-in constants
#In conjunction with the built-in datatypes there are a small number of built-in 
#constants in the built-in namespace:
#True : The true value of the built-in type bool
#False : The false value of the built-in type bool
#None : A singleton object used to signal that a value is absent.
#Ellipsis or ... : used in core Python3+ anywhere and limited usage in Python2.7+ as part of array notation.
#numpy and related packages use this as a 'include everything' reference in arrays.
#NotImplemented : a singleton used to indicate to Python that a special method doesn't support the specific
#arguments, and Python will try alternatives if available.
#a = None # No value will be assigned. Any valid datatype can be assigned later
#Python 3.x Version >=0

#None doesn't have any natural ordering. Using ordering comparison operators ( < , <= , >= , > ) isn't #supported anymore and will raise a TypeError.


#Constantes integradas
#Em conjunto com os tipos de dados integrados, há um pequeno número de constantes integradas no namespace #integrado:
#Verdadeiro: o valor verdadeiro do tipo interno bool
#False: o valor falso do tipo embutido bool
#Nenhum: um objeto singleton usado para sinalizar que um valor está ausente.
#Reticências ou ...: usado no núcleo Python3 + em qualquer lugar e uso limitado em Python2.7 + como parte da #notação de matriz.
#pacotes numpy e relacionados usam isso como uma referência 'incluir tudo' em arrays.
#NotImplemented: um singleton usado para indicar ao Python que um método especial não suporta o método #específico
#argumentos, e Python tentará alternativas, se disponíveis.
#a = Nenhum # Nenhum valor será atribuído. Qualquer tipo de dados válido pode ser atribuído posteriormente
#Python 3.x Version >=0

#None não tem nenhuma ordem natural. O uso de operadores de comparação de pedidos (<, <=,> =,>) não é mais compatível e gerará um TypeError.

#Testing the type of variables
#Testando o tipo de variáveis

#In python, we can check the datatype of an object using the built-in function type .
#Em python, podemos verificar o tipo de dados de um objeto usando o tipo de função embutido.

a = '123'           #atribuir em a = '123'
print(type(a))      #exibir tipo de dado de a

b = 123             #atribuir em b = 123
print(type(b))      #exibir tipo de dado de b