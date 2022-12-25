#cato = float(input('Digite o cateto oposto: '))
#cata = float(input('Digite o cateto adjacente: '))
#hi = (cato ** 2 + cata ** 2) ** (1/2)
#print('O valor da hipotenusa é {}'.format(hi))
import math
cato = float(input('Digite o cateto oposto: '))
cata = float(input('Digite o cateto adjacente: '))
hi = math.hypot(cato, cata)
print('O valor da hipotenusa é {}'.format(hi))