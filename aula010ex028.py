# EXERCÍCIO28 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 
# e peça para o usuário descobri qual número foi escolhido pelo computador. O programa deverá escrever
# na tela se o usuário venceu ou perdeu

from random import randint
computador = randint(0, 5) #faz o computador pensar 

print(10 * '==')
print('Vou pensar em um número de 0 a 5. Tente adivinha')
print(10 * '==') 
num = int(input('Em que número eu pensei? ')) #jogador tenta adivinha  

if num==computador:
    print('CARAMBA! Você conseguiu adivinha. Não vou perder da próxima vez')

else:
    print('GANHEI! eu pensei no número {} e não no {}'.format(computador, num))