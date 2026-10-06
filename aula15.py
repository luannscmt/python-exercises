idade = int(input('idade: '))

if idade < 18:
    print('nao pd entrar, precisa ser de maior')
else:
    tipo = int(input('tipo de bilhete: VIP[1] NORMAL[2]'))

    if tipo == 1:
        valor = 100
        print('bilhete vip slecionado')
        print(f'total: {valor}')
    elif tipo == 2:
        valor = 50
        print('bilhete normal selecionado')
        print(f'total: {valor}')
    else:
        print('tipo invalido')