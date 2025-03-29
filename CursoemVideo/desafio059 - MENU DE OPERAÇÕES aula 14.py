from time import sleep
v1 = float(input('Primeiro valor: '))
v2 = float(input('Segundo valor: '))
menu = ' '
while menu != 5:
    menu = int(input('\033[7mMENU DE OPÇÕES:\033[m\n \033[42m[1]\033[m somar\n \033[42m[2]\033[m multiplicar\n \033[42m[3]\033[m maior valor\n \033[42m[4]\033[m novos números\n \033[42m[5]\033[m sair do programa\nDigite sua opção: '))
    if menu == 1:
        print('\033[33m{} + {} = {}\033[m'.format(v1,v2,(v1+v2)))
        print(' ')
        sleep(1)
    elif menu == 2:
        print('\033[31m{} x {} = {}\033[m'.format(v1,v2,(v1*v2)))
        print(' ')
        sleep(1)
    elif menu == 3:
        if v1 > v2:
            print('\033[34m{} é maior que {}.\033[m'.format(v1,v2))
            print(' ')
            sleep(1)
        else:
            print('\033[34m{} é maior que {}.\033[m'.format(v2,v1))
            print(' ')
            sleep(1)
    elif menu == 4:
        print(' ')
        v1 = float(input('Primeiro valor: '))
        v2 = float(input('Segundo valor: '))
        print(' ')
print('Você encerrou o programa.')