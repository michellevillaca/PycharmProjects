números = [[],[]]
for n in range(0,7):
    v = (int(input(f'Digite o {n + 1}º valor: ')))
    if v%2 == 0:
        números[0].append(v)
    else:
        números[1].append(v)
números[0].sort()
números[1].sort()
print('-='*30)
print(f'Os valores digitados foram: {números}.')
print(f'Os valores PARES digitados foram: {números[0]}')
print(f'Os valores ÍMPARES digitados foram: {números[1]}')