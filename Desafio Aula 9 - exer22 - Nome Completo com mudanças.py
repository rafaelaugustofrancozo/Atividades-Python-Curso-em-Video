nome = str(input('Digite o nome completo: '))
print(nome)
print('Nome com tudo maiúsculo: {}'.format(nome.upper()))
print('Nome com tudo minúsculo: {}'.format(nome.lower()))
semespaco = nome.replace(' ', '')
print('Quantidade de caracteres no nome: {}'.format(len(semespaco)))
dividido = nome.split()
print('Quantidade de letras do primeiro nome: {}'.format(len(dividido[0])))