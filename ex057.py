sexo = str(input('Informe sua sexualidade [F/M]: ')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Dados invalidos, por favor, informe seu sexo corretamente: ')).strip().upper()[0]
print(f'sexo {sexo} registrado ')