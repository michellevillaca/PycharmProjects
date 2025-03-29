from random import randint
from time import sleep
jogos = {}
print('VALORES SORTEADOS:')
for j in range(0,4):
    sleep(0.5)
    jogos['jogador'] = f'jogador {j+1}'
    jogos['dado'] = randint(1,6)
    print(f'O {jogos['jogador']} tirou {jogos['dado']}')
#inacabado