import random
from time import sleep
num = random.randint(0, 10)
user = 1
totaltentativas = 0
print('-'*20)
print('JOGO DA ADIVINHAÇÃO')
print('-'*20)
while num != user:
    print('Vou sortear um número de 0 a 10. Tente adivinhar qual será o número.')
    user = int(input('Qual é o seu palpite? '))
    print('PROCESSANDO...')
    sleep(0.75)
    num = random.randint(0, 10)
    print('\033[1mO número que eu sorteei foi \033[1;31m{}\033[m. \033[1mTente novamente!\033[m'.format(num))
    totaltentativas += 1
    print(' ')
print('Parabéns! Você conseguiu! Foram necessárias {} tentativas para você adivinhar o número sorteado.'.format(totaltentativas))