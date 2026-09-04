n = int(input('Digite um numero: '))
for i in range(1,11): # essa parte diz "repita o bloco de codigo 10 vezes, com i variando de 1 a 10"
    resultado = n * i # multiplicando o numero digitado pelo valor de i
    print(f'{n} x {i} = {resultado}') # essa parte mostra o resultado da multiplicação no formato "n x i = resultado"

#forma pratica melhor que usar varios print, usando f-string