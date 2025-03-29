import emoji
vel=float(input('A quantos km/h você estava? '))
#multa aplicada de R$ 7,00 a cada km acima do limite
multa=(vel-80)*7
if vel>80:
    print(emoji.emojize('\033[1;31mMULTADO! :police_car_light: Você excedeu o limite de 80 km/h. Sua multa é de R$ {}.'.format(multa)))
else:
    print(emoji.emojize('\033[1;32mVocê não ultrapassou o limite de velocidade. Dirija com segurança e tenha um bom dia! :green_circle:'))