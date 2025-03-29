jogador = {'nome': str(input('Nome do Jogador: ')).strip().capitalize()}
partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
gols = []
tot = 0
for g in range(0,partidas):
    gol = int(input(f'Quantos gols na partida {g+1}? '))
    gols.append(gol)
    tot += gol
jogador['gols'] = gols
jogador['total'] = tot
print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {jogador['nome']} jogou {partidas} partidas.')
for i,v in enumerate(gols):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {tot} gols.')