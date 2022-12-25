from datetime import date
print('\033[1;33;33m==========VERIFICAÇÃO DE MAIORIDADE==========\033[m')
vetor = []
for c in range(0,7):
    vetor.append(int(input('DIGITE O ANO DE NASCIMENTO: ')))
print(vetor)
ma = 0
me = 0
atual = date.today().year
for c in range(0, len(vetor)):
    if  atual - vetor[c] >= 18:
      ma+= 1
    else:
      me+= 1
print('MAIORES DE IDADE: \033[1;33;33m{}\033[m. MENORES DE IDADE: \033[1;33;33m{}\033[m'.format(ma,me))

#SOLUÇÃO DO PROFESSOR
from datetime import date
print('\033[1;33;33m==========VERIFICAÇÃO DE MAIORIDADE==========\033[m')
ma = 0
me = 0
atual = date.today().year
for c in range(0,7):
    nasc = int(input('DIGITE O ANO DE NASCIMENTO: '))
    idade = atual - nasc
    if  idade >= 18:
      ma+= 1
    else:
      me+= 1
print('MAIORES DE IDADE: \033[1;33;33m{}\033[m. MENORES DE IDADE: \033[1;33;33m{}\033[m'.format(ma,me))
