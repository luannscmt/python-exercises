# diz se quem gnhou foi o time 1 ou 2

time1 = int(input('Quantos gols o time 1 fez? '))
time2 = int(input('Quantos gols o time 2 fez? '))

if time1 > time2:
    print(f'Time 1 venceu')
elif time2 > time1:
    print(f'Time 2 venceu')
else:
    print('empate')