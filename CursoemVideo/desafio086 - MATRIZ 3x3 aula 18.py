matriz = []
i1 = i2 = 0
for v in range(0,9):
    matriz.append(int(input(f'Digite um valor para {i1,i2}: ')))
    if i2 < 3:
        i2 += 1
        if i2 == 3:
            i2 = 0
            i1 += 1
print('-='*30)
print(f'[ {matriz[0]} ] [ {matriz[1]} ] [ {matriz[2]} ]\n'
      f'[ {matriz[3]} ] [ {matriz[4]} ] [ {matriz[5]} ]\n'
      f'[ {matriz[6]} ] [ {matriz[7]} ] [ {matriz[8]} ]')