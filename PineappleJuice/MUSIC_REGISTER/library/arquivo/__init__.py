from MUSIC_REGISTER.library.interface import *

def arquivoExiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(arq):
    a = open(arq, 'wt+')
    a.close()
    print(f'Arquivo {arq} criado com sucesso!')

def lerArquivo(arq):
    import io
    a = io.open(arq, 'rt', encoding ='utf8')
    cabeçalho('SUA PLAYLIST')
    for linha in a:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n','    ')
        print(f'{dado[0]:<30}{dado[1]:<15}')
    a.close()

def cadastrar(arq,música,artista):
    import io
    a = io.open(arq, 'at', encoding='utf8')
    a.write(f'{música};{artista}\n')
    print('Música registrada com sucesso!')
    a.close()