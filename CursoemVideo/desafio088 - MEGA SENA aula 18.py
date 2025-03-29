from random import randint
from time import sleep
print('-'*20)
print(f'{'JOGO NA MEGA SENA':^20}')
print('-'*20)
lista = []
jogos =[]
cont = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*5, f'SORTEANDO OS {cont} JOGOS','-='*5)
for jogo in range(0,cont):
    for números in range(0,6):
        n = randint(0,60)
        if n not in jogos:
            jogos.append(n)
        elif n in jogos:
            n = randint(0,60)
            if n not in jogos:
                jogos.append(n)
        if números == 5:
            lista.append(jogos[:])
            jogos.clear()
            sleep(1)
            print(f'Jogo {jogo+1}: {lista[jogo]}')
sleep(1)
print('-='*3, '< BOA SORTE! >', '-='*3)