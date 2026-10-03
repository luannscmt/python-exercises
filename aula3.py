# Calcula o frete e o valor total da compra

compra = float(input('valor da compra: '))

if compra >= 200:
    frete = 0
    total = frete + compra
    print('frete gratis')
    print(f'total: {total}')
else:
    frete = 15
    total = frete + compra
    print(f'frete: {frete}')
    print(f'total: {total}')