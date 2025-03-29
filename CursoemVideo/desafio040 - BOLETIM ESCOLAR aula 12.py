aluno=str(input('Aluno: '))
n1=float(input('Primeira nota: '))
n2=float(input('Segunda nota: '))
média=(n1+n2)/2
print('A média de {} é {}.'.format(aluno,média))
if média < 5:
    print('\033[31mREPROVADO\033[m')
elif 5 < média < 6.9:
    print('\033[33mRECUPERAÇÃO\033[m')
else:
    print('\033[32mAPROVADO\033[m')