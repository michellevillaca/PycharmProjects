números = []
pares = []
ímpares = []
while True:
    números.append(int(input('Digite um número: ')))
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r not in 'SN':
        r = str(input('Opção inválida. Deseja continuar? [S/N] ')).strip().upper()[0]
    elif r in 'N':
        break
for i, v in enumerate(números):
    if v%2 == 0:
        pares.append(v)
    elif v% 2 == 1:
        ímpares.append(v)
print('-='*30)
print(f'A lista completa é {números}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')