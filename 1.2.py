import math

# Função para calcular a área do círculo
def calcular_area(raio):
    return math.pi * (raio ** 2)

# Guarda o valor do raio do círculo
raio = float(input("Digite o valor do raio do círculo: "))

# Calcula a área do círculo
area = calcular_area(raio)

# Mostra o valor da área com quatro casas decimais
print(f"A área do círculo é: {area:.4f}")