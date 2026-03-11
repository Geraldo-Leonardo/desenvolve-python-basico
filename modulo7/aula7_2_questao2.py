
# Solicita ao usuário inserir uma frase
frase = input("Digite uma frase: ")
frase = frase.lower()
#print("Frase original com teste lower:", frase)    # Teste para verificar se a frase foi convertida para minúscula

# Define as vogais a serem substituídas
vogais = "aeiou"
# Substituir as vogais por "*"
frase_modificada = ""
for vogal in frase:
    if vogal in vogais:
        frase_modificada += "*"
    else:
        frase_modificada += vogal
# Exibe a frase modificada
print()
print("Frase modificada:", frase_modificada)
print()

