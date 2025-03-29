km=float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de \033[1;34m{}km\033[m.'.format(km))
if km <= 200:
    print('A sua viagem vai custar \033[32mR${:.2f}\033[m.'.format(km*0.50))
else:
    print('A sua viagem vai custar \033[32mR${:.2f}\033[m.'.format(km*0.45))
#preço de R$0,50 por km para viagens de até 200 km e R$0,45 para viagens mais longas.