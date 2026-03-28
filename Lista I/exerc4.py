salarioVelho = float(input("Insira o valor em reais do seu salário atual: "))
aumentoPorcentagem = float(input("Insira o valor em % do seu futuro aumento: "))

aumento = salarioVelho/100 * aumentoPorcentagem
salarioNovo = salarioVelho + aumento

print ("Valor do aumento: R$:",aumento)
print ("Valor do salário com o aumento aplicado: R$:",salarioNovo)