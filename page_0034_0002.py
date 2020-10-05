#The above is also true for mutable types (like list , dict , etc.) just as it is true for immutable types (like int , string ,
#tuple , etc.):

x = y = [7,8,9]     # x and y refer to the same list object just created, [7,8,9]
                    # x e y referem-se ao mesmo objeto de lista recém-criado, [7,8,9]
print(x)
x = [13, 8, 9]      # now refers to a different list object just created, [13,8,9]
                    # agora se refere a um objeto de lista diferente recém-criado, [13,8,9]
print(y)            # printing the value of the list using its other name        
                    # imprimindo o valor da lista usando seu outro nome
print(x)            # printing the value of the list using its other name
                    # imprimindo o valor da lista usando seu outro nome

#So far so good. Things are a bit different when it comes to modifying the object (in contrast to assigning the name to
#a different object, which we did above) when the cascading assignment is used for mutable types. Take a look
#below, and you will see it first hand:

#Por enquanto, tudo bem. As coisas são um pouco diferentes quando se trata de modificar o objeto (em contraste com atribuir o nome a
#um objeto diferente, que fizemos acima) quando a atribuição em cascata é usada para tipos mutáveis. Dê uma olhada
#abaixo, e você verá em primeira mão:

x = y = [7,8,9] # x and y are two different names for the same list object just created, [7,8,9]
                # x e y são dois nomes diferentes para o mesmo objeto de lista recém-criado, [7,8,9]
x[0] = 13   # we are updating the value of the list [7, 8, 9] through one of its names, x in this case 
            # estamos atualizando o valor da lista [7, 8, 9] por meio de um de seus nomes, x neste caso
print(y)    # printing the value of the list using its other name 
            # imprimindo o valor da lista usando seu outro nome
print(x)    # printing the value of the list using its other name 
            # imprimindo o valor da lista usando seu outro nome
# Output: [13, 8, 9] # hence, naturally the change is reflected # portanto, naturalmente a mudança é refletida

#Nested lists are also valid in python. This means that a list can contain another list as an element.
#Listas aninhadas também são válidas em python. Isso significa que uma lista pode conter outra lista como um elemento.
x = [1,2, [3,4,5], 6,7]     #this is nested list 
                            #esta é uma lista aninhada
print(x[2])                  #exibe resultado da lista aninhada
#Output: [3,4,5]

print(x[2][1])
#Output: 4

#Lastly, variables in Python do not have to stay the same type as which they were first defined -- you can simply use
#= to assign a new value to a variable, even if that value is of a different type.

#Por último, as variáveis em Python não precisam permanecer do mesmo tipo que foram definidas inicialmente - 
# você pode simplesmente usar = para atribuir um novo valor a uma variável, mesmo se esse valor for de um tipo diferente.

a = 2       #atribuir 2 a variavel a
print(a)    #exibir a
#Output: 2


