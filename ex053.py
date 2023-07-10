word = str(input('Digite uma frase:')).strip().upper()
palavra = word.split()
junto = ''.join(palavra)
inverso = ''
for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]
print(junto, inverso)
if junto == inverso:
    print(f'{word} é um palidromo ')
else:
    print(f'{word} não é um palidromo')

