pessoa = {}
grupo = []
soma = média = 0
while True:
    pessoa.clear() #antes de ler uma nova pessoa, eu preciso apagar a pessoa antes de colocar no grupo
    pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F: ')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    grupo.append(pessoa.copy())
    while True:
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if r in 'SN':
            break
        print('ERRO! Responda apenas S ou N: ')
    if r == 'N':
        break
print('-='*30)
print(grupo)
print(f'=> O grupo tem {len(grupo)} pessoas.')
média = soma/len(grupo)
print(f'=> A média de idade é de {média:5.2f} anos.') #5 casas ao todo e 2 decimais
print(f'=> As mulheres cadastradas foram:', end = '')
for p in grupo:
    if p['sexo'] == 'F':
        print(f'{p['nome']}; ', end = '')
print()
print('=> Lista das pessoas que estão acima da média:')
for p in grupo:
    if p['idade'] >= média:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')