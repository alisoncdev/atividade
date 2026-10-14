def contar_abaixo(quantidades, minimo):
    contador = 0
    for i in range(len(quantidades)):
        if quantidades[i] < minimo:
            contador += 1
    return contador
produtos = ["Luva de vaqueta", "Óculos de proteção", "Disco de corte", "Lixa grão 120", "Fita isolante"]
estoque = [12, 3, 0, 25, 7]
minimo = 8
for i in range(len(produtos)):
    print(produtos[i], ":", estoque[i])
faltando = contar_abaixo(estoque, minimo)
print("Itens abaixo do mínimo:", faltando)