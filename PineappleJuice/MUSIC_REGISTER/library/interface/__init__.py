def cabeçalho(txt):
    print('-'*42)
    print(f'\033[46m{txt.center(42)}')
    print('\033[m-'*42)

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número válido.')
            continue
        else:
            return n

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'\033[42m{cont} - \033[45m{item}')
        cont += 1
    print('\033[m-'*42)
    opç = leiaInt('\033[32mSua opção: \033[m')
    return opç