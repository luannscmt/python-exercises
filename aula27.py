ingressos = int(input('quantos ingressos? '))
pipoca = input('quer pipoca? ')

total = ingressos * 20

if pipoca == 'sim':
    total = total + 12

print(f'total: {total}')

if total > 50:
    print('vc gastou mais de 50 reais')
else:
    print('gastou menos q 50 reais')
