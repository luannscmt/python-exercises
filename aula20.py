km = float(input('quantos km? '))

if km < 3:
    print('corrida ruim')
elif km <= 7:
    print('boa corrida')
else:
    print('corrida muito boa')

print(f'vc correu {km} km')