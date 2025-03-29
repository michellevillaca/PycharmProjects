co=float(input('Digite o comprimento do cateto oposto do triângulo retângulo: '))
ca=float(input('Digite o comprimento do cateto adjacente do triângulo retângulo: '))
h=(co**2 + ca**2)**(1/2)
print('Sendo o comprimento do cateto oposto {}cm e do cateto adjacente {}cm, o comprimento da hipotenusa é {:.2f}cm'.format(co,ca,h))