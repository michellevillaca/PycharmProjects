from time import sleep
def maior(*núm):
    maiorvalor = 0
    sleep(0.5)
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in núm:
        sleep(0.5)
        print(f'{valor}, ', end='')
    sleep(0.5)
    print(f'Foram informados {len(núm)} valores ao todo.')
    for valor in núm:
        if valor > maiorvalor:
            maiorvalor = valor
    sleep(0.5)
    print(f'O maior valor foi {maiorvalor}.')
#Programa Principal
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()