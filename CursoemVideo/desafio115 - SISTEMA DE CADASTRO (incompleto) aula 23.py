from úteis import cores, strings
import json
pessoa = {}
lista = []
while True:
      strings.linhapadrão('MENU PRINCIPAL')
      print(f'{cores.cor[3]}1 - {cores.cor[4]}Ver pessoas cadastradas\n'
            f'{cores.cor[3]}2 - {cores.cor[4]}Cadastrar nova pessoa \n'
            f'{cores.cor[3]}3 - {cores.cor[4]}Sair do Sistema{cores.cor[0]}')
      print('-'*30)
      resp = int(input(f'{cores.cor[3]}Sua opção:{cores.cor[0]} '))
      print('-'*30)
      if resp == 1:
            strings.linhapadrão('PESSOAS CADASTRADAS')
            for k,v in enumerate(lista):
                  for valor in v.values():
                        print(f'{valor:<15}', end ='')
                  print()
            with open('lista.json', 'r') as file:
                  lista = json.load(file)
                  for i in pessoa.values():
                        print(f'{i}   ', end='  ')
                  print()
      elif resp == 2:
           strings.linhapadrão('NOVO CADASTRO')
           while True:
                 pessoa.clear()
                 try:
                       pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
                       pessoa['idade'] = int(input('Idade: '))
                 except (ValueError, TypeError):
                       print(f'{cores.cor[1]}ERRO! O valor que você digitou não é valido. Tente novamente.{cores.cor[0]}')
                       continue
                 else:
                       print('Pessoa cadastrada com sucesso!')
                       break
           with open('lista.json', 'w') as file:
                 json.dump(lista, file)
           lista.append(pessoa.copy())
      elif resp == 3:
            print('VOLTE SEMPRE')
            break
      else:
            print(f'{cores.cor[1]}ERRO! Por favor, digite uma opção válida do menu.{cores.cor[0]}')