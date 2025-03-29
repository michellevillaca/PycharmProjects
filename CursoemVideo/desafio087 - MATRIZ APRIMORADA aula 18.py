matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = somacoluna3 = maiorlinha2 = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um número para [{linha},{coluna}]: '))
        if matriz[linha][coluna]%2 == 0:
            somapares += matriz[linha][coluna]
        if coluna == 2:
            somacoluna3 += matriz[linha][coluna]
        if linha == 1:
            maiorlinha2 = matriz[linha][coluna]
            if matriz[linha][coluna] > maiorlinha2:
                maiorlinha2 = matriz[linha][coluna]
print('\033[1;35m-=\033[m'*30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'\033[1;33m[{matriz[linha][coluna]:^5}]', end='')
    print()
print('\033[1;35m-=\033[m'*30)
print(f'A soma dos \033[1mvalores pares é \033[1;32m{somapares}\033[m.')
print(f'A soma dos \033[1mvalores da terceira coluna é \033[1;31m{somacoluna3}\033[m.')
print(f'O maior valor da \033[1msegunda linha é \033[1;34m{maiorlinha2}\033[m.')
