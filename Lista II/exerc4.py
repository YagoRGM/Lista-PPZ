a = int(input("Digite o 1º número: "))
b = int(input("Digite o 2º número: "))
c = int(input("Digite o 3º número: "))

if a >= b and a >= c:
    maior = a
elif b >= a and b >= c:
    maior = b
else:
    maior = c

print(f"O maior número é: {maior}")