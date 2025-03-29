def leiadinheiro(v):
    while True:
        print('Digite o preço: R$ ', end = '')
        v = str(input(''))
        if v.isnumeric():
            return v
            break
        elif v in (str, ',.'):
            return v
            break
        else:
            print(f'\033[1;31mERRO: "{v}" é um preço inválido!\033[m')

p = leiadinheiro('Digite o preço: R$ ')