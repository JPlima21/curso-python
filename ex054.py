from datetime import date
atua = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input(f'Digite o ano em que a {c}º pessoa nasceu:'))
    idade = atua - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'No total tivemos {maior} maiores de idade e {menor} menores')


