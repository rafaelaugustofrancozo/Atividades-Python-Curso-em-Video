vel = float(input('Digite a velocidade do carro:'))
velad = vel-80
print('Limite de velocidade da pista: 80KM/H')
print('Velocidade registrada: {:.2f}KM/H'.format(vel))
if vel>80:
    print('Você foi pego acima do limite de velocidade! Sua multa será de R${:.2f}'.format(velad*7))
print('Tenha uma boa viagem! Dirija com segurança!')

