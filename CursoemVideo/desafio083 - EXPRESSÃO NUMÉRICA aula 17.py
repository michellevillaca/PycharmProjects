print('~'*5,'VALIDADOR DE EXPRESSÕES MATEMÁTICAS','~'*5)
expr = str(input('Digite a expressão: '))
pilha = [] #a expressão também é uma lista de símbolos e códigos. Então, para cada símbolo na expressão, eu vou criar um if:
for símbolo in expr:
    if símbolo == '(': #se o símbolo for um parêntese abrindo, eu o coloco na pilha
        pilha.append('(')
    elif símbolo == ')': #aqui eu tenho duas possibilidades, ou a minha lista está vazia, ou ela está cheia.
        if len(pilha) > 0: #se o tamanho da minha pilha for maior que zero, significa que ela não está vazia, isto é, tem um parêntese em aberto.
            pilha.pop() #comando 'apagar' para remover o parêntese aberto, isso significa que "deu match", o parêntese fechando encontrou seu par de parêntese abrindo, e podemos removê-lo da pilha.
        else:
            pilha.append(')') #se não tiver parêntese nenhum, ou seja, se a pilha está vazia, ele manda acrescentar o parêntese fechando, para podermos saber que ele não encontrou seu par.
            break
if len(pilha) == 0: #se a pilha estiver sem nenhum elemento, significa que todos os parênteses que se fecharam tinham seu par correspondente.
    print('\033[32mSua expressão está válida!\033[m')
else: #aqui significa que ou não teve algum parêntese para fechar, e existe um ou mais em aberto que não foi apagado na lista, ou então existe um parêntese de fechar a mais porque não tinha um aberto para ser apagado.
    print('\033[31mSua expressão está errada!\033[m')