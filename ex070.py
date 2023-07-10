print('--' * 10)
print(' ' * 4, 'LOJA DO JP')
print('--' * 10)
total = 0
totmil = 0

while True:
    produto = str(input('Digite o nome do produto:')).strip()
    preço = float(input('Preço R$:'))
    total += preço
    if preço > 1000:
        totmil += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    if resposta == 'N':
        break
print('{:-^40}'.format('FIM DO PROCESSO'))
print(f'O total da compra foi {total} ')
print(f'Temos {totmil} produtos acima de mil reais')
