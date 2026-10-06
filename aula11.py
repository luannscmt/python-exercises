macas = int(input('qantas maçã você quer? '))

total = macas * 2

if macas >= 10:
    desconto = 5
else:
    desconto = 0

valor_final = total - desconto

print(f'total: R${total}')
print(f'desconto: R${desconto}')
print(f'valor final: R${valor_final}')