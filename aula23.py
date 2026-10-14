quantidade = int(input('quantas camisa? '))

if quantidade < 1:
    print('vc precisa comprar pelo menos 1 camisa')
else:
    preco = 35
    original = quantidade * preco

    if quantidade >= 5:
        desconto = original * 0.10
    else:
        desconto = 0

    final = original - desconto

    print(f'preço original: R${original}')
    print(f'desconto: R${desconto}')
    print(f'preço final: R${final}')
