n = int(input("Quantas entradas foram registradas hoje? "))

total = 0
maior = 0

for i in range(1, n + 1):
    qtd = int(input(f"Quantidade da entrada {i}: "))
    total = total + qtd

    if qtd > maior:
        maior = qtd

print("Total recebido:", total, "unidades")
print("Maior entrada:", maior, "unidades")

if n > 0:
    print("Média por entrada:", round(total / n, 2))