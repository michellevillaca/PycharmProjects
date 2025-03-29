def linha():
    print('-'*30)
    print('     CONTROLE DE TERRENOS')
    print('-'*30)
def área(a,b):
    A = a*b
    print(f'A área de um terreno {a} x {b} é {A}m².')
#Programa Principal
linha()
área(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))