from ex115.library.interface import *
from ex115.library.arquivo import *
from time import sleep
from úteis import cores

arq = 'cursoemvídeo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

cabeçalho('SISTEMA ARQUIVO v1.0')
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho(f'    {cores.corfundo[5]}Saindo do Sistema... Até logo!{cores.cor[0]}')
        break
    else:
        print(f'{cores.cor[1]}ERRO! Por favor, digite uma opção válida do menu.{cores.cor[0]}')
    sleep(1)