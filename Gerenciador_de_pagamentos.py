print('{:=^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque (10% de desconto)
[ 2 ] à vista cartão (5% de desconto)
[ 3 ] 2x no cartão (preço normal)
[ 4 ] 3x ou mais no cartão (20% de juros)''')

total = 0
opção = int(input('Qual é a opção? '))

if opção == 1:
    total = preco - (preco * 10 / 100)
elif opção == 2:
    total = preco - (preco * 5 / 100)
elif opção == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS.')
elif opção == 4:
    total_de_parcelas = int(input('Quantas parcelas? '))
    total = preco + (preco * 20 / 100)  
    parcela = total / total_de_parcelas
    print(f'Sua compra será parcelada em {total_de_parcelas}x de R${parcela:.2f} COM JUROS.')
else:
    print('OPÇÃO INVÁLIDA de pagamento. Por favor, execute o programa novamente.')
    total = 0 
    
if opção in [1, 2, 3, 4]:
    print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')