print('~'*20, 'Analisador de Triângulos','~'*20)
r1=float(input('Primeiro segmento (cm): '))
r2=float(input('Segundo segmento (cm): '))
r3=float(input('Terceiro segmento (cm): '))
#para que três segmentos formem um triângulo, é preciso que a soma de dois lados seja sempre menor que o terceiro lado.
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Segundo os valores que você me deu, os três segmentos \033[0;32mPODEM\033[m formar um triângulo.')
else:
    print('Segundo os valores que você me deu, os três segmentos \033[0;31mNÃO PODEM\033[m formar um triângulo.')