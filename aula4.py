# Compara dois números e mostra a diferença entre eles

numero1 = float(input('primeiro numero: '))
numero2 = float(input('segundo numero: '))

if numero1 > numero2:
    print(f'o primeiro número é maior')
elif numero2 > numero1:
    print(f'o segundo número é maior')
else:
    print(f'os numeros são iguais')

print(f"diferença: {numero1 - numero2}")