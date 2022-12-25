nome = str(input('Qual é o seu nome: '))
if nome == 'Rafael':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal...')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1+n2)/2
print('A sua média foi {:.2f}'.format(m))
if m >= 7:
    print('Você está aprovado, parabens!')
else:
    print('Você está de recuperação.')

#if simplificado
print('Você está aprovado, parabens!' if m>=7 else 'Você está de recuperação.')