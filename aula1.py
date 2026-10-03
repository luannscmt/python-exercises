# divide o valor da contra entre as pessoas

conta = float(input('valor da conta: '))
pessoas = int(input('quantidade de pessoas: '))

if pessoas <= 0:
    print('só pode acima de uma pessoa')
else:
    valor = conta / pessoas
    print(f'cada pessoa deve pagar: {valor}')