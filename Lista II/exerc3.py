peso = float(input("Digite o peso do peixe: "))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f"Excesso de peso: {excesso:.2f}Kg, multa: R$: {multa:.2f}")
else:
    excesso = 0
    multa = 0
    print(f"Excesso de peso: {excesso:.2f}Kg, multa: R$: {multa:.2f}")