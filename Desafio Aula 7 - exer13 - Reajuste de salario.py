salario = float(input('Digite o salário atual do funcionário: '))
reajuste = float(input('Digite o percentual a ser reajustado: '))
reajusteaplicado = reajuste/100
print('Salário atual: R${:.2f}'.format(salario))
print('Novo salário com reajuste de {}%: R${:.2f}'.format(reajuste, salario+(salario*reajusteaplicado)))