import math
ang = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print('O ângulo digitado é de {:.2f} graus. Seu seno é de {:.2f}, cosseno é {:.2f}, e tangente é {:.2f}!'.format(ang, seno, cosseno, tangente))