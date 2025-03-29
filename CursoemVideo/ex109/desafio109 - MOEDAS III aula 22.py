from exercícios.ex109 import moedas
p=float(input('Digite o preço: R$ '))
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p,True)}.')
print(f'O dobro de {moedas.moeda(p)} é {moedas.dobro(p,True)}.')
print(f'Aumentando 15%, temos {moedas.aumentar(p,15,True)}.')
print(f'Reduzindo 13%, temos {moedas.diminuir(p,13,True)}.')