from time import sleep
def contador(i,f,p):
    sleep(0.5)
    print('-='*15)
    sleep(0.5)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(2.0)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont } ',end='')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ',end='')
            sleep(0.5)
            cont -= p
        print('FIM!')
#Programa Principal
contador(1,10,1)
contador(10,0,2)
print('-='*20)
print('Agora é a sua vez de personalizar a contagem!')
início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(início,fim,passo)