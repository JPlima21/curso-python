print(10*'=<>=')
print(7 * ' ', '10 TERMOS DE UMA PA')
print(10*'=<>=')
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
décimo = primeiro + (10 - 1) * razao

for c in range(primeiro, décimo + razao, razao):
    print(c)