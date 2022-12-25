#exer48
print('\033[1;33;33m===================SOMA DOS ÍMPARES ATÉ 500==================\033[m')
n = 0
qt = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end= ' ')
        n+= c
        qt+= 1
print('\nSoma: {}'.format(n))
print('Quantidade de num.: {}'.format(qt))
print('FIM')