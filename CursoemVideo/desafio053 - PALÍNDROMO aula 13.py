frase=str(input('Escreva uma frase: ')).strip().upper() #strip tira os espaços desnecessários
palavras=frase.split() #passo 1: separar as palavras da frase
junto=''.join(palavras) #passo 2: juntá-las novamente (sem espaços)
#com os dois comandos acima eu eliminei os espaços internos
inverso = junto [::-1] #fatiei do início ao fim, contando de trás para frente (-1)
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')