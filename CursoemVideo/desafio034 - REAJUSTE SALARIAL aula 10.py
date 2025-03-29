salário = float(input('Digite o seu salário: R$ '))
print('O seu salário é R${:.2f}.'.format(salário))
if salário >= 1250:
    aumento10 = salário*(10/100)
    print('O seu aumento será de \033[31m10%\033[m, isto é, R${}.\nSeu salário passará a ser \033[0;32mR${}\033[m.'.format(aumento10,(aumento10+salário)))
else:
    aumento15 = salário*(15/100)
    print('O seu aumento será de \033[31m15%\033[m, isto é, R${}.\nSeu salário passará a ser \033[0;32mR${}\033[m.'.format(aumento15,(aumento15+salário)))