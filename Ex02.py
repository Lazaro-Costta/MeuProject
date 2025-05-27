total = 0
mais1k = 0
cont = 0
primeiro = 0
barato = ' '
while True:
    nome = str(input('nome do produto:'))
    preço = float(input('preço:'))
    continuar = ' '
    total += preço
    cont += 1
    if cont == 1:
        barato = nome
        primeiro = preço
    else:
        if preço < primeiro:
            barato = nome
            primeiro = preço
    if preço >= 1000:
        mais1k += 1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]:')).lstrip().upper()[0]
    if continuar == 'N':
        break
print(f'Total gasto na compra foi R${total:.2f}')
print(f'Total de {mais1k} produtos custaram mais de R$:1000')
print(f'O produto mais barato foi {barato} que custou R$:{primeiro:.2f}')