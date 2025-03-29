nome=input('Nome do aluno: ')
n1=float(input('Nota 1: '))
n2=float(input('Nota 2: '))
ma=(n1+n2)/2
print('Considerando que a primeira nota foi {:.1f} e a segunda nota foi {:.1f}, a média do aluno {} é {:.1f}.'.format(n1,n2,nome,ma))