def linha(txt):
    '''
    -> Mostrar um texto em forma de título (com linhas em cima e embaixo).
    :param txt: mensagem digitada em string
    :return: texto decorado entre linhas
    '''
    tamanho = len(txt) + 20
    print('-'*tamanho)
    print(f'{txt}'.center(30))
    print('-'*tamanho)

def linhapadrão(txt):
    print('-'*30)
    print(f'{txt}'.center(30))
    print('-'*30)