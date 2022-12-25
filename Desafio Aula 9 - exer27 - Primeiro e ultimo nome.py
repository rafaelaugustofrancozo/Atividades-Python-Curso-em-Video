nome = str(input('Digite um nome completo: ')).strip()
lista = nome.split()
print(lista)
print('{}'.format(len(lista)))
print('O ultimo nome é {}'.format(lista[len(lista)-1]))
print('O primeiro nome é {} e o último nome é {}'.format(lista[0], lista.pop()))#essa função pop vai tirar o item da lista, de acordo com o index passado, e pegar para si (caso eu declare ela alimentando uma variável). Se não passar index nenhum, ela pega o ultimo da lista por padrão