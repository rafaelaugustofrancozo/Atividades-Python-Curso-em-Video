from datetime import date, datetime
print('\033[0;36;1m==========CNN - CATEGORIAS==========\033[m')
print('CATEGORIAS POR IDADE:\n'
      'ATÉ \033[0;35;1m9 ANOS:\033[m \033[0;34;1mMIRIM\033[m\n'
      'ATÉ \033[0;35;1m14 ANOS:\033[m \033[0;34;1mINFANTIL\033[m\n'
      'ATÉ \033[0;35;1m19 ANOS:\033[m \033[0;34;1mJUNIOR\033[m\n'
      'ATÉ \033[0;35;1m20 ANOS:\033[m \033[0;34;1mSENIOR\033[m\n')
anonascimento = int(input('Digite o ano de nascimento do atleta: '))
anoatual = date.today()
anostring = str(anoatual)
ano2 = anostring[0:4:]
anoint = int(ano2)
if anoint - anonascimento <=9:
      print('IDADE: \033[0;34;1m{}\033[m\n'
            '\033[0;35;1mCATEGORIA DO ATLETA:\033[m \033[0;34;1mMIRIM\033[m'.format(anoint - anonascimento))
elif anoint - anonascimento >=10 and anoint - anonascimento <=14:
      print('IDADE: \033[0;34;1m{}\033[m\n'
            '\033[0;35;1mCATEGORIA DO ATLETA:\033[m \033[0;34;1mINFANTIL\033[m'.format(anoint - anonascimento))
elif anoint - anonascimento >=14 and anoint - anonascimento <=19:
      print('IDADE: \033[0;34;1m{}\033[m\n'
            '\033[0;35;1mCATEGORIA DO ATLETA:\033[m \033[0;34;1mJUNIOR\033[m'.format(anoint - anonascimento))
elif anoint - anonascimento == 20:
      print('IDADE: \033[0;34;1m{}\033[m\n'
            '\033[0;35;1mCATEGORIA DO ATLETA:\033[m \033[0;34;1mSENIOR\033[m'.format(anoint - anonascimento))
else:
      print('Atletas de {} anos não tem categoria definida na tabela da CNN fornecida.'.format(anoint - anonascimento))