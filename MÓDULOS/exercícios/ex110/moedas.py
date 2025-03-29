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
        return moeda(preço)
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
        return moeda(preço)
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
        return moeda(preço)
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
        return moeda(preço)
    else:
        return tot

def moeda(preço = 0, moeda = 'R$'):
    '''
    --> Converter o número em formato monetário.
    :param preço: valor
    :param moeda: determina a formatação monetária
    :return: valor em formato monetário
    '''
    return f'{moeda} {preço:.2f}'.replace('.',',')

def resumo(preço=0,taxaaum=10,taxared=5):
    '''
    -> Resumir todas as operações do módulo MOEDAS
    :param preço: valor
    :param taxaaum: aumento (%)
    :param taxared: redução (%)
    :return: resumo de todas as operações do módulo, contando com dobro, metade, aumento e redução do valor
    '''
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{moeda(dobro(preço))}')
    print(f'Metade do preço: \t{moeda(metade(preço))}')
    print(f'{taxaaum}% de aumento: \t{moeda(aumentar(preço,taxaaum))}')
    print(f'{taxared}% de redução: \t{moeda(diminuir(preço,taxared))}')
    print('-'*30)