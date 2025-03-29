from datetime import date
ano=int(input('Que ano você quer analisar? (Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
#Um ano é bissexto se ele é múltiplo de 4 (isto é, divisível por 4), exceto quando terminados em 00.
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print('O ano \033[33m{}\033[m é \033[7mbissexto\033[m.'.format(ano))
else:
    print('O ano \033[33m{}\033[m \033[7mnão é bissexto\033[m.'.format(ano))