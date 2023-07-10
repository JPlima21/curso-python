listanum = []
listapar = []
listaimpar = []

while True:
    listanum.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N]: ')).strip()
    if resp not in 'SsNn':
        resp = str(input('Por favor digite novamente...\nQuer acontinuar? [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(listanum):
    if v % 2 == 0:
        listapar.append(v)
    elif v % 2 == 1:
        listaimpar.append(v)

print(f'Lista completa é {listanum}')
print(f'lista de pares é {listapar}')
print(f'Lista de ímpares é {listaimpar}')