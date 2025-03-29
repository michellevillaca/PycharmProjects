print('-'*18)
print('LOJINHA XING LING')
print('-'*18)
total = quant1000 = maisbarato = cont = 0
nomemaisbarato = ' '
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preço = float(input('Preço: R$ '))
    user = ' '
    while user not in 'SN':
        user = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('')
    total += preço
    cont += 1
    if preço >= 1000:
        quant1000 += 1
    if cont == 1 or preço < maisbarato:
        maisbarato = preço
        nomemaisbarato = produto
    #else:
        #if preço < maisbarato:
            #maisbarato = preço
            #nomemaisbarato = produto
    if user in 'Nn':
        break
print('\033[35m{:-^40}\033[m'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi \033[032mR${total:.2f}\033[m.')
print(f'Temos \033[33m{quant1000} produtos\033[m custando mais de R$1000.')
print(f'O produto mais barato foi \033[33m{nomemaisbarato}\033[m, que custa \033[32mR${maisbarato}\033[m.')