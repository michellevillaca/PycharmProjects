números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('\033[32mValor adicionado com sucesso!\033[m')
    else:
        print('\033[31mValor duplicado; não será adicionado.\033[m')
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r not in 'SN':
        r = str(input('Opção inválida. Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print('-='*30)
números.sort()
print(f'Você digitou os valores {números}.')