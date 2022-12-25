print('\033[0;32;32m==========COMPARANDO NÚMEROS==========\033[m')
num1 = float(input('Digite um número: '))
num2 = float(input('Digite mais um número: '))
print('\033[0;32;32m==========INFORMAÇÕES E RESULTADOS==========\033[m')
print('Primeiro valor digitado: \033[4;31;33m{:.2f}\033[m'.format(num1))
print('Segundo valor digitado: \033[4;31;33m{:.2f}\033[m'.format(num2))
if num1 > num2:
    print('\033[0;34;34mO PRIMERO VALOR É MAIOR!\033[m')
elif num2 > num1:
    print ('\033[0;34;34mO SEGUNDO VALOR É MAIOR!\033[m')
else:
    print ('\033[0;34;34mOS DOIS VALORES SÃO IGUAIS!\033[m')
