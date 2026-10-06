peso = float(input('peso: '))

if peso <= 2:
    frete = 5.0
elif peso <= 10:
    frete = 12.0
else:
    frete = 20.0

entregarapida = int(input('quer envio rapido? SIM[1] NÃO[0]'))

print(f'frete: {frete}')

if entregarapida == 1:
    taxa = 15.0
else:
    taxa = 0.0

print(f'taxa entrega rapida: {taxa}')

total = frete + taxa

print(f'total: {total}')