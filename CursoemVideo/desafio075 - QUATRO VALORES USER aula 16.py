n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
números = n1,n2,n3,n4
par = 0
print(f'Você digitou os valores {números}.')
print(f'O valor 9 apareceu {números.count(9)} vezes.')
if 3 in números:
    print(f'O valor 3 apareceu na {números.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram ', end = ' ')
for n in números:
    if n%2 == 0:
        print(n, end = ' ')