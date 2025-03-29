import random
print('~'*10,'JOKENPÔ','~'*10)
lista=['PEDRA','PAPEL','TESOURA']
user=str(input('Escolha PEDRA, PAPEL ou TESOURA: ')).upper()
computer=random.choice(lista)
print('Eu escolhi {}'.format(computer))
if user == 'pedra'.upper() and computer == 'PAPEL' or user == 'papel'.upper() and computer == 'TESOURA' or user == 'tesoura'.upper() and computer == 'PEDRA':
    print('OPS, VOCÊ PERDEU!')
elif user == 'papel'.upper() and computer == 'PEDRA' or user == 'tesoura'.upper() and computer == 'PAPEL' or user == 'pedra'.upper() and computer == 'TESOURA':
    print('VOCÊ VENCEU!')
elif user == 'pedra'.upper() and computer == 'PEDRA' or user == 'papel'.upper() and computer == 'PAPEL' or user == 'tesoura'.upper() and computer == 'TESOURA':
    print('EMPATAMOS!')