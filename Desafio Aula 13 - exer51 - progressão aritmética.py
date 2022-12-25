primeirotermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for c in range(primeirotermo, (razao*9)+primeirotermo, razao):
    print('{}'.format(c), end='-')
print('FIM')