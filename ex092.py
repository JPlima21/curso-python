from datetime import datetime
cadastro = {}
cadastro['nome'] = str(input('Nome: ')).strip()
nasc = int(input('Ano de nascimento: '))
cadastro['idade'] = datetime.now().year - nasc
cadastro['ctps'] = int(input('Carteira de Trabalho (0 caso não tenha): '))

if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Salário: R$'))
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in cadastro.items():
    print(f' - {k} tem valor {v}')