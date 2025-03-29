listanum = []
maior = menor = 0
for posição in range (0,5):
    listanum.append(int(input(f'Digite um valor para a posição {posição}: ')))
    if posição == 0:
        maior = menor = listanum[posição]
    else:
        if listanum[posição] > maior:
            maior = listanum[posição]
        if listanum[posição] < menor:
            menor = listanum[posição]
print('-='*30)
print(f'você digitou os números {listanum}')
print(f'O maior número digitado é {maior}, nas posições ', end = '')
for i,v in enumerate(listanum):
    if v == maior:
        print(f'{i}; ', end ='')
print()
print(f'O menor número digitado foi {menor} nas posições ', end = '')
for i,v in enumerate(listanum):
    if v == menor:
        print(f'{i}; ', end = '')
print()