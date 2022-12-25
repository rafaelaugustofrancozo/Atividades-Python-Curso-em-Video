import random
print('==========JOKENPÔ!==========')
meujogo = str(input('Pedra, papel ou tesoura? ')).lower().strip()
outrojogo = ['pedra', 'papel', 'tesoura']
pegajogopc = str(random.choice(outrojogo))

if meujogo != 'pedra' and meujogo != 'papel' and meujogo != 'tesoura':
    print('OPÇÃO NÃO EXISTE, JOGUE NOVAMENTE!')
    exit()
else:
    print('SUA JOGADA: {}'.format(meujogo))
    print('JOGO DO PC: {}'.format(pegajogopc))

    if meujogo == 'pedra' and pegajogopc == 'tesoura':
        print('VOCÊ GANHOU!')
    elif meujogo == 'pedra' and pegajogopc == 'papel':
        print('VOCÊ PERDEU!')
    elif meujogo == 'pedra' and pegajogopc == 'pedra':
        print('EMPATE!')
    elif meujogo == 'tesoura' and pegajogopc == 'pedra':
        print('VOCÊ PERDEU!')
    elif meujogo == 'tesoura' and pegajogopc == 'papel':
        print('VOCÊ GANHOU!')
    elif meujogo == 'tesoura' and pegajogopc == 'tesoura':
        print('EMPATE!')
    elif meujogo == 'papel' and pegajogopc == 'pedra':
        print('VOCÊ GANHOU!')
    elif meujogo == 'papel' and pegajogopc == 'tesoura':
        print('VOCÊ PERDEU!')
    else:
        print('EMPATE!')