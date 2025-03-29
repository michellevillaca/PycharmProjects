sexo = str(input('Por favor, informe seu sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [F/M]: '))
if sexo == 'F'.upper():
    print('Sexo FEMININO registrado com sucesso.')
else:
    print('Sexo MASCULINO registrado com sucesso.')