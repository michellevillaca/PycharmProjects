n1=int(input('Digite um número: '))
n2=int(input('Digite mais um número: '))
n3=int(input('Digite mais um número: '))
#Achando o maior número:
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('\033[33mMaior número: \033[34m{}'.format(maior))
#Achando o menor número:
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('\033[33mMenor número: \033[31m{}'.format(menor))