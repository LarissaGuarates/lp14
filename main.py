from conversor import valor_pol

valor_cm = int(input('Insira o valor em centímetros: '))

file = open('Arquivo', 'w+')
file.write(
    f'o valor {valor_cm} em centímetros corresponde a {valor_pol(valor_cm)} valor em polegadas.'
)
file.seek(0, 0)
print(file.read())
file.close()
print('nova versao do codigo')