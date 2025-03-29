def ficha(jogador='<desconhecido>',gol=0):
    print(f'O jogador {jogador} fez {gol} gol(s) no campeonato.')
    print('-' * 40)

#Programa Principal
print('-'*40)
nome = str(input('Nome do Jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome,gols)