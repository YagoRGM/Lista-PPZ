cigarros = int(input('Quantos cigarros você fuma por dia: '))
anos = int(input('Por quantos anos você fuma: '))

total_cigarros = cigarros * (anos * 365)
total_minutos = total_cigarros * 10
dias_perdidos= total_minutos / 1440

print('Você já perdeu', dias_perdidos, 'dias de vida')