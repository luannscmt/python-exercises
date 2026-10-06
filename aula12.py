# sitema de aluguel de bike

horas = int(input("quantas horas? "))

preco = horas * 10

if horas >= 5:
    desconto = 10
else:
    desconto = 0

total = preco - desconto

print(f'preço: R${preco}')
print(f'desconto: R${desconto}')
print(f'total: R${total}')