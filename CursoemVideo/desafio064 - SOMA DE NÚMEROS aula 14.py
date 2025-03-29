print('CALCULADORA DE NÚMEROS')
print('Digite quantos números quiser; ao final, vamos somá-los. Para parar a contagem, digite "999".')
soma = 0
cont = 0
n = 1
while n != 999:
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if n == 999:
        soma -= 999
        cont -= 1
print('Foram digitados {} números, e a soma deles é igual a {}.'.format(cont,soma))