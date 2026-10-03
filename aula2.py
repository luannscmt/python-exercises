# Classifica a pessoa de acordo com a idade

idade = int(input('diga sua idade: '))

if idade < 12:
    print('criança')
elif idade <= 17:
    print('adolescente')
elif idade <= 59:
    print('adulto')
else:
    print('idoso')