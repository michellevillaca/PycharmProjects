def título(txt):
    print('-'*30)
    print(txt)
    print('-'*30)
título('      CURSO EM VÍDEO   ')
título('   MICHELLE VILLAÇA ANDRY ')

def soma(a,b):
    s = a+b
    print(f'A soma de {a} + {b} é igual a {s}.')
#Programa Principal:
soma(4,5)
soma(9,9)
soma(1,2)
soma(b=3, a=8) #mudando a ordem
print()

def contador(*núm):
    for valor in núm:
        print(f'{valor}', end='; ')
    tam = len(núm)
    print(f'Recebi os valores {núm} e são a todo {tam} números.')
contador(1,2,3)
contador(7,5,3,2,8,5,4)
contador(2,2)

def dobra(lst):
    posição = 0
    while posição < len(lst):
        lst[posição] *=2
        posição +=1
valores = [6,3,5,6,7,8]
dobra(valores)
print(valores)