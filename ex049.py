num = str(input('Digite um número para saber sua tabuada:')).strip().upper()
num = int(num)
print(5 * '=<>=')
for c in range(1, 11):
    print(f'{num} x {c:2} = {num*c}')
print(5 * '=<>=')