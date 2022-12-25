print('\033[1;33;33m==========VERIFICAÇÃO DE PESO==========\033[m')
vetor = []
for c in range(0,5):
    vetor.append(float(input('DIGITE O PESO: ')))
print(vetor)
vetor.sort()
print('MAIOR PESO: \033[1;33;33m{}\033[m. MENOR PESO: \033[1;33;33m{}\033[m'.format(vetor[4],vetor[0]))

#solução do professor
maiorpeso = 0
menorpeso = 0
for p in range (0,5):
    peso = float(input('Digite o peso da pessoa {}:'.format(p)))
    if p == 0:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print('O maior peso lido foi: {}'.format(maiorpeso))
print('O menor peso lido foi: {}'.format(menorpeso))

