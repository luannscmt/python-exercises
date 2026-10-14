horas = float(input('quantas horas vc dormiu? '))

if horas < 6:
    print('vc dormiu pouco')
elif horas <= 8:
    print('vc dormiu +/-')
else:
    print('vc dormiu muito')
