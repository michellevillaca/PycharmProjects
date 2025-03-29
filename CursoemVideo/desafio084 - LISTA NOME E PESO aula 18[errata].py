pessoas = []
dados = []
cont = maior = menor = 0
nomemaispes = nomemaislev = ' '
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso (kg): ')))
    pessoas.append(dados[:])
    dados.clear()
    cont += 1
    for p in pessoas:
        if p == 0:
            maior = pessoas[0][1]
            nomemaispes = pessoas[0][0]
        else:
            if p[1] > maior:
                maior = p[1]
                nomemaispes = p[0]
    for p in pessoas:
        if p == 0:
            menor = pessoas[0][1]
            nomemaislev = pessoas[0][0]
        else:
            if p[1] < menor:
                menor = p[1]
                nomemaislev = p[0]
    r = (str(input('Deseja continuar? [S/N]: '))).strip().upper()[0]
    if r not in 'SN':
        r = (str(input('Opção inválida. Deseja continuar? [S/N] '))).strip().upper()[0]
    if r in 'N':
        break
print(pessoas[1])
print(f'Ao todo, você cadastrou {cont} pessoas.')
print(f'O maior peso foi de {maior}kg, que é o peso de {nomemaispes}.')
print(f'O menor peso foi de {menor}kg, que é o peso de {nomemaislev}.')