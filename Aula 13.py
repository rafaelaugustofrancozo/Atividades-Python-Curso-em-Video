for c in range(0,6):
    print('oi')
print('fim')

for c in range(0,7):
    print(c)
print('fim')


for c in range(6,0,-1):#contar pra tras
    print(c)
print('fim')

for c in range(0,7,2): #saltar de dois em dois
    print(c)
print('fim')

i = int(input('inicio: '))
f = int(input('fim: '))
p = int(input('passo: '))
for c in range(i, f+1, p):
    print(c)
print('fim')

s = 0
for c in range(0,4):
    n = int(input('Digite um numero: '))
    s+=n
print('O resultado é {}'.format(s))
print('fim')