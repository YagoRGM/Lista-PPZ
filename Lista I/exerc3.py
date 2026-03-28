dia = int(input("Insira a quantidade de dias: "))
hora = int(input("Insira a quantidade de horas: "))
minutos = int(input("Insira a quantidade de minutos: "))
segundos = int(input("Insira a quantidade de segundos: "))

conversaoDias = dia * 86400
conversaoHora = hora * 3600
conversaoMinutos = minutos * 60

totalSegundos = conversaoDias + conversaoHora + conversaoMinutos + segundos
print ("Total de segundos: ",totalSegundos,"segundos")