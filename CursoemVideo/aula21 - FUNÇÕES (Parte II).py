help(print)

def contador(i,f,p):
    """
    --> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ',end='')
        c += p
    print('FIM!')

help(contador)
contador(1,10,2)

def somar(a=0,b=0,c=0):
    s = a+b+c
    print(f'A soma vale {s}.')
somar(3)
somar(4,3,6)
somar(2,4)

def função():
    n1=4
    print(f'n1 dentro vale {n1}.')
n1 = 2
print(f'n1 global vale {n1}.')
função()

def multiplicar(a=1,b=1,c=1):
    m = a*b*c
    return m
r1 = multiplicar(4,5,2)
r2 = multiplicar(2,2,2)
r3 = multiplicar (10,2)
print(f'Os resultados foram {r1}, {r2} e {r3}.')