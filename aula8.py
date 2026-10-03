refri = 6
quantidade = int(input('quantos refrigerante quer comprar? '))
total = refri * quantidade

if total > 30:
    print(f'total: R${total}')
    print('compra grande')
else:
    print(f'total: R${total}')
    print('compra pequena')