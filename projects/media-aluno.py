print('==='*20)
print('CALCULANDO A MÉDIA DE UM ALUNO DE 4 BIMESTRES')
print('==='*20)
n1 = float(input('Nota do 1 bimestre: '))
n2 = float(input('Nota do 2 bimestre: '))
n3 = float(input('Nota do 3 bimestre: '))
n4 = float(input('Nota do 4 bimestre: '))
m = (n1 + n2 + n3 + n4) / 4
if m >= 5:
    print(f'Sua media foi {m:.1f}!! PARÁBENS VOCÊ FOI APROVADO!!')
else:
    print(f'Sua media foi {m:.1f}!! INFELIZMENTE VOCÊ FOI REPROVADO!! ESTUDE MAIS E TENTE NOVAMENTE!!')
print('Como dizia o filosofo Aristóteles: "A educação é a melhor provisão para a velhice."')