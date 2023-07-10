maior = 0
menor = 0
for r in range(1, 6):
    peso = float(input(f'digite o {r}º peso:'))
    if r == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi {maior}Kg\nO menor peso lido foi {menor}Kg')
