from time import sleep
c = ('\033[m',          # 0 = sem cores
     '\033[0;30;41m',   # 1 = vermelho
     '\033[0;30;42m',   # 2 = verde
     '\033[0;30;43m',   # 3 = amarelo
     '\033[0;30;44m',   # 4 = azul
     '\033[0;30;45m',   # 5 = roxo
     '\033[7;30m')      # 6 = preto
def ajuda(comando):
    título(f'Acessando o manual do comando \'{comando}\'', 4)
    print(c[5], end='')
    help(comando)
    print(c[0], end='')
    sleep(2)

def título(msg, cor=0):
    tamanho = len(msg) + 4
    print(c[cor], end ='')
    print('~'*tamanho)
    print(f'  {msg}')
    print('~'*tamanho)
    print(c[0], end='')
    sleep(0.5)

#Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO', 1)