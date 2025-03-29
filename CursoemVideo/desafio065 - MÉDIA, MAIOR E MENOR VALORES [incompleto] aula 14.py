n1 = int(input('Digite um valor: '))
soma = n1
média = n1
cont = 1
user = ' '
while user != 'N'.strip().upper():
    n2 = int(input('Digite outro valor: '))
    user = str(input('Deseja digitar outro valor? [S/N] ')).strip().upper()
    soma += n2
    cont += 1
    média = soma/cont
print('Você digitou {} números. A soma desses números foi {}, e sua média foi {}.'.format(cont,soma,média))