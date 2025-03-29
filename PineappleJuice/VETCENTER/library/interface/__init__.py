def cabeçalho(txt):
    print('-'*42)
    print(f'\033[45m{txt.center(42)}')
    print('\033[m-'*42)

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número válido.\033[m')
            continue
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número válido.\033[m')
            continue
        else:
            return n

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    cont=1
    for item in lista:
        print(f'\033[43m{cont} -\033[m \033[46m{item}')
        cont += 1
    print('\033[m-'*42)
    opção = leiaInt('\033[33mSua Opção: \033[m')
    return opção