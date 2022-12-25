print('\033[0;35;35m==========CÁLCULO DE MÉDIA DE NOTAS==========\033[m')
nome = str(input('DIGITE O NOME DO ALUNO: '))
nome.strip()
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2
if media < 5:
    print('ALUNO: {}\nMÉDIA FINAL: {}\nSTATUS: \033[0;31;31mREPROVADO!\033[m'.format(nome, media))
elif media >=5 and media <= 6.9:
    print('ALUNO: {}\nMÉDIA FINAL: {}\nSTATUS: \033[0;33;33mEM RECUPERAÇÃO\033[m'.format(nome, media))
else:
    print('ALUNO: {}\nMÉDIA FINAL: {}\nSTATUS: \033[0;32;32mAPROVADO! PARABÉNS!\033[m'.format(nome, media))