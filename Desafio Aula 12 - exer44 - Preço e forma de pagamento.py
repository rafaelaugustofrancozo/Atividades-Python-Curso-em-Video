print('\033[1;33;33m==========PREÇO DO PRODUTO\033[4;33;33m==========')
print('\n\033[4;32;32mFORMAS DE PAGAMENTO DISPONÍVEIS:\033[m\n'
      '\n1 - À VISTA (DINHEIRO OU CHEQUE) - \033[1;31;31m10% DE DESCONTO\033[m'
      '\n2 - À VISTA (CARTÃO) - \033[1;31;31m5% DE DESCONTO\033[m'
      '\n3 - EM ATÉ 2X NO CARTÃO - \033[1;31;31mPREÇO NORMAL\033[m'
      '\n4 - 3 OU MAIS X NO CARTÃO - \033[1;31;31m20% DE JUROS\033[m\n')

formapagamento = int(input('\033[1;;mESCOLHA A OPÇÃO PARA PAGAMENTO(1,2,3 OU 4):\033[m '))
valproduto = float(input('Qual o valor do produto? '))

if formapagamento == 1:
      print('\n\033[4;39;39mOPÇÃO ESCOLHIDA:\033[m \033[1;32;32m{} - À VISTA (DINHEIRO OU CHEQUE).\033[m O valor do produto será de \033[1;34;34mR${:.2f}\033[m'.format(formapagamento, valproduto - (valproduto * 0.10)))
elif formapagamento == 2:
      print('\n\033[4;39;39mOPÇÃO ESCOLHIDA:\033[m \033[1;32;32m{} - À VISTA (CARTÃO).\033[m O valor do produto será de \033[1;34;34mR${:.2f}\033[m'.format(formapagamento, valproduto - (valproduto * 0.05)))
elif formapagamento == 3:
      print('\n\033[4;39;39mOPÇÃO ESCOLHIDA:\033[m \033[1;32;32m{} - EM ATÉ 2X NO CARTÃO.\033[m O valor do produto será de \033[1;34;34mR${:.2f}\033[m'.format(formapagamento, valproduto))
else:
      print('\n\033[4;39;39mOPÇÃO ESCOLHIDA:\033[m \033[1;32;32m{} - 3 OU MAIS X NO CARTÃO.\033[m O valor do produto será de \033[1;34;34mR${:.2f}\033[m'.format(formapagamento, valproduto + (valproduto * 0.20)))