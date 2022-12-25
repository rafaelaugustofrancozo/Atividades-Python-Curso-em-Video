media = 0
contmulher = 0
idadehomemvelho = 0
nomehomemvelho = ''
for c in range(1,5):
    print('======{}a PESSOA======'.format(c))
    nome = str(input('DIGITE O NOME: '))
    idade = int(input('DIGITE A IDADE: '))
    sexo = str(input('DIGITE O SEXO (M/F):')).upper()
    media+= idade
    if sexo == 'F' and idade < 20:
        contmulher+= 1
    if sexo == 'M':
        if c == 0:
            nomehomemvelho = nome
            idadehomemvelho = idade
        else:
            if idade > idadehomemvelho:
                idadehomemvelho = idade
                nomehomemvelho = nome

print('Media de idade das pessoas: {}'.format(media/4))
print('Qtd mulheres menores de 20: {}'.format(contmulher))
print('Nome do homem mais velho: {},e sua idade é de: {}.'.format(nomehomemvelho, idadehomemvelho))
