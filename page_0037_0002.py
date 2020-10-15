#Sequences and collections
#Sequências e coleções

#Python differentiates between ordered sequences and unordered collections (such as set and dict ).
#Python diferencia entre sequências ordenadas e coleções não ordenadas (como set e dict).

#strings ( str , bytes , unicode ) are sequences
#strings (str, bytes, unicode) são sequências

#reversed : A reversed order of str with reversed function
#reversed: uma ordem invertida de str com função invertida

a = reversed('hello')
str(a)
print(a)

#tuple : An ordered collection of n values of any type ( n >= 0 ).
#tupla: uma coleção ordenada de n valores de qualquer tipo (n> = 0).

a = (1,2,3)
b = ('a',1,'python', (1,2))
#b[2] = `something else` #returns a TypeError

#Supports indexing; immutable; hashable if all its members are hashable
#Suporta indexação; imutável; hashable se todos os seus membros forem hashable