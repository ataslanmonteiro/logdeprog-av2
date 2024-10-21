# Função para inserir os dados de um lançamento
def inserir_lancamento():
    codigo = input("Digite o ID do produto: ")
    quant = int(input("Digite a quantidade do produto: "))
    valor_unit = float(input("Digite o valor unitário do produto: "))
    return codigo, quant, valor_unit

# Inicia a variável que irá guardar o valor total a ser pago
valor_total = 0

# Captura os dados de 5 lançamentos
for i in range(5):
    print(f"Lançamento do produto {i+1}")
    codigo, quant, valor_unit = inserir_lancamento()
    valor_total += quant * valor_unit
    print(f"Subtotal após lançamento do produto {i+1}: R$ {valor_total:.2f}\n")

# Mostra o valor total a ser pago após os 5 lançamentos
print(f"Valor total a ser pago: R$ {valor_total:.2f}")

    
