import math

num = str(input('Digite um número de 0 a 9999'))
print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[len(num)-2]))
print('Centena: {}'.format(num[len(num)-3]))
print('Milhar: {}'.format(num[len(num)-4]))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10 #forma matematica para pegar cada casa, divindo o numero pela divisão inteira, e depois pegando o resto da divisão para o valor