#resolvido de uma maneira mais facil
from math import factorial
num = int(input('Digite um número para saber seu fatorial: '))
c = num
f = factorial(num)
print(f'Caulando {num}! = ', end='')
for c in range(num, 0, -1):
    print(f'{c}', end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
print(f'{f}', end='')

#resolvido da maneira que o exercicio pediu

