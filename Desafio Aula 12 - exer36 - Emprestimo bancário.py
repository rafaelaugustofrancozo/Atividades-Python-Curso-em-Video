print('==========TESTE DE CRÉDITO==========')
valcasa = float(input('Digite o valor da casa: '))
valsalario = float(input('Digite o seu salário: '))
anos = int(input('Em quantos anos pretende pagar: '))
valmensal = valcasa / (anos * 12)
salcomdesconto = valsalario * 0.30
print('Valor do imóvel pretendido: \033[7;32;40mR${:.2f}\033[m'.format(valcasa))
print('Salário atual do contratante: \033[7;32;40mR${:.2f}\033[m'.format(valsalario))
#print('valor mensal: \033[0:33:35m{:.2f}\033[0:33:35m'.format(valmensal))
#print('30% do salário: {:.2f}'.format(salcomdesconto))
if salcomdesconto >= valmensal:
    print('Seu empréstimo foi concedido! O valor da prestação da casa será de: \033[7;32;40mR${:.2f}\033[m'.format(valmensal))
else:
    print('\033[7;31;40mEMPRÉSTIMO NEGADO\033[m\n O valor da prestação excede 30% do seu salário, que hoje é de R${:.2f}. Lamentamos.'.format(salcomdesconto))
