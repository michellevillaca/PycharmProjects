maior = 0
menor = 0
for pessoa in range (1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(pessoa)))
    if pessoa == 1: #se eu li somente a informação de 1 pessoa até agora, então automaticamente ela é tanto a maior quanto a menor ocorrência; por isso classifico como a leitura do peso da primeira pessoa como maior e também como menor:
        maior = peso
        menor = peso
    else:
        if peso > maior: #se o peso que eu acabei de ler for maior que o maior peso (ou seja, maior que o da primeira pessoa)
            maior = peso #então o maior peso passa a ser o número que eu acabei de ler.
        if peso < menor:
            menor = peso #mesma lógica para o menor peso
print('O maior peso lido foi de {}kg.'.format(maior))
print('O menor peso lido foi de {}kg.'.format(menor))