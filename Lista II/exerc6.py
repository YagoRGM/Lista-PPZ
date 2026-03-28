salarioHora = int(input("Valor do salário por hora:  "))
horasTrabalhadas = int(input("Número de horas trabalhadas no mês:  "))
salariobruto = salarioHora * horasTrabalhadas

print("Seu salário bruto é: ",salariobruto)
imposto = salariobruto * 0.11
inss = salariobruto * 0.08
sindicato = salariobruto * 0.05

print("O valor do imposto é: ",imposto)
print("O valor do INSS é: ",inss)
print("O valor do sindicato é: ",sindicato)
salarioliquido = salariobruto - imposto - inss - sindicato
print("O valor do salário líquido é: ",salarioliquido)