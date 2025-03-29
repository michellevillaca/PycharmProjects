print('-=-'*20,'\n',' '*15, 'ANALISADOR DE TRIÂNGULOS 2.0\n', '-=-'*20)
r1=float(input('Primeiro segmento: '))
r2=float(input('Segundo segmento: '))
r3=float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Os três segmentos formam um triângulo EQUILÁTERO: todos os lados iguais.')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('Os três segmentos formam um triângulo ISÓCELES: dois lados iguais.')
    elif r1 != r2 != r3:
        print('Os três segmentos formam um triângulo ESCALENO: todos os lados diferentes.')
else:
    print('Os três segmentos não podem formar um triângulo.')