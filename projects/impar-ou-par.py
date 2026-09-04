# Esse numero e impar ou par???

from time import sleep
numero = int(input('Digite um numero: '))
n = numero % 2
print('PROCESSANDO...')
sleep(2)
if n == 0:
    print('O numero {} e PAR' .format(numero))
else:
    print('O numero {} e IMPAR' .format(numero))