print('\033[1;35m.'*10,'TABUADAS','.'*10,'\033[m')
while True:
    print('\033[1;33m-'*40)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*40,'\033[m')
    if n < 0:
        break
    for c in range (1,11):
        print(f'{n} x {c} = \033[1;32m{n*c}\033[m')
print('Programa encerrado.')