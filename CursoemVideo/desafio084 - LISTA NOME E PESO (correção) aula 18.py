listatemporária = []
listaprincipal = []
maior = menor = 0
while True:
    listatemporária.append(str(input('Nome: ')))
    listatemporária.append(int(input('Peso: ')))
    if len(listaprincipal) == 0:
        maior = menor = listatemporária[1]
    else:
        if listatemporária[1] > maior:
            maior = listatemporária[1]
        if listatemporária[1] < menor:
            menor = listatemporária[1]
    listaprincipal.append(listatemporária[:])
    listatemporária.clear()
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(listaprincipal)} pessoas.')
print(f'O maior peso foi de {maior}kg, que é de ',end = '')
for p in listaprincipal:
    if p[1] == maior:
        print(f'{p[0]}; ', end = '')
print()
print(f'O menor peso foi de {menor}kg, que é o de ', end ='')
for p in listaprincipal:
    if p[1] == menor:
        print(f'{p[0]}; ', end = '')