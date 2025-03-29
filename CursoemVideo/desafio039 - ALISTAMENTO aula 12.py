from datetime import date
ano=int(input('Digite o seu ano de nascimento: '))
if date.today().year - ano == 18:
    print('PERÍODO DE ALISTAMENTO. Você faz 18 anos neste ano.')
elif date.today().year - ano < 18:
    print('Você tem {} anos.'.format(date.today().year - ano))
    print('Faltam {} anos para o seu período de alistamento.'.format(18 - (date.today().year - ano)))
else:
    print('Você tem {} anos. Seu período de alistamento está {} ano(s) ATRASADO.'.format((date.today().year - ano),(date.today().year - ano)-18))