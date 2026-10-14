estoque = int(input("Digite o estoque inicial: "))
quantidade_retirada = 0
total_retirado = 0

while True:
    quantidade = int(input("Digite a quantidade que deseja retirar (0 para sair): "))

    if quantidade == 0:
        break
    elif quantidade < 0:
        print("Quantidade inválida!")
    elif quantidade > estoque:
        print("Não há produtos suficientes no estoque!")
    else:
        estoque = estoque - quantidade
        quantidade_retirada += 1
        total_retirado += quantidade
        print("Retirada realizada!")
        print("Estoque atual:", estoque)

print("\n--- Resumo do dia ---")
print("Retiradas realizadas:", quantidade_retirada)
print("Total de produtos retirados:", total_retirado)
print("Estoque final:", estoque)

if estoque <= 5:
    print("Atenção! É necessário solicitar uma nova compra.")