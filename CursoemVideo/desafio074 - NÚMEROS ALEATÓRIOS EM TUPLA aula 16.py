from random import randint
n1 = randint(0,10)
n2 = randint(0,10)
n3 = randint(0,10)
n4 = randint(0,10)
n5 = randint(0,10)
lista = n1,n2,n3,n4,n5
print(f'Os valores sorteados foram {lista}.')
maior = menor = n1
if n2 > n1 and n2 > n3 and n2> n4 and n2 > n5:
    maior = n2
elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
    maior = n3
elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
    maior = n4
else:
    maior = n5
print(f'O maior valor sorteado foi {maior}.')
if n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
    menor = n2
elif n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5:
    menor = n3
elif n4 < n1 and n4 < n2 and n4 < n3 and n4 < n5:
    menor = n4
else:
    menor = n5
print(f'O menor valor sorteado foi {menor}.')