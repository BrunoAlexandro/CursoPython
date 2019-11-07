import math
salario = float(input('Digite o salário do trabalhador: '))
minimo = salario + (salario * 10 / 100)
maximo = salario + (salario * 15 / 100)


if salario <= 1250:
    print(f'O aumento deste funcionário ficará no total de {minimo}R$ (10%)')
else:
    print(f'O aumento deste funcionário ficará no total de {maximo}R$ (15%)')

