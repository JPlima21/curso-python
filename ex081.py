lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N]')).strip()
    if resp not in 'NnSs':
        resp = str(input('Por favor digite sua resposta novamente...\nQuer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'Você digitou {len(lista)} valores')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista...')