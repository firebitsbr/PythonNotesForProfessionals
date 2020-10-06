#Python uses the colon symbol ( : ) and indentation for showing where blocks of code begin and end (If you come
#from another language, do not confuse this with somehow being related to the ternary operator - https://en.wikipedia.org/wiki/%3F:). 
#That is, blocks in Python, such as functions, loops, if clauses and other constructs, have no ending identifiers. All blocks start 
#with a colon and then contain the indented lines below it.

#Python usa o símbolo de dois pontos (:) e indentação para mostrar onde os blocos de código começam e terminam (se você vier
#de outro idioma, não confunda isso com estar de alguma forma relacionado ao operador ternário - https://en.wikipedia.org/wiki/%3F :).
#Isso é, blocos em Python, como funções, loops, cláusulas if e outras construções, não têm identificadores de finalização. Todos os blocos começam
# com dois-pontos e contém as linhas recuadas abaixo dele.

def my_function():      #This is a function definition. Note the colon (:) esta é uma definição de função. Observe os dois pontos (:)
    a = 2               #This line belongs to the function because it's indented. #Esta linha pertence à função porque está indentada.
    return a            #This line also belongs to the same function. #Esta linha também pertence à mesma função.
print(my_function())    #This line is OUTSIDE the function block. #Esta linha está FORA do bloco de funções. 

a = 1
b = 2

if a > b:               #If block starts here   #Se o bloco começar aqui
    print(a)            #This is part of the if block   #Isso faz parte do bloco if
else:                   #else must be at the same level as if   #mais deve estar no mesmo nível como se
    print(b)            #This line is part of the else block    #Esta linha é parte do bloco else