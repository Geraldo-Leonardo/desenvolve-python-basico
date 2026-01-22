

# Lista de números pares entre 20 e 50
pares = [x for x in range(20, 51) if x % 2 == 0]
print()
print("Números pares entre 20 e 50:", pares)

# Lista de quadrados de 1 a 9
quadrados = [x**2 for x in range(1, 10)]
print("\nQuadrados dos números de1 a 9:", quadrados)

# Lista de números divisíveis por 7 entre 1 e 100
divisiveis_por_7 = [x for x in range(1, 101) if x % 7 == 0]
print("\nNúmeros divisíveis por 7 entre 1 e 100:", divisiveis_por_7)

# Lista de par ou ímpar para valores em range(0,30,3)
paridade = ['par' if x % 2 == 0 else 'ímpar' for x in range(0, 30, 3)]
print("\nImprima par ou ímpar para valores em range(0,30,3):", paridade)
print()