soma = 0
cont = 0
for c in range(1, 7):
   num = int(input('Digite um número aléatorio:'))
   if num % 2 == 0:
       cont += 1
       soma += num
print(f'Você informou {cont} números pares e a soma de todos eles é {soma}')
