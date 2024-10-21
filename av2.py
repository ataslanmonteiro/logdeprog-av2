# Função para inserir os dados de cada lançamento
def inserir_lancamento():
    codigo = input("Digite o código de ID do produto: ")
    quant = int(input("Digite a quantidade do produto: "))
    valor_unit = float(input("Digite o valor unitário do produto: "))
    return codigo, quant, valor_unit

#Inicia a variável que irá guardar o valor total a ser pago
valor_total = 0

#Insere os dados de 5 lançamentos
for i in range(5):
    print(f"Lançamento {i+1}")
    codigo, quant, valor_unit = inserir_lancamento()
    valor_lancamento += quant * valor_unit
    valor_total += valor_lancamento
    print(f"Valor do lançamento {i+1}: R$ {valor_lancamento:.2f}")
    print(f"Subtotal após lançamento {i+1}: R$ {valor_total:.2f}\n")

# Mostra o valor total da soma dos 5 lançamentos
print(f"Soma total dos 5 lançamentos: R$ {valor_total:.2f}")
    