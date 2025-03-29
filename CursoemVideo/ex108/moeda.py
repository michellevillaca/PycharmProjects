def aumentar(v,a):
    '''
    -> Calcular o preço considerando uma porcentagem de aumento.
    :param v: valor
    :param a: porcentagem de aumento (%)
    :return: valor com o aumento aplicado
    '''
    porcent = v*(a/100)
    tot = v+porcent
    return tot

def diminuir(v,d):
    '''
    -> Calcular o preço considerando uma porcentagem de redução.
    :param v: valor
    :param d: porcentagem de redução (%)
    :return: valor com redução aplicada
    '''
    porcent = v*(d/100)
    tot = v-porcent
    return tot

def dobro(v):
    '''
    -> Calcular o dobro de um valor.
    :param v: valor
    :return: dobro do valor (valor x 2)
    '''
    return v*2

def metade(v):
    '''
    -> Calcular a metade de um valor.
    :param v: valor
    :return: metade do valor dado (valor / 2)
    '''
    return v/2

def moeda(v = 0, moeda = 'R$'):
    '''
    --> Converter o número em formato monetário.
    :param v: valor
    :param moeda: determina a formatação monetária
    :return: valor em formato monetário
    '''
    return f'{moeda} {v}'.replace('.',',')