def leiaInt(n):
    while True:
        print('Digite um número: ', end='')
        número = str(input(''))
        if número.isnumeric():
            return número
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')

#Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')