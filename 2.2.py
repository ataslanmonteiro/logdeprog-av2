import math

# Função para calcular as raízes usando a fórmula de Baskara
def calcular_raizes(a, b, c):
    if a == 0:
        return "Impossível calcular: O valor de 'a' não pode ser zero."
    
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        return "Impossível calcular: O valor de 'delta' não pode ser negativo"
    
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)

    return raiz1, raiz2

# Captura os coeficientes da equação
try:
    a = float(input("Digite o valor de 'a': "))
    b = float(input("Digite o valor de 'b': "))
    c = float(input("Digite o valor de 'c': "))
except ValueError:
    print("Erro: Todos os coeficientes devem ser números válidos.")
else:
    # Calcular as raizes
    resultado = calcular_raizes(a, b, c)

    # Mostra o resultado
    if isinstance(resultado, str):
        print(resultado)
    else:
        raiz1, raiz2 = resultado
        print(f"As raízes da equação são:")
        print(f" x1 = {raiz1:.5f}")
        print(f" x2 = {raiz2:.5f}")


