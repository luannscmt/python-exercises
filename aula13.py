# sistema de passagem de onibus

idade = int(input('digite sua idade: '))

if idade < 0:
    print('idade invalida')
elif idade >= 60:
    passagem = 5 / 2
    print(f'valor da passagem: R${passagem}')
else:
    passagem = 5
    print(f'valor da passagem: R${passagem}')