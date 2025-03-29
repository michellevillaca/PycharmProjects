def leiadinheiro(msg):
    válido = False #criar uma variável (flag) para dizer se o número é válido ou inválido; começamos com False porque não leu nada (não é válido) ainda
    while not válido: #enquanto não for válido, ele vai ficar lendo o valor
        entrada = str(input(msg)).replace(',','.') #converter todas as vírgulas digitadas em pontos, assim a leitura acontece em formato float
        if entrada.isalpha() or entrada.strip() == '': #no segundo comando, para o caso de a pessoa digitar vários espaços, o comando retira os espaços, e, se o que sobrar for um espaço vazio, então ele consegue ler
            print(f'\033[1;31mERRO: "{entrada}" é um preço inválido!\033[m')
        else:
            válido = True
            return float(entrada)