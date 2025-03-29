print('\033[1;33m-=-'*8,'10 TERMOS DE UMA PA','-=-'*8,'\033[m')
primeirotermo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão: '))
termo = 1
print('\033[35m',primeirotermo, end = ' -> ')
while termo <= 9:
    termo += 1
    primeirotermo += razão
    print(primeirotermo, end = ' -> ')
print('\033[31mFIM')