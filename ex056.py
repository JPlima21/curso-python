#variaveis
mediaidade = 0
somaidade = 0
maioridadehomem = 0
nomevelho = 0
menoridademulher = 0

#repetição
for c in range(1, 5):
    print(5 * '-', f'{c}º pessoa', 5 * '-' )
    nome = str(input('Nome:')).strip()
    idade = str(input('Idade:')).strip()
    idade = int(idade)
    sexo = str(input('Sexo F/M:')).strip().upper()
    somaidade += idade

#identificando o nome do homem mais velho
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

#idenficando quantas mulheres possui menos de 20 anos
    if idade <= 20 and sexo in 'Ff':
        menoridademulher += 1

mediaidade += somaidade / 4
print(f'A média de idade do grupo é {mediaidade}')
print(f'O homem mais velho possui {maioridadehomem}anos e se chama {nomevelho}')
print(f'Existe {menoridademulher} mulher que possui a idade menor que 20 anos ')