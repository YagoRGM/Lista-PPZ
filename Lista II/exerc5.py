a = int(input("Digite o 1º número: "))
b = int(input("Digite o 2º número: "))
c = int(input("Digite o 3º número: "))

if a >= b and a >= c:
    if b >= c:
        maior = a
        menor = c
    elif c >= b:
        maior = a
        menor = b
                    
elif b >= a and b >= c:
    if a >= c:
        maior = b
        menor = c
    elif c >= a:
        maior = b
        menor = a
        
elif c >= a and c >= b:
    if a >= b:
        maior = c
        menor = b
    elif c >= a:
        maior = c
        menor = a

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")