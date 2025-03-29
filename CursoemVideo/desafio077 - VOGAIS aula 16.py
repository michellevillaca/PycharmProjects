palavras = ('aprender','programar','linguagem','python',
            'curso','gratis','estudar','praticar','trabalhar',
            'mercado','programador','futuro')
for vocábulos in palavras:
    print(f'\nNa palavra {vocábulos.upper()}, temos: ', end = '')
    for letras in vocábulos: #a própria palavra é uma lista - uma lista de letras
        if letras in 'aeiou':
            print(letras, end = ' ')