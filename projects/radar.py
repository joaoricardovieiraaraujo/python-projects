# Radar eletronico em python simulador
print('====' * 15)
print('SEJA BEM VINDO AO RADAR ELETRONICO EM PYTHON!')
print('====' * 15)
vl = int(input('Digite a velocidade do carro: '))
m = (vl - 80) * 7
if vl > 80:
    print('MULTADO!!! VOCÊ ULTRAPASSOU O LIMITE DE VELOCIDADE DE 80KM/H VOCÊ LEVOU UMA MULTA DE R${:.2f}' .format(m))
else:
    print('VOCÊ ESTA DENTRO DO LIMITE DE VELOCIDADE, TENHA UM BOM DIA! E DIRIJA COM SEGURANÇA!')
