n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s+= n
s-= 999 #GAMBIARRA! O BREAK SERVE PARA ISSO,INTERROMPER A EXECUÇÃO ONDE DE FATO É NECESSÁRIO.
print('A soma é: \033[0;33;33m{}\033[m'.format(s))

#criando a rotina com o break, e o loop infinito

s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s+= n
#s-= 999 GAMBIARRA ELIMINADA
print('A soma é: \033[0;33;33m{}\033[m'.format(s))# PYTHON 3
print(f'A soma é: \033[0;33;33m{s}\033[m') #PYTHON 3.6+
print('A soma é: %d' %(s)) #PYTHON 2
