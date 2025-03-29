teste = list()
teste.append('Michelle')
teste.append(28)
galera = list()
galera.append(teste[:]) #[:] significa uma cópia, pois, sem esse elemento, eu crio uma dependência entre as listas, de modo que, o que eu mudar depois, mudará a lista anterior.
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)

turma = [['João',19], ['Ana',33], ['Joaquim',13], ['Maria',45]]
print(turma)
print(turma[0][0])
print(turma[1][0])
print(turma[2])
print(turma[0][1])
for p in turma:
    print(p)
    print(p[0])
    print(f'{p[0]} tem {p[1]} anos de idade.')

pessoas = list()
dados = list() #lista temporária
totmaior = totmenor = 0
for c in range (0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    pessoas.append(dados[:])
    dados.clear()
for p in pessoas: #para cada pessoa em pessoas
    if p[1] >= 21: #se o espaço de idade (1) for maior ou igual a 21
        print(f'{p[0]} é maior de idade.') #mostro o espaço de nome (0) de quem é maior de idade.
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')