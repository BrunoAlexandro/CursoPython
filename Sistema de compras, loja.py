print('='*10, 'Sistema de lojas', '='*10)
preco = int(input('Digite o valor da compra: '))
print('FORMAS DE PAGAMENTO')
print(' [1] Dinheiro/Cheque', '\n',
      '[2] A vista no cartão', '\n',
      '[3] 2x no cartão', '\n',
      '[4] 3x no cartão')
opcao = int(input('Digite a opção que deseja: '))

dinheiro = (preco * 0.90)
cartao_avista = (preco * 0.95)
cartao_3x = (preco * 1.20)

if opcao == 1:
    print(f'O valor de {preco:.2f}R$ no dinheiro ou cheque fica {dinheiro:.2f}R$ com 10% de desconto.')
elif opcao == 2:
    print(f'O valor à vista no cartão fica {cartao_avista:.2f}R$ com 5% de desconto.')
elif opcao == 3:
    print(f'O valor em até 2x no cartão é de {preco:.2f}R$, sem juros.')
elif opcao == 4:
    print(f'O valor em até 3x no cartão é de {cartao_3x:.2f}R$, com 20% de juros.')


