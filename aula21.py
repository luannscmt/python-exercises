tamanho = int(input('escolha um tamanho: [1][2][3]'))

if tamanho == 1:
    print('pizza pequena')
    print('preço: R$20')
elif tamanho == 2:
    print('pizza média')
    print('preço: R$30')
elif tamanho == 3:
    print('pizza grande')
    print('Preço: R$40')
else:
    print('tamanho invalido')