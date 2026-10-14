consumo = float(input('consumo de agua: '))

if consumo <= 10:
    conta = 30
elif consumo <= 20:
    conta = 50
else:
    conta = 80

print(f'valor da conta: {conta}')
