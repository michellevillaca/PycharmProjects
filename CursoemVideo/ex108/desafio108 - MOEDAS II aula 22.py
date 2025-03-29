from exercícios.ex108 import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}.')
print(f'Aumentando 20%, temos {moeda.moeda(moeda.aumentar(p, 20))}.')
print(f'Reduzindo 35%, temos {moeda.moeda(moeda.diminuir(p, 35))}.')