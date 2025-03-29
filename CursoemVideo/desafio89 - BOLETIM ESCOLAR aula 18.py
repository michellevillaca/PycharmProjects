turma = []
alunos = []
while True:
    alunos.append(str(input('Nome: ')))
    alunos.append(float(input('Nota 1: ')))
    alunos.append(float(input('Nota 2: ')))
    turma.append(alunos[:])
    alunos.clear()
    r = (str(input('Deseja continuar? [S/N] '))).strip().upper()[0]
    if r not in 'SN':
        r = (str(input('Opção inválida. Deseja continuar? [S/N] ')))
    elif r in 'N':
        break
print('-='*30)
print(f'{'nº':<1} {'NOME':^8} {'MÉDIA':>10}')
print('-'*25)
for c in range(0,len(turma)):
    print(f'{c:<1} {turma[c][0]:^8} {(turma[c][1]+turma[c][2])/2:>10}')
print('-'*25)
while True:
    pergunta = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    for c in range(0,len(turma)):
        if pergunta == c:
            print(f'As notas de {turma[c][0]} são [{turma[c][1], turma[c][2]}]')
            print('-'*25)
    if pergunta == 999:
        break