# Jogo ppt = pedra, papel e tesoura

from random import choice
from time import sleep
opcoes = ['pedra', 'papel', 'tesoura']
jogador = input('Escolha pedra, papel ou tesoura: ').lower()
computador = choice(opcoes)
if jogador not in opcoes: 
    print('Jogada irregular! Tente novamente!!!')
print('VOCÊ JOGOU {}' .format(jogador))
print('PROCESSANDO...')
sleep(2)
print('A MAQUINA JOGOU {}' .format(computador))
print('PROCESSANDO...')
sleep(2)
if computador == jogador:
    print('EMPATE!!!')
else:
    if jogador == 'pedra' and computador == 'tesoura' or \
    jogador == 'papel' and computador == 'pedra' or \
    jogador == 'tesoura' and computador == 'papel':
        print('PARÁBENS!!! VOCÊ VENCEU A MAQUINA!!!')
    else:
        print('VOCÊ PERDEU!!! A MAQUINA VENCEU!!!')