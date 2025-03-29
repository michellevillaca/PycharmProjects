turma = []
while True:
    nome = (str(input('Nome: ')))
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    média = (nota1 + nota2)/2
    turma.append([nome, [nota1, nota2], média])
    r = (str(input('Deseja continuar? [S/N] '))).strip().upper()[0]
    if r not in 'SN':
        r = (str(input('Opção inválida. Deseja continuar? [S/N] ')))
    elif r in 'N':
        break
print('-='*30)
print(f'{'nº':<4} {'NOME':<10} {'MÉDIA':>8}')
print('-'*25)
for i, a in enumerate(turma):
    print(f'{i:<1} {a[0]:^10} {a[2]:>8.1f}')
print('-'*25)
while True:
    pergunta = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if pergunta <= len(turma)-1:
            print(f'As notas de {turma[pergunta][0]} são [{turma[pergunta][1]}]')
            print('-'*25)
    if pergunta == 999:
        print('FINALIZANDO...')
        break
print('<<< VOLTE SEMPRE! >>>')