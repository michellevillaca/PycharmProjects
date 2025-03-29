#fatorial usando o WHILE
n = int(input('Digite um número: ')) #pedimos um número inteiro ao usuário, e armazenamos na variável "n"
resultado = 1 #precisamos calcular o produto; vamos armazenar esse produto na variável "resultado", mas a princípio, iniciamos a variável com o resultado 1
count = 1 #precisamos de um contador, para ir de 1 até "n", e a cada interação do laço WHILE, ela é incrementada
#dentro do laço while, fazemos com que "resultado" seja multiplicado por "count", pois "count" vai assumir os valores de 1, 2, 3, ..., até "n". Quando chegar em "n", o looping deve parar. Logo, o condicional de while deve ser: count <= n
while count <= n:
    resultado *= count #--> resultado = resultado * count; ou seja, o novo valor de "resultado" vai ser o valor antigo multiplicado por "count".
    count += 1 #--> count = count + 1; ou seja, estamos incrementando o valor de count em uma unidade a cada interação do laço.
print('O resultado de {}! é igual a {}.'.format(n,resultado))
print(' ')

#fatorial usando FOR
n = int(input('Digite um número: '))
resultado = 1
for n in range (1,n+1):
    resultado *= n
print('O resultado de {}! é igual a {}.'.format(n,resultado))