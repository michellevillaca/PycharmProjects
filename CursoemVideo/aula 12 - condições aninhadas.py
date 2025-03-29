nome = str(input('Qual é o seu nome? '))
if nome == 'Michelle':
    print('Que nome lindo!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é bem comum.')
print('Tenha um bom dia {}.'.format(nome))