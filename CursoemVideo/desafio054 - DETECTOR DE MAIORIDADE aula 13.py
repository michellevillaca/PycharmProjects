from datetime import date
from time import sleep
atual=date.today().year
contmenor = 0
contmaior = 0
for pess in range(1,8):
    nascimento=int(input('Digite o ano de nascimento da pessoa {}: '.format(pess)))
    idade=atual-nascimento
    sleep(0.3)
    print('Quem nasceu em {} tem {} anos.'.format(nascimento,idade))
    print(' ')
    if idade < 21:
        contmenor += 1
    else:
        contmaior +=1
print('{} pessoas são menores de idade.'.format(contmenor))
print('{} pessoas são maiores de idade.'.format(contmaior))