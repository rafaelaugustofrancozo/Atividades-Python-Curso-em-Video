import math #importa a biblioteca inteira
from math import sqrt #só importa a função sqrt
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é {}!'.format(num, math.ceil(raiz)))#ceil arredonda pra cima, floor pra baixo
