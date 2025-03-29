def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[33mO usuário preferiu não inserir dados.\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            v = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[33mO usuário preferiu não inserir dados.\033[m')
            return 0
        else:
            return v

num=leiaInt('Digite um valor: ')
v=leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {num} e o real foi {v}.')