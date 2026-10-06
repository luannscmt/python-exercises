salario = float(input('salario: '))
vendas = float(input('vendas: '))

if vendas >= 5000:
    comissao = vendas * 0.10
    print(f'meta feita: comissão de {comissao}')
else:
    comissao = vendas * 0.02
    print(f'a meta nn foi feita: comissão de {comissao}')

total = salario + comissao

print(f'total: {total}')