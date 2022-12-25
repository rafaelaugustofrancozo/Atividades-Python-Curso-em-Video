rom datetime import date, datetime
#print('==========VERIFICAÇÃO DE IDADE PARA ALISTAMENTO MILITAR==========')
#datanascimento = str(input('Digite sua data de nascimento(dd/mm/aaaa: '))
#datanascimentoconvertida = datetime.strptime(datanascimento,'%d/%m/%Y')#só não usei o metodo date direto, porque ele não tem a strptime, que converte string pra datetime
#datahoje = date.today()
#idadeemanos = (datahoje - datanascimentoconvertida.date()) / 365
#if idadeemanos < 18:
#    print('Você ainda não tem 18 anos para se alistar.')
#elif idadeemanos == 18:
#    print('Você está em idade de alistamento!')
#elif idadeemanos >= 19:
#    print('Você já passou da idade de se alistar, e está atrasado {} ano(s)'.format(idadeemanos-18))

####RALEI ATOA AI EM CIMA, O EXERCICIO É MAIS SIMPLES
from datetime import date, datetime
print('\033[0;32;32m==========VERIFICAÇÃO DE IDADE PARA ALISTAMENTO MILITAR==========\033[m')
anonasc = int(input('Digite o ano de nascimento: '))
anoatual = 2022
anoauto = date.today().year
if (anoatual - anonasc) < 18:
    print('VOCÊ NASCEU EM {}, E TEM {} ANOS, PORTANTO AINDA NÃO PRECISA SE ALISTAR.\n VOCÊ DEVERÁ SE ALISTAR EM {}.'.format(anonasc, anoatual-anonasc, anoatual + (18-(anoatual-anonasc))))
elif (anoatual -anonasc) == 18:
    print('ESTÁ NA HORA DE ALISTAR!!!!!')
else:
    print('VOCÊ ESTÁ ATRASADO, POIS TEM {} ANOS, E JÁ DEVERIA TER SE ALISTADO!'.format(anoatual-anonasc))