num = [2, 5, 9, 1]
num[2] = 3 #mudando o valor do índice [2], que era 9.
num.append(7) #adicionando o valor 7 ao fim da lista.
num.sort() #colocando em ordem.
num.sort(reverse=True) #colocando os números em ordem descrescente.
num.insert(2,2) #adicionando o valor 2 na posição 2. O programa pega o número da posição 2, joga para a direita, e coloca o 2 ali.
num.pop(1) #eliminando o número em posição 1 na lista.
num.remove(2) #ele remove a primeira ocorrência do elemento na lista, portanto, somente o primeiro 2.
if 4 in num:
    num.remove(4)
else:
    print('Não encontrei o número 4.')
print(num)
print(f'Essa lista tem {len(num)} elementos.')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(f'Os valores da minha lista são: ', end = ' ')
for v in valores:
    print(f'{v}', end = ' ')
print('')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}.')
print('Cheguei ao final da lista.')

valores = list()
for cont in range (0,5):
    valores.append(int(input('Digite um valor: ')))
for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao fim da lista.')