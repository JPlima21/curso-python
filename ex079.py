listanum = []
while True:
    print('-=-' * 10)
    num = int(input('Digite um valor: '))
    if num not in listanum:
        listanum.append(num)
        print('Valor adicionado a lista com sucesso...')
    else:
        print('Valor já digitado! Não irei adcionar a lista...')
    resp = str(input('Quer continuar? [S/N]')).strip()
    if resp in 'Nn':
        break
print('<|>' * 10)
listanum.sort()
print(f'Você digitou os valores {listanum}')
