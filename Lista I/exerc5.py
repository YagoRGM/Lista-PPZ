valor = float(input("Insira o valor em reais da mercadoria: "))
descontoPorcentagem = float(input("Insira o valor em % do desconto: "))

desconto = valor * descontoPorcentagem / 100
preco = valor - desconto

print ("Valor do desconto: R$:",desconto)
print ("Valor da mercadoria com o desconto aplicado: R$:",preco)