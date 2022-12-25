num = int(input('Digite um número:'))
print('O número digitado foi {}, e é um número par.' if num % 2 == 0 else 'O número digitado foi {}, e é um número ímpar.'.format(num, num))