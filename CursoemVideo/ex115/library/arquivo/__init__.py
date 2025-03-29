from ex115.library.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # rt = read & text, para tentar abrir o arquivo em modo texto.
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # write, text & +, para escreve um arquivo de texto, e se o arquivo não existir, ele cria.
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    import io
    try:
        a = io.open(nome, 'rt', encoding='utf8') #para conseguir ler palavras com acentuação.
    except:
        print('ERRO ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    import io
    try:
        a = io.open(arq, 'at', encoding='utf8') # append & text, para incorporar um valor/texto ao arquivo de texto.
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()