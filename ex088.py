from random import randint
from time import sleep
print('-=' * 15)
print(f'      JOGOS DA MEGASENA')
print('-=' * 15)
quant = int(input('Quantos jogos você quer que eu sorteie?'))
lista = []
jogos = []
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'-=' * 3, f'Sorteando {quant}', '=-' * 3)
for i, l in enumerate(jogos):
    sleep(1)
    print(f'jogo {i + 1}: {l}')

