aluno = {'Nome': str(input('Nome: ')).strip().capitalize()}
aluno['Média'] = float(input(f'Média de {aluno['Nome']}: '))
#print(f'Nome é igual a {aluno['nome']}\nMédia é igual a {aluno['média']}')
if aluno['Média'] >= 7:
    aluno['Situação'] = 'APROVADO'
elif aluno['Média'] >= 5:
    aluno['Situação'] = 'RECUPERAÇÃO'
else:
    aluno['Situação'] = 'REPROVADO'
#print(f'Situação é igual a {aluno['situação']}.')
print('-='*30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')