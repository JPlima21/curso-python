from random import randint
from time import sleep
bot = randint(0, 10)
acertou = False
palpite = 0
print('Olá meu nome é Bismuto \(^◡^)')
sleep(1)
resp = str(input('vamos jogar um jogo de adivinhação?')).strip().upper()[0]
if resp == 'N':
    print('ah, ok então, vamos deixar para a proxima :(')
if resp == 'S':
    print('Que legal (^◡^), então bora lá')
    sleep(1)
    print('Vou pensar em um número de 0 a 10\ntente adivinhar em qual número eu pensei')
    while not acertou:
        escolha = str(input('Qual o seu palpite?'))
        escolha = int(escolha)
        palpite += 1
        if escolha == bot:
            acertou = True
        else:
            if escolha < bot:
                print('Mais... Qual seu palpite?')
            elif escolha > bot:
                print('Menos... Qual o seu palpite?')
    print(f'Você acertou com {palpite} palpites, Parabéns!')
