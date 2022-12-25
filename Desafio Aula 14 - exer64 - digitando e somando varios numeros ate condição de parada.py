parada = 0
contador = 0
soma = 0
vetor = []
print('\033[2;33;33m========================= RECEBENDO, CONTANDO E SOMANDO NÚMEROS! =======================\033[m')
while parada != 999:
    num = int(input('Digite um número: '))
    if num != 999:
        contador+= 1
        soma+= num
        vetor.append(num)
    else:
        parada = 999
print('Numeros digitados: {}'.format(vetor))
print('Quantidade de números digitados: {}. Somatório final: {}'.format(contador, soma))
print('FIM')
