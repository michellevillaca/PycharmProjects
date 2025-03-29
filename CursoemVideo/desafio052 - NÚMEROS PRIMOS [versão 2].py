num=int(input('Digite um número: '))
tot = 0
for c in range (1,num+1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, tot))
if tot == 2: #o número que é divísivel por apenas dois números: somente por 1 e por ele mesmo
    print('Por isso, ele é PRIMO.')
else:
    print('Por isso, ele NÃO É PRIMO.')