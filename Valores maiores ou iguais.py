valor_um = int(input('Digite o primeiro valor: '))
valor_dois = int(input('Digite o segundo valor: '))

if valor_um == valor_dois:
    print('Os valores são iguais')
elif valor_um <= valor_dois:
    print('O segundo valor é o maior')
elif valor_um >= valor_dois:
    print('O primeiro valor é maior.')
