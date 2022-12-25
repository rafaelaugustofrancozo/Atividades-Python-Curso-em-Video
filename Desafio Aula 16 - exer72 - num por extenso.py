tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito'
         , 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num not in range(0,21):
        print('Número inválido. Tente novamente.')
    print(f'Voce digitou o número {tupla[num]}!')
    continua = ' '
    while continua not in ('SN'):
        continua = str(input('Deseja mais números?(S/N) ')).strip().upper()[0]
    if continua == 'N':
        break
print('FIM')
