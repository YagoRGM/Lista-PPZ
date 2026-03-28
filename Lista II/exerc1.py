a = int(input("Digite o 1º número: "))
b = int(input("Digite o 2º número: "))
c = int(input("Digite o 3º número: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Triângulo equlátero")
    elif a == b or a == c or b == c: 
        print("Triângulo isósceles")
    elif a != b and a != c and b != c: 
        print("Triângulo escaleno")
else:
    print("Esses três número não podem formar um triângulo")