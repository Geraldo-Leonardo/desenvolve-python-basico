
frase = input("Digite uma frase: ")
vogais = "aeiou"
contagem = 0
indices = []
for i, letra in enumerate(frase.lower()):
    if letra in vogais:
        contagem += 1
        indices.append(i)
        #print(f"Vogal '{letra}' encontrada no índice {i}.")     # Linha de teste para verificar iteração, opcional
print(f"\n{contagem} vogais.")

print("\nÍndices", indices)