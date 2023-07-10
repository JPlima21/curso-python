num = str(input('DIgite um número:')).strip()
num = int(num)
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[31m', end='')
        total += 1
    else:
        print('\033[34m', end='')
    print(f'{c}', end=' ')
print(f'\n\033[mnúmero {num} foi dividido {total} vezes')
if total == 2:
    print(f'\033[32m{num} é um número primo, pois ele é divisivel somente por 2 números')
else:
    print(f'\033[31m{num} NÃO é um número primo')
    
