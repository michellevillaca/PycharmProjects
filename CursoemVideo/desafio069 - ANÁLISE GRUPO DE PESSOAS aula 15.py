c18 = 0
chomens = 0
cmulheres20 = 0
print('-'*20)
print('CADASTRE UMA PESSOA')
while True:
    print('-' * 20)
    idade = int(input('Idade: '))
    if idade >= 18:
        c18 += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('.'*20)
    if sexo in 'Mm':
        chomens +=1
    elif sexo in 'Ff':
        if idade < 20:
            cmulheres20 += 1
    user = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while user not in 'SsNn':
        user = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if user in 'Nn':
        break
print('='*5, 'FIM DO PROGRAMA', '='*5)
print(f'Total de pessoas com mais de 18 anos: {c18}.\nAo todo, temos {chomens} homens cadastrados e temos {cmulheres20} mulheres com menos de 20 anos.')