n = int(input('Digite um número para calcular seu fatorial: '))
cont = n
f = 1 #sempre que trabalhamos com multiplicação, o "número limpo" é 1 (pois qualquer número vezes 1 é igual a ele mesmo); para adição, o "número limpo" é zero, pois é do zero que começamos a soma com o número que queremos.
print('Calculando {}! = '.format(n), end='')
while cont > 0:
    print('{} '.format(cont), end = '')
    print('x' if cont > 1 else '=', end = ' ')
    f *= cont
    cont -= 1
print('{}'.format(f))