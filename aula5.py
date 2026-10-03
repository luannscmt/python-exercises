# Verifica a porcentagem da bateria do celular

bateria = int(input('bateria: '))

if bateria == 100:
    print('celular ta carregado')
elif bateria <= 15:
    print('bateria acabando')
    print('coloca o celular pra carregar')
elif bateria <= 50:
    print('bateria media')
else:
    print("bateria boa")