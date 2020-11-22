#In conditional statements it is possible to test the datatype with isinstance . However, it is usually not encouraged
#to rely on the type of the variable.

#Em declarações condicionais, é possível testar o tipo de dados com isinstance. No entanto, geralmente não é 
#encorajado a confiar no tipo da variável.

i = 7                       #atribuir em i = 7        
if isinstance(i, int):      #se tipo de dados em i, int (inteiro)
    i += 1                  #i recebe mais 1
    print(i)                #exibir conteudo de i
elif isinstance(i, str):    #senão se tipo de dados em i, str (string)   
    i = int(i)              #i recebe inteiro de i
    i += 1                  #i recebe mais 1
    print(i)                #exibir conteudo de i

#For information on the differences between type() and isinstance() read: #Differences between isinstance and type in Python (https://stackoverflow.com/questions/1549801/what-are-the-differences-between-type-and-isinstance)

#Para obter informações sobre as diferenças entre type () e isinstance (),leia: Diferenças entre isinstance e type em Python (https://stackoverflow.com/questions/1549801/what-are-the-differences-between-type-and-isinstance)

#To test if something is of NoneType :
#Para testar se algo é de NoneType:

x = None
if x is None:
    print('Not a surprise. I just defined x as None.')