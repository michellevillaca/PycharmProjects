times = ('Botafogo','Palmeiras','Fortaleza',
         'Flamengo','São Paulo','Internacional',
         'Bahia','Cruzeiro','Atlético-MG',
         'Vasco da Gama','Grêmio','Criciúma',
         'Bragantino','Juventude','Athletico-PR',
         'Fluminense','EC Vitória','Corinthians',
         'Cuiabá','Atlético-GO')
print('-'*7,'LISTA DE TIMES DO BRASILEIRÃO','-'*7,'\n',times,'\n')
print('-'*7,'Os 5 primeiros são:','-'*7,'\n',times[0:5],'\n')
print('-'*7,'Os 4 últimos são:','-'*7,'\n',times[-4:],'\n')
print('-'*7,'Times em ordem alfabética','-'*7,'\n',sorted(times),'\n')
if 'Chapecoense' in times:
    print('-' * 20, f'\nO Chapecoense está na {times.index('Chapecoense') + 1}ª posição.')
else:
    print('-'*20,'\nO Chapecoense não está nos 20 primeiros times da Tabela.')
#print('-'*20,f'\nO São Paulo está na {times.index('São Paulo')+1}ª posição.')