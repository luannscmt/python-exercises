produto = input('produto: ')
quantidade = int(input('quantidade no estoque'))
minimo = int(input('estoque minimo: '))

if quantidade < minimo:
    faltam = minimo - quantidade

    print(f'o estoque de {produto} ta baixo')
    print(f'precisa de {faltam} pra atingir o minimo')
else:
    print(f'o estoque de {produto} ta normal')