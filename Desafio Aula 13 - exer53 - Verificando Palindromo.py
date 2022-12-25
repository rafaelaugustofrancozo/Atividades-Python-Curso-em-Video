#exer53
print('==========VERIFICAÇÃO DE PALÍNDROMO============')
frase = str(input('Digite a frase: '))
frase2 = frase.replace(' ', '').strip()
print('Palavra digitada sem os espaços para verificação: \033[1;33;33m{}\033[m'.format(frase2))
palavrainvertida = frase2[len(frase)+2::-1]
print('Palavra invertida para verificação: \033[1;33;33m{}\033[m'.format(palavrainvertida))
if frase == palavrainvertida:
    print('PALÍNDROMO')
else:
    print('NÃO É CASO DE PALÍNDROMO!')

#SOLUÇÃO DO PROFESSOR
frase = str(input('Digite a frase: '))
palavras = frase.split( )
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso+= junto[letra]
if inverso == junto:
    print('PALÍNDROMO')
else:
    print('NÃO É PALÍNDROMO')