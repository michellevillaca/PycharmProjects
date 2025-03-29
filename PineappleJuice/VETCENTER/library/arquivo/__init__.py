from VETCENTER.library.interface import *
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
    a = io.open(arq, 'rt', encoding='utf8')
    cabeçalho('PETS CADASTRADOS')
    for linha in a:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        print(f'PET:{dado[0]:<7}{dado[1]:>3} anos \tTutor:{dado[2]:<3}')
    a.close()

def cadastrar(arq,nome,idade,tutor):
    import io
    a = io.open(arq, 'at', encoding='utf8')
    a.write(f'{nome};{idade};{tutor}\n')
    print(f'Novo registro de {nome} adicionado com sucesso!')
    a.close()
