turnê = []
artista = {}
músicas = []
while True:
    artista.clear()
    artista['nome'] = str(input('Artista: '))
    total = int(input(f'Quantos shows {artista['nome']} fez? '))
    músicas.clear()
    for show in range(0,total):
        músicas.append(int(input(f'Quantas músicas no show {show+1}? ')))
    artista['shows'] = total
    artista['músicas'] = músicas[:]
    turnê.append(artista.copy())
    while True:
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if r in 'SN':
            break
        print('ERRO! Digite apenas S ou N: ')
    if r == 'N':
        break
print(turnê)
print('-='*30)
print(f'{'cod.':>3} ', end ='')
for i in artista.keys():
    print(f'{i:<20}', end='') #índices da tabela
print()
print('-'*60)
for k, v in enumerate(turnê):
    print(f'{k:>3}  ', end='') #mostrar a chave [que nesse caso são os índices]
    for dado in v.values(): #para dado em cada valor em valores
        print(f'{str(dado):<20}' , end ='')
    print()
print('-'*60)
while True:
    busca = int(input('Mostrar dados para qual artista? (999 para parar): '))
    if busca == 999:
        break
    elif busca >= len(turnê):
        print(f'ERRO! Não existe jogador com código {busca}.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {turnê[busca]['nome']}: ')
        for show, música in enumerate(turnê[busca]['músicas']):
            print(f' No show {show+1}, tocou {música} músicas.')
    print('-' * 60)
print(' << VOLTE SEMPRE! >> ')