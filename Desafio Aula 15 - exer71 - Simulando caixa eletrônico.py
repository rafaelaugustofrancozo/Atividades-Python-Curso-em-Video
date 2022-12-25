#conta20 = valor20 = conta10 = valor10 = conta1 = valor1 = 0
#print('\033[1;33;33m{:=^100}\033[m'.format('| BEM VINDO AO BANCO R.A.F! |'))
#while True:
#    valor = (int(input('Qual o valor de saque: R$')))
#    conta50 = int(valor / 50)
#    if valor % 50 != 0:
#        valor20 = valor % 50
#        conta20 = int(valor20 / 20)
#    if valor20 % 20 != 0:
#        valor10 = valor20 % 20
#        conta10 = int(valor10 / 10)
#    if valor10 % 10 != 0:
#        valor1 = valor10 % 10
#        conta1 = int(valor1 / 1)
#    break
#print('\n\033[1;32;32mVALOR A SER SACADO: R${}\033[m'.format(valor))
#print(f'\nQuantidade de cédulas de 50 reais: {conta50}')
#print(f'Quantidade de cédulas de 20 reais: {conta20}')
#print(f'Quantidade de cédulas de 10 reais: {conta10}')
#print(f'Quantidade de cédulas de 1 real: {conta1}')
#print('\n\033[1;33;33m{:*^100}\033[m'.format('OBRIGADO POR UTILIZAR NOSSOS SERVIÇOS! VOLTE SEMPRE!'))

#SOLUÇÃO DO PROFESSOR
valor = int(input('Que valor deseja sacar: R$'))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de {ced} reais!')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('OBRIGADO')




