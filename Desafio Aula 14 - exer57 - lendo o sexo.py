sexo = ''
#while sexo not in 'MmFf':
while sexo != 'M' and sexo != 'F':
    sexo = str(input('DIGITE O SEXO (M/F): ')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print('Valor incorreto, por favor digite novamente')
print('FIM')