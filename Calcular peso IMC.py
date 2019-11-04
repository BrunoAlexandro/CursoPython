peso = int(input('Digite o peso do paciente: '))
altura = float(input('Digite a altura do paciente: '))

imc = (peso / altura **2)

print(f'O IMC do paciênte é de {imc:.2f}')

if imc <= 18.5:
    print('Você está abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal.')
elif imc >= 40:
    print('Você está obeso.')
elif imc >= 25:
    print('Você está em sobrepeso.')
