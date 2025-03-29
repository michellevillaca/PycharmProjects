def notas(*num,sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    resp = {}
    resp['total'] = len(num)
    resp['maior'] = max(num)
    resp['menor'] = min(num)
    resp['média'] = sum(num)/len(num)
    if sit:
        if resp['média'] >= 7:
            resp['situação'] = 'BOA'
        elif 6 <= resp['média'] < 7:
            resp['situação'] = 'RAZOÁVEL'
        else:
            resp['situação'] = 'RUIM'
    return resp

#Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
resp = notas(7,5,4,9,1,sit=True)
print(resp)
resp = notas(7,9,8.5,10,6.5,sit=True)
print(resp)
help(notas)