boletim = ['ciencias:', 1, 'portugues:', 3, 'matematica:', 5]
resulta = ['Aprovado', 'Reprovado', 'Recuperação']
while True:
    nome = str(input('Nome do aluno: '))
    ciencias = float(input('Nota de Ciências: '))
    boletim[1] = ciencias
    portugues = float(input('Nota de Português: '))
    boletim[3] = portugues
    matematica = float(input('Nota de Matemática: '))
    boletim[5] = matematica
    media = (ciencias + portugues + matematica) / 3
    if media >= 7:
        resultado = resulta[0]
    elif 5 <= media <= 6.9:
        resultado = resulta[2]
    else:
        resultado = resulta[1]
    print(f'Nome: {nome}')
    print(boletim)
    print(resultado)