def aumentar(preço,taxa,str=False):
    '''
    -> Calcular o preço considerando uma porcentagem de aumento.
    :param preço: valor
    :param taxa: porcentagem de aumento (%)
    :param str: se o usuário quer que o valor seja formatado em formato monetário
    :return: valor com o aumento aplicado
    '''
    tot = preço+(preço*taxa/100)
    if str == True:
        return f'R$ {tot:.2f}'
    else:
        return tot

def diminuir(preço,taxa,str=False):
    '''
    -> Calcular o preço considerando uma porcentagem de redução.
    :param preço: valor
    :param taxa: porcentagem de redução (%)
    :param str: se o usuário quer que o valor seja formatado em formato monetário
    :return: valor com redução aplicada
    '''
    tot = preço-(preço*taxa/100)
    if str == True:
        return f'R$ {tot:.2f}'
    else:
        return tot

def dobro(preço,str=False):
    '''
    -> Calcular o dobro de um valor.
    :param preço: valor
    :param str: se o usuário quer que o valor seja formatado em formato monetário
    :return: dobro do valor (valor x 2)
    '''
    tot = preço*2
    if str == True:
        return f'R$ {tot:.2f}'
    else:
        return tot

def metade(preço,str=False):
    '''
    -> Calcular a metade de um valor.
    :param preço: valor
    :param str: se o usuário quer que o valor seja formatado em formato monetário
    :return: metade do valor dado (valor / 2)
    '''
    tot = preço/2
    if str == True:
        return f'R$ {tot:.2f}'
    else:
        return tot

def moeda(preço = 0, moeda = 'R$'):
    '''
    --> Converter o número em formato monetário.
    :param preço: valor
    :param moeda: determina a formatação monetária
    :return: valor em formato monetário
    '''
    return f'{moeda} {preço:>8.2f}'.replace('.',',')

def resumo(v,a,d):
    '''
    -> Resumir todas as operações do módulo MOEDAS
    :param v: valor
    :param a: aumento (%)
    :param d: redução (%)
    :return: resumo de todas as operações do módulo, contando com dobro, metade, aumento e redução do valor
    '''
    from úteis.strings import decoração
    print(decoração.linha('RESUMO DO VALOR'))
    print('Preço analisado:   ', end='')
    print(f'{moeda(v):<15}')
    print('Dobro do preço:    ',end='')
    print(f'{moeda(dobro(v)):<15}')
    print('Metade do preço:   ', end='')
    print(f'{moeda(metade(v)):<15}')
    print(f'{a}% de aumento:    ', end='')
    print(f'{moeda(aumentar(v,a)):<15}')
    print(f'{d}% de redução:    ', end='')
    print(f'{moeda(diminuir(v,d)):<15}')
    print('-'*35)