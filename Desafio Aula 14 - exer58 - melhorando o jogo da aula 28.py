#solução do professor
from random import randint
computador = randint(0,5)#o sorteio
jogador = 10
contador = 1
while computador != jogador:
        jogador = int(input('Digite o número que o computador pensou:'))
        if jogador != computador:
            print('Você disse que o número é {}, mas errou. Tente novamente!'.format(jogador))
            contador+= 1
print('Você acertor! O computador pensou no número {}!. Você tentou {} vez(es) até acertar!'.format(computador, contador))