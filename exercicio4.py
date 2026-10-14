nomes = []
quantidades = []

for i in range(5):
    nome = input(f"Nome do produto {i + 1}: ")
    quantidade = int(input("Quantidade contada: "))
    nomes.append(nome)
    quantidades.append(quantidade)

print("\n--- Inventário ---")
total = 0
maior = quantidades[0]
posicao_maior = 0

for i in range(5):
    if quantidades[i] < 10:
        situacao = "(REPOR)"
    else:
        situacao = "(OK)"
    print(f"{nomes[i]}: {quantidades[i]} {situacao}")

    total += quantidades[i]

    if quantidades[i] > maior:
        maior = quantidades[i]
        posicao_maior = i

print("Total de unidades:", total)
print(f"Maior estoque: {nomes[posicao_maior]} ({maior})")