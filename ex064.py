num = int(input('Digite um numero [999 pra PARAR o código]: '))
cont = soma = 0
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um numero [999 pra PARAR o código]: '))
print(f'você digitou {cont} números e a soma entre eles é igual a {soma}')