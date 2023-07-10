homens = 0
maior18 = 0
menor20 = 0
while True:
    print(10 * '--')
    print(5 * ' ','CADASTRO')
    print(10 * '--')
    idade = 0
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]:')).strip().upper()
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N]:')).strip().upper()

    if sexo == 'M':
        homens += 1
    if idade >= 18:
        maior18 += 1
    if sexo == 'F' and idade <= 20:
        menor20 += 1
    if escolha == 'N':
        break

print(f'Total de pessoas com mais de 18 anos {maior18}')
print(f'No total temos {homens} homens cadastrado')
print(f'E temos {menor20} mulheres com menos de 20 anos')