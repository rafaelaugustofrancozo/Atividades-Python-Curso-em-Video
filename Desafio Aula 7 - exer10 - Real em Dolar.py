#Real em dólar (considerando o dólar a 3.27 reais)
num = float(input('Digite um número: '))
print('Com R${:.2f} é possível comprar US${:.2f}'.format(num,num/3.27))
