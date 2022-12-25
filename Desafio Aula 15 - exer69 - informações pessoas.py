mais18 = qthomem = qtmulher = qtmulhermenos20 = qtpessoas = 0
while True:
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa(M/F): ')).upper().strip()[0]
    idade = int(input('Digite a idade da pessoa: '))
    if idade > 18:
        qtpessoas+= 1
    if sexo == 'M':
        qthomem+= 1
    if sexo == 'F' and idade < 20:
        qtmulhermenos20+= 1
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Deseja cadastrar mais dados(S/N): ')).upper().strip()[0]
    if pergunta == 'N':
       break

print(f'\nQuantidade de pessoas com mais de 18 anos: {qtpessoas}')
print(f'Número de homens cadastrados: {qthomem}')
print(f'Número de mulheres com menos de 20 anos: {qtmulhermenos20}')