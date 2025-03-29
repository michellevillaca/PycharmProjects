def maior(*núm):
    maiorvalor = 0
    for valor in núm:
        if valor > maiorvalor:
            maiorvalor = valor
    print('-='*30)
    print('Analisando os valores passados...')
    print(f'{núm} => Foram informados {len(núm)} valores ao todo.')
    print(f'O maior valor foi {maiorvalor}.')
#Programa Principal
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()