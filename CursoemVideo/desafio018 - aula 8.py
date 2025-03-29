import math
ang=float(input('Digite um ângulo: '))
sen=math.sin(math.radians(ang))
cos=math.cos(math.radians(ang))
tan=math.tan(math.radians(ang))
print('De acordo com o ângulo digitado, temos:\n*sen: {:.2f}\n*cos: {:.2f}\n*tan: {:.2f}'.format(sen,cos,tan))