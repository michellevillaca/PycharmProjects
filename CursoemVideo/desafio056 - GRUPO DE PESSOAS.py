tot = 0
maisvelho = 0
contmulheres = 0
nomehomemvelho = ' '
for pessoa in range (1,5):
    nome = str(input('Digite o seu nome: '))
    idade = int(input('Digite a sua idade: '))
    gênero = int(input('Qual é o seu gênero?\n [1] Feminino\n [2] Masculino\nDigite a opção desejada: '))
    print(' ')
    tot += idade
    média = tot/4
    if pessoa == 1:
        if gênero == 2:
            maisvelho = idade
            nomehomemvelho = nome
    else:
        if gênero == 2:
            if idade > maisvelho:
                maisvelho = idade
                nomehomemvelho = nome
    if gênero == 1:
        if idade < 20:
            contmulheres += 1

print('A média de idade do grupo é de {} anos.'.format(média))
print('O homem mais velho do grupo tem {} anos, que é o {}.'.format(maisvelho,nomehomemvelho))
print('Há {} mulheres menores de 20 anos no grupo.'.format(contmulheres))