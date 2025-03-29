s = 0 #acumulador
cont = 0 #contador
for c in range (1,501, 2): #coloca-se o 2 para "pular" um número, deixando somente os números ímpares nesse caso, pois a contagem começa do 1
    if c%3 == 0:
        cont = cont + 1 #o contador serve para contar quantos números eu achei.
        s = s+c #faço com que a soma receba o que ela tem (0) mais um número (estou acumulando um número)
print('A soma dos {} números, que são todos os números ímpares múltiplos de três encontrados no intervalo de 1 a 500, foi {}.'.format(cont,s))