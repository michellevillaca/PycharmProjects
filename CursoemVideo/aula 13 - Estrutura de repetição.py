i=int(input('Início: '))
f=int(input('Fim: '))
p=int(input('Passo: '))
for c in range (i, f+1, p):
    print(c)

s = 0
for c in range (0,4):
    n=int(input('Digite um valor: '))
    s += n
print('A soma de todos os valores foi {}.'.format(s))