kmRodado = float(input('Digite a quantidade de quilômetros rodados com o carro alugado: '))
diasAlugado = float(input('Digite a quantidade de dias que você passou com o carro alugado: '))

calculoDia = diasAlugado * 60
calculoKm = kmRodado * 0.15
custoGeral = calculoDia + calculoKm

print('O custo total que você precisa pagar com o aluguel deste veículo é: R$',custoGeral)