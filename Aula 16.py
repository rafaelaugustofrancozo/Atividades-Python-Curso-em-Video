#tuplas (usa-se entre parenteses)
#tuplas são imutaveis
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[0])
print(lanche[1:3])#desconsidera o ultimo
print(lanche[2:])#do terceiro até o fim
print(lanche[:2])#do primeiro item até o segundo
print(lanche[-3:])#conta começando do ultimo, e lista até o final


for comida in lanche:
    print(f'Itens da lista: {comida}')

for cont in range (0, len(lanche)):
    print(f'{lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'{comida} na posição {pos}')