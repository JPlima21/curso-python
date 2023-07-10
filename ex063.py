print(10 * '=<>=')
print(7 * ' ', 'Sequecia de Fibonacci')
print(10 * '=<>=')
num = int(input('quantor termos você quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end= '')
cont = 3
while cont <= num:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
