ficha = dict()
ficha['nome'] = str(input('Nome: '))
ficha['média'] = float(input(f'Média de {ficha["nome"]}: '))
print(f'Nome do aluno: {ficha["nome"]}')
print(f'Média igual: {ficha["média"]}')
if ficha["média"] >= 6:
    print('Situação: Aprovado')
else:
    print('Situação: Reprovado')