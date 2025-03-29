num=int(input('Digite um número inteiro: '))
escolha=(int(input('Escolha a base de conversão, sendo:\n [1] para binário\n [2] para octal\n [3] para hexadecimal\nSua opção: ')))
if escolha == 1:
    print('A conversão do seu número para binário é {}.'.format(bin(num)[2:]))
elif escolha == 2:
    print('A conversão do seu número para octal é {}.'.format(oct(num)[2:]))
elif escolha == 3:
    print('A conversão do seu número para hexadecimal é {}.'.format(hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')