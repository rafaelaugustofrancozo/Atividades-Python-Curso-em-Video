c = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c+= 1
    s+= n
print(f'\033[0;33;33mTotal de número digitados:\033[m {c}\n'
      f'\033[0;33;33mResultado da soma:\033[m {s}')