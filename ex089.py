from pynput import keyboard

ficha = []

while True:
    nome = str(input('Nome: ')).strip()
    nota1 = float(input('1º nota: '))
    nota2 = float(input('2º nota: '))
    média = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], média])

    resp = str(input('Quer continuar? [S/N]: ')).strip()
    if resp not in 'NnSs':
        resp = str(input('Resposta invalida...\nQuer continuar? [S/N]: ')).strip()
    
    if resp in 'Nn':
        break

print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 24)
for i, f in enumerate(ficha):
    print(f'{i + 1:<4}{f[0]:<10}{f[2]:>8.1f}')
while True:
    opc = str(input('Mostrar notas de qual aluno? ( "999" Para finalizar )'))
    if opc <= len(ficha) -1:
        print(f'Notas {ficha[opc][0]} são {ficha[opc][1]}')
    if opc == 999:
        print('Finalizando...')
        break
