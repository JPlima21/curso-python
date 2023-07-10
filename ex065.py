media = cont = soma = maior = menor = 0
resp = 'S'
while resp in 'S':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar [S/N]?')).strip().upper()[0]

media += soma / cont
print(f'você digitou {cont} números ae a média entre eles é igual a {media}')
print(f'O maior número é {maior} e o menor número é {menor}')