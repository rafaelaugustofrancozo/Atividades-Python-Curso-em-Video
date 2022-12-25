tabela = ('Cruzeiro', 'Grêmio', 'Vasco', 'Bahia', 'Sampaio Corrêa', 'Ituano',
          'Sport Recife', 'Criciúma', 'Londrina', 'Guarani', 'CRB', 'Ponte Preta',
          'Vila Nova', 'Chapecoense', 'Tombense', 'Novohorizontino', 'CSA', 'Brusque'
          ,'Operário', 'Náutico')
cont = 1
print('Quatro primeiros: ', end='')
for num in range(0,5):
        if num != 4:
            print(f'{tabela[num]}, ', end = '')
        else:
            print(f'{tabela[num]}', end='')
print(f'\nQuantro primeiros: {tabela[0:5]}') #Opção simples, retornando a tupla sem formatação, a opção acima fiz de forma mais elegante, removendo parenteses e aspas simples
print(f'Os Rebaixados: {tabela[-4:]}')
print(f'Tabela em ordem alfabética:{sorted(tabela)}')
for pos, cont in enumerate(tabela):
    if cont == 'Chapecoense':
        print(f'Posição final da Chape: {pos+1}')