print('\033[35m-=-'*20)
print(' '*15,'CALCULADORA DE EMPRÉSTIMO')
print('-=-'*20,'\033[m')
casa=float(input('Valor da casa: R$ '))
salário=float(input('Seu salário: R$ '))
tempo=int(input('Quantos anos de financiamento? '))
print('O número de prestações será de: \033[33m{} parcelas\033[m, totalizando \033[32mR${:.2f}\033[m por mês.'.format((tempo*12),casa/(tempo*12)))
mensalidade=casa/(tempo*12)
if mensalidade > (salário*(30/100)):
    print('EMPRÉSTIMO NEGADO. Infelizmente, a prestação mensal excede 30% do seu salário.')
else:
    print('EMPRÉSTIMO APROVADO!')