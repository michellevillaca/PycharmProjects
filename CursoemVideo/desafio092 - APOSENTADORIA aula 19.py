from datetime import date
pessoa = {'nome': str(input('Nome: '))}
nascimento = int(input('Ano de Nascimento: '))
pessoa['idade'] = date.today().year - nascimento
pessoa['ctps'] = int(input('Carteira de trabalho (0) não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = (pessoa['contratação']+35)-nascimento
print('-='*30)
print(pessoa)
for k,v in pessoa.items():
    print(f'\033[33m{k}\033[m tem valor \033[32m{v}\033[m')