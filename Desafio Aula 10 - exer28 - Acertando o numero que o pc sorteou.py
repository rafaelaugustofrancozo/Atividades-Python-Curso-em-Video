import random
lista = [0,1,2,3,4,5]
epc = random.choice(lista)
#print('Numero: {}'.format(epc))
num = int(input('Digite o número que o computador pensou:'))
if num == epc:
    print('Você disse que o número é {}, e o computador escolheu o mesmo número! Que sorte!'.format(num))
else:
    print('Você disse que o número é {}, porém o número foi {}. Mais sorte na próxima vez...'.format(num, epc))

#solução do professor
from random import randint
computador = randint(0,5)#o sorteio
jogador = int(input('Digite o número que o computador pensou:'))
if jogador == computador:
    print('Você disse que o número é {}, e o computador escolheu o mesmo número! Que sorte!'.format(jogador))
else:
    print('Você disse que o número é {}, porém o número foi {}. Mais sorte na próxima vez...'.format(jogador, computador))
