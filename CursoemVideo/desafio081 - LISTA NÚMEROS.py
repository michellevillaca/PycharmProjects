lista = []
cont = 0
while True:
    n = int(input('Digite um valor: '))
    cont += 1
    lista.append(n)
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r not in 'SN':
        r = str(input('Opção inválida. Deseja continuar? [S/N] ')).strip().upper()[0]
    elif r in 'N':
        break
lista.sort(reverse = True)
print('-='*30)
print(f'Você digitou {cont} elementos.') #outra opção em vez de usar o 'cont' é colocar {len(lista)}
print(f'Os valores em ordem decrescente são {lista}.')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 NÃO FAZ parte da lista.')