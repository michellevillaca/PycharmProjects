preço=float(input('\033[4mPreço do produto:\033[m R$ '))
pagamento=int(input('\033[4mQual será a forma de pagamento?\033[m\n \033[42m[1]\033[m À vista em dinheiro/PIX (10% de desconto)\n \033[42m[2]\033[m À vista no cartão (5% de desconto)\n \033[42m[3]\033[m Parcelado em 2x no cartão\n \033[42m[4]\033[m Parcelado em 3x ou mais no cartão (20% de juros)\n\033[4mDigite sua opção:\033[m '))
if pagamento == 1:
    total=preço-(preço*10/100)
    print('Seleção de pagamento \033[32mà vista em dinheiro/PIX (10% de desconto)\033[m:\ntotal de \033[31mR${:.2f}\033[m por \033[32mR${:.2f}\033[m.'.format(preço,total))
elif pagamento == 2:
    total=preço-(preço*5/100)
    print('Seleção de pagamento \033[32mà vista no cartão (5% de desconto)\033[m:\ntotal de \033[31mR${:.2f}\033[m por \033[32mR${:.2f}\033[m.'.format(preço,total))
elif pagamento == 3:
    parcela=preço/2
    print('Seleção de pagamento em \033[33m2x no cartão (sem desconto)\033[m:\n\033[32m2x de R$ {:.2f}\033[m, total de \033[32mR${:.2f}\033[m.'.format(parcela,preço))
elif pagamento == 4:
    parcela=int(input('\033[4mEm quantas vezes vai parcelar?\033[m '))
    total=preço+(preço*20/100)
    preçoparcela=total/parcela
    print('Seleção de pagamento em \033[31m3x ou mais no cartão (20% de juros)\033[m:\ntotal de \033[32mR${:.2f}\033[m por \033[33mR${:.2f}\033[m.'.format(preço,total))
    print('Pagamento feito em \033[31m{} vezes\033[m de \033[33mR${:.2f}\033[m.'.format(parcela,preçoparcela))
else:
    print('Opção inválida. Tente novamente.')