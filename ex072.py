numptbr = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze','Treze', 'Catorse', 'Quinse', 'Dezesseis', 'Dezessete',
           'Dezoito', 'Dezenove', 'Vinte')

while True:
    núm = int(input('Digite um número entre 0 e 20:'))
    if 0 <= núm <= 20:
        break
    print('Tente novamente.', end=' ')
print(f'Você digitou o número {numptbr[núm]}')
