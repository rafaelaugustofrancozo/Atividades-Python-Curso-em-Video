#exer49
print('\033[1;31;31m==========TABUADA==========\033[m')
n = int(input('TABUADA DO? '))
for c in range(0,11):
    print('\033[1;33;33m{}\033[m X \033[1;31;31m{}\033[m: \033[1;34;34m{}\033[m'.format(n, c, n*c))