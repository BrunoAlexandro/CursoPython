idade = int(input('Digite a idade: '))

if idade <= 17:
    print('Esta pessoa precisará se alistar ainda.')
elif idade == 18:
    print('Esta pessoa necessita se alistar imediatamente.')
elif idade >= 18:
    print('Já passou o tempo de alistamento.')