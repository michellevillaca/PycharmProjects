pessoas = {'nome': 'Michelle', 'sexo': 'F', 'idade': 28, 'peso': 54.5}
del pessoas['peso'] #deletando uma chave
pessoas['idade'] = 30 #modificando o valor de uma chave
pessoas['altura'] = 1.73 #adicionando uma chave
print(pessoas['nome'])
print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())
for k, v in pessoas.items():
    print(f'{k} = {v}')

#criando dicionários dentro de listas
brasil = []
estado1 = {'UF': 'Rio de Janeiro','sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['UF'])
print(brasil[1]['sigla'])

#####

estado = dict()
brasil = list()
for c in range(0,3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy()) #cópia sem relacionar os itens, como na lista [:]
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
    for v in e.values():
        print(v, end = '')
    print()