def quantidade_a_pedir(atual, minimo, maximo):
    if atual <= minimo:
        return maximo - atual
    else:
        return 0
itens_solicitacao = 0
valor_total = 0

for i in range(3):
    nome = input(f"Produto {i + 1}: ")
    atual = int(input("Estoque atual: "))
    minimo = int(input("Estoque mínimo: "))
    maximo = int(input("Estoque máximo: "))
    preco = float(input("Preço unitário: "))

    quantidade = quantidade_a_pedir(atual, minimo, maximo)

    if quantidade > 0:
        subtotal = quantidade * preco
        print(f">> Pedir {quantidade} de {nome} = R$ {subtotal:.2f}")

        itens_solicitacao += 1
        valor_total += subtotal
    else:
        print(f">> {nome}: estoque OK")
        
print("\n--- Solicitação de compra ---")
print("Itens na solicitação:", itens_solicitacao)
print(f"Valor total: R$ {valor_total:.2f}")