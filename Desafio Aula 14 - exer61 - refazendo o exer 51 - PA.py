#primeirotermo = int(input('Primeiro termo: '))
#razao = int(input('Razão: '))
#c= primeirotermo
#while c <= (razao*9)+primeirotermo:
#    print('{}'.format(c), end='-')
#    c+= razao
#pergunta = str(input('\nDeseja mostrar mais alguns termos?(S/N) ')).upper().strip()
#if pergunta == 'S':
#    quantos = int(input('Quantos termos? '))
#    while c <= (razao*(9+quantos))+primeirotermo:
#        print('{}'.format(c), end='-')
#        c+= razao
#print('\nFIM')

primeirotermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c= primeirotermo
cont = 0
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(c), end='')
        print(' - ' if cont < total else '', end='')
        c+= razao
        cont+=1
    mais = int(input('\nDeseja adicionar mais quantos valores à sequencia: '))
print('FIM')