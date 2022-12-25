#exer52
print('\033[1;33;33m==========\033[m\033[1;33;33mVERIFICAR SE O NÚMERO É PRIMO\033[m\033[1;33;33m==========\033[m')
n = int(input('DIGITE UM NUMERO: '))
v1 = 0

for c in range(1, n+1):
    if n % c == 0:
        print('\033[34m',end= ' ')
    else:
        print('\033[31m',end= ' ')
        v1+= 1
    print('{}'.format(c), end= ' ')
if v1 == 2:
    print('\nNum: {}, Qd Divisíveis: {}. PRIMO!'.format(n, v1))
else:
    print('Num: {}, Qd Divisíveis: {}. NÃO É PRIMO!'.format(n, v1))