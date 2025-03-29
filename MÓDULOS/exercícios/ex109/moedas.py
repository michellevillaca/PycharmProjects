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