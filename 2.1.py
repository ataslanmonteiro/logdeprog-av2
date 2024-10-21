# Tabela de produtos
produtos = {
    1: "Cachorro Quente",
    2: "X-Salada",
    3: "X-Bacon",
    4: "Torrada Simples",
    5: "Refrigerante"
}

# Tabela de preços
precos = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}

# Função para guardar os dados de um pedido
def inserir_pedido():
    codigo = int(input("Digite o código do item: "))
    quant = int(input("Digite a quantidade do item: "))
    return codigo, quant

# Guarda o pedido
codigo, quant = inserir_pedido()

# Calcula o valor total do pedido
if codigo in produtos:
    valor_total = precos[codigo] * quant
    print(f"Item: {produtos[codigo]}")
    print(f"Quantidade: {quant}")
    print(f"Valor total a pagar: R$ {valor_total:.2f}")
else:
    print("Código de item inválido.")

