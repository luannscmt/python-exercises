pontos = int(input('fez quantos pontos? '))

if pontos < 50:
    print('sem medalha')
elif pontos < 80:
    print('medalha de bronze')
elif pontos < 100:
    print('medalha de prata')
else:
    print('medalha de ouro')
