listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-'*40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-'*40)
for posição in range (0,len(listagem)):
    if posição % 2 == 0:
        print(f'{listagem[posição]:.<30}', end = '') #".<30" significa pontos alinhados à esquerda, estipulando o print da variável em trinta caracteres.
    else:
        print(f'R${listagem[posição]:>7.2f}') #:>7 para alinhar a variável à direita com 7 espaços, e .2f para mostrar duas casas decimais (pois queremos ver em formato de preço).
print('-'*40)