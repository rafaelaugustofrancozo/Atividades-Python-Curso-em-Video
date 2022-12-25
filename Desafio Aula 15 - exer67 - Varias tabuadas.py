while True:
    n = int(input('\033[1;32;32mQuer ver a tabuada de qual valor? (DIGITE UM VALOR NEGATIVO PARA PARAR)\033[m '))
    if n < 0:
        break
    for c in range (1, 11, 1):
        print(f'\033[1;34;34m{n} x {c}\033[m = \033[1;33;33m{n*c}\033[m')
print('\033[1;31;31m=\033[m'*20, end='')
print('\033[1;31;31mACABOU\033[m', end='')
print('\033[1;31;31m=\033[m'*20 )
