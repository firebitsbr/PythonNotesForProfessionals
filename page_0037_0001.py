#numbers
#int:   integer number

a = 2                   #atribuir 2 em a
b = 100                 #atribuir 100 em b
c = 123456789           #atribuir 123456789 em c
d = 38563846326424324   #atribuir 38563846326424324 em d

print(a)                #exibir a
print(b)                #exibir b
print(c)                #exibir c
print(d)                #exibir d

#Integers in Python are of arbitrary sizes.
#Inteiros em Python são de tamanhos arbitrários.

#Note: in older versions of Python, a long type was available and this was distinct from int . The two have
#been unified.
#Observação: nas versões anteriores do Python, um tipo longo estava disponível e era diferente do int. Os dois têm
#foi unificado.

#float: Floating point number; precision dependes on the implementation
#and system architecture, for CPython the float dataype corresponds to a C double.

#float: Número do ponto flutuante; a precisão depende da implementação
#e arquitetura do sistema, para CPython o tipo de dados float corresponde a um C duplo.

a = 2.0             #atribuir 2.0 em a
b = 100.e0          #atribuir 100.e0 em b 
c = 123456789.e1    #atribuir 123456789.e1 em c

print(a)            #exibir a
print(b)            #exibir b
print(c)            #exibir c

#complex: Comples numbers
#complexo: números complexos

a = 2 + 1j      #atribuir em a igual 2 + 1j
b = 100 + 10j   #atribuir em b 

#The < , <= , > and >= operators will raise a TypeError exception when any operand is a complex number.
#Os operadores <, <=,> e> = irão gerar uma exceção TypeError quando qualquer operando for um número complexo.

#Strings
#Python 3.x version >= 3.0

#str : a unicode string. The type of 'hello'    #str: uma string unicode. O tipo de 'olá'
#bytes : a byte string. The type of b'hello'    #bytes: uma string de bytes. O tipo de b'hello '
