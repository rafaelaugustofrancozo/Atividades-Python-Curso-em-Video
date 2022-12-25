#exer47
print('\033[1;32;32m=====================NUMEROS PARES====================\033[m')
for c in range(2,51):
    if c % 2 == 0:
        print('\033[1;32;32m{}, \033[m'.format(c), end=' ')
print('FIM')

for c in range(2,51, 2):
        print('\033[1;32;32m{}, \033[m'.format(c), end=' ')
print('FIM')