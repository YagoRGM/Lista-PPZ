distancia = float(input("Digite a distância (em km): "))
veloMedia = float(input("Digite a velocidade média (em km/h): "))

if veloMedia != 0:
    tempo = distancia / veloMedia
    print("Duração aproximada da viagem:", tempo, "horas")
else:
    print("Velocidade não pode ser zero.")