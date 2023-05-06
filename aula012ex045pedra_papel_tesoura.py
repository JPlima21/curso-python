from time import sleep
from random import randint 
#escolha do bot
itens = ('Pedra', 'Papel', 'Tesoura')
bot = randint(0, 2)

print('Vamos jogar PEDRA, PAPEL, TESOURA?')
sleep(3)
#escolha do jogador
 
print('escola uma dessas opções: ')
print('[ 0 ] Pedra \n[ 1 ] Papel \n[ 2 ] Tesoura')
jogador = int(input('Qual a sua jogada? '))

sleep(1)
print('JO')
sleep(1)
print('KEN!')
sleep(1)
print('PÓ!!!')

print('=÷=' * 10)
print('computador jogou: {}'.format(itens[bot]))
print('jogador jogou: {}'.format(itens[jogador]))
print('=÷=' * 10)

if bot == 0: #computador escolheu Pedra 
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador WIN')
    elif jogador == 2:
        print('computador WIN')
    else:
        print('JOGADA INVÁLIDA')

elif bot == 1: #computador escolheu Papel 
     if jogador == 0:
         print('computador WIN')
     elif jogador == 1:
         print('EMPATE')
     elif jogador == 2:
         print('Jogador WIN')
     else:
         print('JOGADA INVÁLIDA')

elif bot == 2: #computador escolheu Tesoura 
    if jogador == 0:
        print('Jogador WIN')
    elif jogador == 1:
        print('computador WIN')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')