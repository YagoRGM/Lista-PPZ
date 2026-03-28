metrosquad = float(input("Metros quadrados a serem pintados: "))
litros = metrosquad / 3
latas = litros / 18

if latas % 1 != 0:
    latas = int(latas) + 1
else:
    latas = int(latas)

preco = latas * 80
print("Quantidade de latas a serem compradas:", latas)
print(f"Preço total a ser pago: R$ {preco:.2f}")

#edvwfuyeiwfdysgvhwbjieuygfbhd