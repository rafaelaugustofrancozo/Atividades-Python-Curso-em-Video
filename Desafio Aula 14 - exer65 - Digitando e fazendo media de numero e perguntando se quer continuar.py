pergunta = 'S'
contador = 0
media = 0
soma = 0
maior = 0
menor = 0
vetor = []
print('\033[2;33;33m========================= RECEBENDO, FAZENDO A MÉDIA, MAIOR E MENOR! =======================\033[m')
while pergunta != 'N':
    num = int(input('Digite um número: '))
    contador+= 1
    soma+= num
    vetor.append(num)
    if contador == 1:
        maior = num
        menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num
    pergunta = str(input('Deseja adicionar mais números? (S/N)')).upper().strip()[0]
print('Numeros digitados: {}'.format(vetor))
print('Quantidade de números digitados: {}. Somatório final: {}'.format(contador, soma))
print('Maior valor digitado: {}. Menor valor digitado: {}'.format(maior, menor))
print('Media final: {}'.format(soma/contador))
print('FIM')
