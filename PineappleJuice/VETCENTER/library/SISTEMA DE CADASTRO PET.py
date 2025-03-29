from VETCENTER.library.arquivo import *
from VETCENTER.library.interface import *
from time import sleep

arquivo = 'cadastropet.txt'
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

cabeçalho('CADASTRO VETCENTER')
while True:
    resp = menu(['Lista de PETS cadastrados',
                 'Cadastrar novo PET',
                 'Sair do Sistema'])
    if resp == 1:
        lerArquivo(arquivo)
    elif resp == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome do PET: '))
        idade = leiaFloat('Idade (em anos): ')
        tutor = str(input('Tutor(a): '))
        cadastrar(arquivo,nome,idade,tutor)
    elif resp == 3:
        cabeçalho('Saindo do Sistema... ATÉ LOGO!')
        break
    else:
        print('\033[31mERRO! Por favor, digite uma opção válida do menu.\033[m')
    sleep(1)