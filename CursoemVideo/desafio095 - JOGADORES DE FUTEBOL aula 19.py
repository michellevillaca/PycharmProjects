jogadores = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome']  = str(input('Nome do Jogador: ')).strip().capitalize()
    tot = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'  Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = tot
    jogadores.append(jogador.copy())
    while True:
        r = str(input('Deseja continuar? [S/N] ')).upper()
        print('-' * 20)
        if r in 'SN':
            break
        print('ERRO! Digite apenas S ou N: ')
    if r == 'N':
        break
print('-='*30)
print(jogadores)
print('-='*30)
print('cod ', end ='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end ='')
    for dado in v.values():
        print(f'{str(dado):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {busca}.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[busca]['nome']}: ')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print(' << VOLTE SEMPRE! >> ')