from random import radiant
from time import sleep

print('==='*20)
print('TENTE ACERTAR O NÚMERO QUE ESTOU PENSANDO')
print('==='*20)
j = int(input('Digite um numero de 0 a 5: '))
m = radiant(0,5)
print('A MAQUINA ESTA PENSANDO...')
sleep(2)
if j == m:
    print('PARÁBENS VOCÊ ACERTOU O NÚMERO QUE EU ESTAVA PENSANDO!!')
else:
    print('QUE PENA VOCÊ ERROU!! O NÚMERO QUE EU ESTAVA PENSANDO ERA {}!!' .format(m))