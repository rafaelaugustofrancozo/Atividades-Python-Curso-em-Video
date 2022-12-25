import random
nome1 = str(input('Digite os nome do primeiro aluno: '))
nome2 = str(input('Digite os nome do segundo aluno: '))
nome3 = str(input('Digite os nome do terceiro aluno: '))
nome4 = str(input('Digite os nome do quarto aluno: '))
lista = [nome1, nome2, nome3, nome4]
roletar = random.choice(lista)
print('O aluno escolhido é {}!'.format(roletar))