num = int(input('Digite o número: '))
#a = 1
print ('======TABUADA DO {:=<6}'.format(num))
for a in range(11):
    print('{} x {} = {}'.format(num, a, num*a))