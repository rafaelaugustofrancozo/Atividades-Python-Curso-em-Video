#exer50
print('\033[1;36;36m==========SOMANDO APENAS OS INTEIROS PARES!==========\033[m')
n1=int(input('DIGITE UM NÚMERO: '))
n2=int(input('DIGITE UM NÚMERO: '))
n3=int(input('DIGITE UM NÚMERO: '))
n4=int(input('DIGITE UM NÚMERO: '))
n5=int(input('DIGITE UM NÚMERO: '))
n6=int(input('DIGITE UM NÚMERO: '))
s=0
VETOR = [n1,n2,n3,n4,n5,n6]
for c in range (0, len(VETOR)):
    if VETOR[c] % 2 == 0:
        s+=VETOR[c]
print(s)
print('FIM')

n= 0
s= 0
co=0
for c in range (1, 7):
    n = int(input('DIGITE UM {} NÚMERO: '.format(c)))
    if n % 2 == 0:
        s += n
        co += 1
print('Voce informou {} numeros pares, e a soma é {}'.format(co, s))