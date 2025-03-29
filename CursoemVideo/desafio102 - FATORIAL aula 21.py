def fatorial(n, show=False):
    '''
    --> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não o cálculo.
    :return: O valor do Fatorial de um número n.
    '''
    fator = 1
    print(f'Calculando {n}! = ', end='')
    for c in range(n,0,-1):
        if show:
            print(c, end='')
            if c>1:
                print(' x ', end='')
            else:
                print(' = ',end ='')
        fator *= c
    return fator

#Programa Principal
print(fatorial(5, show = True))
print(fatorial(6, show=False))
help(fatorial)