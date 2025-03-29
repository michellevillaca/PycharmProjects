import math
co=float(input('Digite o comprimento do cateto oposto do triângulo retângulo: '))
ca=float(input('Digite o comprimento do cateto adjacente do triângulo retângulo: '))
hi=math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))