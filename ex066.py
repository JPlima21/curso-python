soma = 0
cont = 0
while True:
    num = int(input('Digite um número (999 para PARAR): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Você digitou {cont} números e a soma deles é igual a {soma}')