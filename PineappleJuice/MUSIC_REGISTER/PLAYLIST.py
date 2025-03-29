from MUSIC_REGISTER.library.arquivo import *
from MUSIC_REGISTER.library.interface import *
from time import sleep

arquivo = 'músicas.txt'
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Visualizar Playlist',
                     'Registrar nova música',
                     'Sair do Programa'])
    if resposta == 1:
        lerArquivo(arquivo)
    elif resposta == 2:
        cabeçalho('REGISTRAR NOVA MÚSICA')
        música = str(input('Música: '))
        artista = str(input('Artista: '))
        cadastrar(arquivo,música,artista)
    elif resposta == 3:
        cabeçalho('Saindo... ATÉ LOGO!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.')
    sleep(1)