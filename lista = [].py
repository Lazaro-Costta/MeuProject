lista = []
pares = []
ímpares = []
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        ímpares.append(n)
    c = str(input('Quer continuar? [S/N]:')).lstrip().upper()[0]
    if c == 'N':
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')