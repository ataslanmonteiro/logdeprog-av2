# Lê o valor de N
N = int(input("Digite a quantidade de valores inteiros a serem lidos: "))

# Inicia contadores
in_count = 0
out_count = 0

# Loop pra ler os valores inteiros X
for _ in range(N):
    X = int(input("Digite um valor inteiro: "))
    if 10 <= X <= 20:
        in_count += 1
    else:
        out_count += 1

# Mostra os resultados
print(f"{in_count} in")
print(f"{out_count} out")
