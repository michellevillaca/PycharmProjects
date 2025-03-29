lanche = 'Hambúrguer','Suco','Pizza','Pudim'
print(lanche[3])
print(lanche[0])
print(lanche[-4])
print(lanche[1:3])
print(lanche[2:])
for comida in lanche:
    print(f'Eu vou comer {comida}')
for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}.')

animais = 'porco', 'vaca', 'cachorro', 'gato', 'urso', 'galinha', 'cavalo', 'elefante', 'zebra', 'girafa'
print(f'Eu tenho um {animais[2]}, mas eu não tenho um {animais[3]}.')
for bichos in animais:
    print(f'Na minha fazenda tem um(a) {bichos}, ia-ia-ô')
print(f'Na minha fazenda tem {len(animais)} animais.')
print(sorted(animais))
print(animais.index('cavalo'))