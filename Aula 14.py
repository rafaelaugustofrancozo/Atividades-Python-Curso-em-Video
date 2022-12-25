for c in range(1,10):
    print(c)
print('FIM')

c=1
while c < 10:
    print(c)
    c+=1
print('FIM')

#FOR EU USO QUNDO EU SEI O LIMITE, OU CONSIGO DEFINI-LO PREVIAMENTE, WHILE EU USO QUANDO NÃO SEI O LIMITE

n=1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')

n=1
par=impar=0
while n !=0:
    n = int(input('Digite um valor: '))
    if n!=0:
        if n % 2 == 0:
            par+= 1
        else:
            impar+= 1
print('Foram digitados {} número (s) pares'.format(par))
print('Foram digitados {} número (s) ímpares'.format(impar))
print('Acabou')