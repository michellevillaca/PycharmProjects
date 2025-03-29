print('-=-'*8, 'PROGRESSÃO ARITMÉTICA', '-=-'*8)
primeiro = int(input('Primeiro termo da PA: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais !=0:
    total += mais
    while cont <= total:
        print(termo, end=' -> ')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão aritmética com {} termos mostrados.'.format(total))