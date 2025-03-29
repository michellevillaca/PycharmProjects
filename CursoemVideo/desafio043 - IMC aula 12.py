peso=float(input('Peso (kg): '))
altura=float(input('Altura (m): '))
IMC=peso/(altura**2)
print('De acordo com o seu peso ({}kg) e a sua altura ({}m), o seu IMC é: {:.2f}.'.format(peso,altura,IMC))
if IMC < 18.5:
    print('\033[1;34mVocê está abaixo do peso.')
elif 18.5 < IMC < 25:
    print('\033[1;32mSeu peso está ideal.')
elif 25 < IMC < 30:
    print('\033[1;33mVocê está com sobrepeso.')
elif 30 < IMC < 40:
    print('\033[1;31mATENÇÃO! Você está com obesidade.')
else:
    print('\033[1;31mATENÇÃO! Você está com obesidade mórbida.')