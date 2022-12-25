tupla = ('pão',1,'leite',2.50,'café',3.20)
print('='*20, end='\n')
print('LISTAGEM DE PREÇOS')
print('='*20)
for pos, itens in enumerate(tupla):
    if pos % 2 == 0:
        print(f'{itens}', end='')
       #print('='*10, end='')
    else:
        print('*'*20, end='')
        print(f'{itens:.2f}')