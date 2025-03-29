#num=str(input('Digite um número de 0 a 9999: '))
#print('O número {} está dividido em:\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(num,num[3],num[2],num[1],num[0]))

num=int(input('Informe um número: '))
u=num//1%10
d=num//10%10
c=num//100%10
m=num//1000%10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))