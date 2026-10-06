valor = float(input('valor: '))

if valor > 150:
    desconto = valor * 0.10
elif valor >= 100:
    desconto = valor * 0.05
else:
    desconto = 0

total = valor - desconto

print(f'valor da compra: {valor}')
print(f'vc recebeu um desconto de: {desconto}')
print(f'total: {total}')
