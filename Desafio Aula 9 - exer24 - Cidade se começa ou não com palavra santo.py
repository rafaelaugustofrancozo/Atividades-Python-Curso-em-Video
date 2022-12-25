#minha solução
cidade = str(input('Digite o nome da cidade: '))
dividido = cidade.strip().upper().split()
result = 'SANTO' in dividido[0]
print('Começa com a palavra "Santo"? {}'.format(result))


#solução do professor
cidade = str(input('Digite o nome da cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')