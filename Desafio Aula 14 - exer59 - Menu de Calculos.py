from time import sleep
opcao = 0
n1 = 0
n2 = 0
while opcao != 5:
    print('[1] - SOMA')
    print('[2] - SUBTRAÇÃO')
    print('[3] - MULTIPLICAÇÃO')
    print('[4] - DIVISÃO')
    print('[5] - SAIR')
    opcao = int(input('ESCOLHA A OPÇÃO: '))
    if opcao == 1:
        print('Opção escolhida : [1] - SOMA')
        n1 = float(input('Digite o primeiro valor do cálculo: '))
        n2 = float(input('Digite o segundo valor do cálculo: '))
        resultado = n1 + n2
        print('Resultado: {}\n'.format(resultado))
    elif opcao == 2:
        print('Opção escolhida : [2] - SUBTRAÇÃO')
        n1 = float(input('Digite o primeiro valor do cálculo: '))
        n2 = float(input('Digite o segundo valor do cálculo: '))
        resultado = n1 - n2
        print('Resultado: {}\n'.format(resultado))
    elif opcao == 3:
        print('Opção escolhida : [3] - MULTIPLICAÇÃO')
        n1 = float(input('Digite o primeiro valor do cálculo: '))
        n2 = float(input('Digite o segundo valor do cálculo: '))
        resultado = n1 * n2
        print('Resultado: {}\n'.format(resultado))
    elif opcao == 4:
        print('Opção escolhida : [4] - DIVISÃO')
        n1 = float(input('Digite o primeiro valor do cálculo: '))
        n2 = float(input('Digite o segundo valor do cálculo: '))
        resultado = n1 / n2
        print('Resultado: {}\n'.format(resultado))
    elif opcao == 5:
        print('Opção escolhida : [5] - SAIR')
        opcao = 5
        print('Finalizando...')
        sleep(3)
print('FIM')

