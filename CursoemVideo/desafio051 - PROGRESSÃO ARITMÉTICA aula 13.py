print('='*10,'10 TERMOS DE UMA PA','='*10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10-1) * razão
for c in range (primeiro,décimo+razão, razão):
    print('{}'.format(c), end=' -> ')
print('FIM')