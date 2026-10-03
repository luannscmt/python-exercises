pontos = int(input('quantos pontos vc fez? '))

if pontos < 100:
    print('continue treinando')
elif pontos > 100 and pontos <= 499:
    print('boa pontuação')
elif pontos >= 500:
    print('pontuação execelente')
