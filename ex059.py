from time import sleep
pvalor = int(input('Digite um valor:'))
svalor = int(input('digite um segundo valor:'))
escolha = 0

while escolha != 5:
    print('Escolha um das opções abaixo')
    print('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior número\n[ 4 ] Digitar novos números\n[ 5 ] Sair do programa')
    escolha = int(input('Qual sua escolha?'))

    if escolha == 1:
        soma = pvalor + svalor
        print(f'O resultado de {pvalor} + {svalor} = {soma}')
    elif escolha == 2:
        multiplicação = pvalor * svalor
        print(f'O resultado de {pvalor} x {svalor} = {multiplicação}')
    elif escolha == 3:
        if pvalor > svalor:
            maior = pvalor
        else:
            maior = svalor
        print(f'O maior valor digitado é {maior}')
    elif escolha == 4:
        pvalor = int(input('Digite um valor:'))
        svalor = int(input('digite um segundo valor:'))
    elif escolha == 5:
        print('Fnalizando...')
        sleep(3)
    else:
        print('Opção invalida, por favor tente novamente.')
    print(10 * '==')
print('Fim do programa, ate aproxima')


