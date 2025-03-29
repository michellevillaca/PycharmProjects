números = []
pares = []
ímpares = []
while True:
    n = (int(input('Digite um número: ')))
    números.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        ímpares.append(n)
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r not in 'SN':
        r = str(input('Opção inválida. Deseja continuar? [S/N] ')).strip().upper()[0]
    elif r in 'N':
        break
print('-='*30)
print(f'A lista completa é {números}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')