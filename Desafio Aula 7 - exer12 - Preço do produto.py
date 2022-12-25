preco = float(input('Digite o preço do produto: '))
desconto = float(input('Digite o percentual de desconto: '))
descontoaplicado = desconto/100
print('Preço sem desconto: R${:.2f}'.format(preco))
print('Preço com desconto de {}%: R${:.2f}'.format(desconto, preco-(preco*descontoaplicado)))