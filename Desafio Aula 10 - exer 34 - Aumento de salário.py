sal = float(input('Digite o salário atual:'))
if sal > 1250:
    print('O reajuste do salário nessa faixa é de 10%. Portanto o novo salário será R${:.2f}'.format((sal* 0.10) + sal))
else:
    print('O reajuste do salário nessa faixa é de 15%. Portanto o novo salário será R${:.2f}'.format((sal*0.15)+sal))