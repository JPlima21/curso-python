from random import randint
vitoria = 0
while True:
    bot = randint(1, 11)
    player = int(input('Digite um número: '))
    total = player + bot
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar? [P\I]')).strip().upper()[0]
    print(f'Você escolheu {player} e o computador {bot}. soma total de {total} ')
    if escolha == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você perdeu')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente')
print(f'GAME OVER, Você teve um total de {vitoria} vitorias')