from datetime import date
atual=date.today().year
nasc=int(input('Ano de nascimento: '))
idade=atual-nasc
print('Quem nasceu em {} tem {} em {}.'.format(nasc,idade,atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o seu alistamento.'.format(saldo))
else:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))