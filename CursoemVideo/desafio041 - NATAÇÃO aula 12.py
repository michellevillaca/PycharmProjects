from datetime import date
atual=date.today().year
ano=int(input('Ano de nascimento: '))
idade=atual-ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano,idade,atual))
if idade <= 9:
    print('CATEGORIA: MIRIM')
elif 9 < idade <= 14:
    print('CATEGORIA: INFANTIL')
elif 14 < idade <= 19:
    print('CATEGORIA: JÚNIOR')
elif 19 < idade <= 25:
    print('CATEGORIA: SÊNIOR')
else:
    print('CATEGORIA: MASTER')