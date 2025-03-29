import random
import emoji
from time import sleep
num = random.randint(0,5) #faz o computador "pensar"
print('-=-'*20)
print('Vou sortear um número de 0 a 5. Tente adivinhar qual número será.')
print('-=-'*20)
user = int(input('Digite o seu palpite: ')) #jogador tenta adivinhar
print('\033[7mPROCESSANDO...\033[m')
sleep(3)
print('O número que eu sorteei foi: \033[34m{}\033[m'.format(num))
if user == num:
    print(emoji.emojize('\033[32mParabéns! Você acertou! :red_heart:'))
else:
    print(emoji.emojize('\033[33mQue pena! Você não acertou. Tente de novo na próxima :winking_face:'))