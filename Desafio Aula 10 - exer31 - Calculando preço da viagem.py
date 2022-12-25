km = float(input('Digite a distância da viagem:'))
if km <=200:
    print('Valor da passagem: R${:.2f}'.format(km*0.5))
else:
    print('Valor da passagem: R${:.2F}'.format(km*0.45))