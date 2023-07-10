listanum = [[], []]
for c in range(1, 8):
    valor = (int(input(f'Digite o {c}º valor: ')))
    if valor % 2 == 0:
        listanum[0].append(valor)
    else:
        listanum[1].append(valor)
listanum[0].sort()
print(f'Valores apres digitados {listanum[0]}')
listanum[1].sort()
print(f'Valores impares digitados {listanum[1]}')