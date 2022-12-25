import random
print('\033[0;35;35m=====JOGO DO PAR OU ÍMPAR=====\033[m')
vitorias = 0

while True:
    jogodopc = random.randint(0,5)
    jogodoplayer = int(input('\nDigite o seu valor: '))
    soma = jogodopc + jogodoplayer
    jogada = ' '
    while jogada not in 'PI':
        jogada = str(input('\033[0;33;33mPAR OU ÍMPAR? (P/I)\033[m ')).upper().strip()[0]
    if jogada == 'P':
        if soma % 2 == 0:
            print(f'Você jogou {jogodoplayer} e o computador jogou {jogodopc} e deu PAR')
            print('\033[0;32;32m\n*****VOCÊ VENCEU!*****\033[m')
            vitorias += 1
        else:
            print(f'Você jogou {jogodoplayer} e o computador jogou {jogodopc} e deu IMPAR')
            print('Você perdeu...')
            break
    else:
        if soma % 2 == 0:
            print(f'Você jogou {jogodoplayer} e o computador jogou {jogodopc} e deu PAR')
            print('Você perdeu...')
            break
        else:
            print(f'Você jogou {jogodoplayer} e o computador jogou {jogodopc} e deu IMPAR')
            print('\033[0;32;32m\n*****VOCÊ VENCEU!*****\033[m')
            vitorias += 1

print(f'\033[1;31;31mGAME OVER!\033[m VITÓRIAS: \033[1;32;32m{vitorias}\033[m')
