quantidade = int(input('quantos combos de lanche? '))

while quantidade < 1:
    print('tem q ser maior q zero')
    quantidade = int(input('denovo diga quantos combos: '))

total = quantidade * 25

if quantidade >= 3:
    desconto = 10
else:
    desconto = 0

final = total - desconto

print(f'total: {total}')
print(f'desconto: {desconto}')
print(f'valor final: {final}')