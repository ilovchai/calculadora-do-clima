tempMediaAnual = 0
mesEscaldante = -90
qntdMesesEscaldantes = 0
mesMenosQuente = 60
meses = 12
menosQuenteNome = ''
maisQuenteNome = ''
mesesExtenso = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

for mes in range(1,13):
    mesNum = int(input('insira um numero de 1 a 12: '))
    while mesNum<=0 or mesNum>12:
        print('>> mes invalido! insira um numero de 1 a 12')
        mesNum = int(input('> insira novamente um mes de 1 a 12: '))

    temp = float(input(f'insira a temperatura do mês {mesNum}: '))
    while temp<=-90 or temp>60:
        print('>> temperatura invalida!')
        temp = float(input(f'> insira novamente a temperatura maxima do mês {mesNum}: '))
    
    # CONTA QUANTIDADE DE MESES ESCALDANTES
    if temp >= 40:
        qntdMesesEscaldantes += 1

    # MOSTRA OS NOMES POR EXTENSO
    nomeExtenso = mesesExtenso[mes - 1]

    # VERIFICA MES MENOS QUENTE
    if temp < mesMenosQuente:
        mesMenosQuente = temp
        menosQuenteNome = nomeExtenso

    # VERIFICA MES ESCALDANTE
    if temp > mesEscaldante:
        mesEscaldante = temp
        maisQuenteNome = nomeExtenso

    # CALCULA MEDIA MAXIMA ANUAL
    tempMediaAnual += temp

mediaAnual = tempMediaAnual / meses

    # OBSERVAÇÃO: prints vazios para maior legibilidade dos dados
print()
print(f'temperatura média máxima anual: {mediaAnual:.2f}°C')
print()
print(f'meses escaldantes (temperatura acima de ou igual a 40°C): {qntdMesesEscaldantes}')
print()
print(f'mês mais escaldante: {maisQuenteNome}')
print()
print(f'mês menos quente: {menosQuenteNome}')


