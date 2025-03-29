m=float(input('Digite uma distância em metros: '))
km=m*0.001
hm=m*0.01
dam=m*0.1
dm=m*10
cm=m*100
mm=m*1000
print('{} metros equivalem a {} centímetros e {} milímetros.'.format(m,cm,mm))
print('A medida de {}m corresponde a:\n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(m,km,hm,dam,dm,cm,mm))