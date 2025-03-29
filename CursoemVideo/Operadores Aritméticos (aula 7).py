n1=int(input('Um valor: '))
n2=int(input('Outro valor: '))
s=n1+n2
mult=n1*n2
div=n1/n2
divint=n1//n2
e=n1**n2
restdiv=n1%n2
print('A soma vale {}.'.format(s),end=' ')
print('A multiplicação dos números é {}.'.format(mult),end=' ')
print('A divisão de {} por {} é {}.'.format(n1,n2,div),end=' ')
print('A divisão inteira de {} por {} é {}.'.format(n1,n2,divint),end=' ')
print('{} elevado a {} é igual a {}.'.format(n1,n2,e),end=' ')
print('O resto da divisão entre {} e {} é {}.'.format(n1,n2,restdiv))
print('Resumindo,\nsoma: {} \nmultiplicação: {} \ndivisão: {} \nexponenciação: {} \ndivisão inteira: {} \nresto da divisão: {}'.format(s,mult,div,e,divint,restdiv))