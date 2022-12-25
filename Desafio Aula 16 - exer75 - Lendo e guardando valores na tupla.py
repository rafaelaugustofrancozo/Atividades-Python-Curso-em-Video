val1 = int(input('Digite o primeiro valor: '))
val2 = int(input('Digite o segundo valor: '))
val3 = int(input('Digite o terceiro valor: '))
val4 = int(input('Digite o quarto valor: '))
tupla = (val1, val2, val3, val4)
print(f'A tupla é: {tupla}')
cont = 0
cont2 = 0
for pos, itens in enumerate(tupla):
    if itens == 9:
        cont+= 1
    if itens == 3:
        cont2+= 1
print(f'Quantidade de vezes que o 9 aparece: {cont}')
if cont2 != 0:
    print(f'Primeira incidência do 3: {tupla.index(3)}')
else:
    print(f'O número 3 não foi digitado nenhuma vez.')
print(f'Valores pares digitados: ', end='')
for itens in tupla:
    if itens % 2 == 0:
        print(f'{itens} ', end='')



