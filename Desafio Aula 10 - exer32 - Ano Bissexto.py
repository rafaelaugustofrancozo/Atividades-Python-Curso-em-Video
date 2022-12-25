import math
ano = str(input('Digite o ano:'))
dezena = int(ano[len(ano)-2::])
if dezena % 4 == 0:
    print('O ano de {} é bissexto!'.format(ano))
else:
    print('0 ano de {} não é bissexto!'.format(ano))