altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
print('A área a ser pintada é de {:.2f}, e gastará {} litros de tinta para ser pintada!'.format(area, area/2))