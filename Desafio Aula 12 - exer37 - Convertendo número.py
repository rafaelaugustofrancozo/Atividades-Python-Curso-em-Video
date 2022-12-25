import math
print('\033[7;34;40mCONVERSÃO DE NÚMERO REAL PARA OUTROS SISTEMAS NUMÉRICOS!\033[m')
num = int(input('Digite o número: '))
print('Para qual sistema número você deseja converter o número: ')
escolha = int(input('Digite:\n 1, para binário;\n 2, para octal;\n 3, para hexadecimal;\n'))
if escolha == 1:
    print('Opção escolhida: \033[4mbinário.\033[m O resultado da conversão é: {:2.f}'.format(bin(num)))
elif escolha == 2:
    print('Opção escolhida: \033[4octal.\033[m O resultado da conversão é: {}'.format(oct(num)))
else:
    print('Opção escolhida: \033[4hexadecimal.\033[m O resultado da conversão é: {}'.format(hex(num)))