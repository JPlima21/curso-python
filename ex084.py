dados = []
pessoas = []
maiorp = menorp = 0
while True:
    dados.append(str(input('Nome: ')).strip())
    dados.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        maiorp = menorp = dados[1]
    else:
        if dados[1] > maiorp:
            maiorp = dados[1]
        if dados[1] < menorp:
            menorp = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N]:')).strip()
    if resp not in 'SsNn':
        resp =  str(input('resposta invalida...\nQuer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=-' * 15)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maiorp}Kg')
for v in pessoas:
    if v[1] == maiorp:
        print(f'{v}', end=' ')
print()
print(f'o menor peso foi de {menorp}Kg')
for v in pessoas:
    if v[1] == menorp:
        print(f'{v}', end=' ')
print()