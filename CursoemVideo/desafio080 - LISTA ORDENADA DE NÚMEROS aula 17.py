lista = []
for c in range(0,5): #c = contador
    n = (int(input('Digite um valor: ')))
    if c == 0 or n> lista[-1]: #se o número for maior do que o último elemento da minha lista (que é o maior até então).
        lista.append(n)
        print('Adicionado ao final da lista.')
    else:
        posição = 0
        while posição < len(lista): #enquanto a posição for menor que o comprimento da lista (indo da posição zero até o fim da lista).
            if n <= lista[posição]:
                lista.insert(posição, n)
                print(f'Adicionado na posição {posição} da lista.')
                break
            posição +=1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}.')