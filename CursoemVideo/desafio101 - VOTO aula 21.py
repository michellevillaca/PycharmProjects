def voto(idade):
    from datetime import date
    idade = date.today().year - nasc
    if 16 <= idade < 18 or idade >= 75:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    elif 18 < idade < 75:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    elif idade < 18:
        print(f'Com {idade} anos: NÃO VOTA.')

idade = 0
print('-'*40)
nasc = int(input('Em que ano você nasceu? '))
voto(idade)
print('-'*40)