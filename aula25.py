quantidade = int(input('quantos jogos quer? '))

if quantidade < 1:
    print('quantidade invalida')
else:
    total = quantidade * 60

    if quantidade >= 2:
        desconto = 15
    else:
        desconto = 0

    final = total - desconto

    print(f'preço original: R${total}')
    print(f'desconto: R${desconto}')
    print(f'preço final: R${final}')
