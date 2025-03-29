n = 1
while n != 0: #enquanto o valor digitado for diferente de 0, ele continuará lendo e pedindo o valor
    n = int(input('Digite um valor: '))
print('Fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')

n = 1
par = ímpar = 0
while n!= 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n%2 == 0:
            par +=1
        else:
            ímpar += 1
print('Você digitou {} números pares e {} números ímpares.'.format(par, ímpar))