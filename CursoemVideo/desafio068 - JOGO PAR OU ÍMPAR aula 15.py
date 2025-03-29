from random import randint
print('-=-'*17)
print(' '*10, 'VAMOS JOGAR PAR OU ÍMPAR')
print('-=-'*17)
c = 0
while True:
    n = int(input('Digite um valor: '))
    user = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    pc = randint(0,11)
    s = n + pc
    x = ' '
    while user not in 'PI':
        user = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    if s%2 == 0:
        x = 'PAR'
        if user in 'Pp':
            print(f'Você jogou {n} e o computador jogou {pc}. Total de {s}, portanto, {x}.')
            print('VOCÊ VENCEU!')
            c += 1
        else:
            print(f'Você jogou {n} e o computador jogou {pc}. Total de {s}, portanto, {x}.')
            print('VOCÊ PERDEU!')
            break
    else:
        x = 'ÍMPAR'
        if user in 'Ii':
            print(f'Você jogou {n} e o computador jogou {pc}. Total de {s}, portanto, {x}.')
            print('VOCÊ VENCEU!')
            c += 1
        else:
            print(f'Você jogou {n} e o computador jogou {pc}. Total de {s}, portanto, {x}.')
            print('VOCÊ PERDEU!')
            break
print(f'GAME OVER! Você venceu {c} vezes.')