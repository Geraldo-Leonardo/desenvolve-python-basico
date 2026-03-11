
def encontrar_anagramas(frase, palavra_objetivo):
    # Normaliza a palavra objetivo para comparação
    palavra_objetivo = palavra_objetivo.lower()
    sorted_objetivo = sorted(palavra_objetivo)
    
    # Divide a frase em palavras
    palavras = frase.split()
    
    anagramas = []
    
    for palavra in palavras:
        # Normaliza a palavra atual para comparação
        palavra_normalizada = palavra.lower()
        if sorted(palavra_normalizada) == sorted_objetivo:
            anagramas.append(palavra)
    
    return anagramas

# Entrada do usuário
frase = input("\nDigite uma frase: ")
palavra_objetivo = input("\nDigite a palavra objetivo para encontrar os anagramas: ")

anagramas = encontrar_anagramas(frase, palavra_objetivo)

print(f"\nAnagramas encontrados : {anagramas}")
print()