
# Abrindo o arquivo para leitura
with open("estomago.txt", "r", encoding="utf-8") as file:
    
    # Lendo todas as linhas do arquivo
    lines = file.readlines()
    
    # Imprimindo as primeiras 25 linhas    
    print("Primeiras 25 linhas:")
    for line in lines[:25]:
        print(line.strip())
    
    # Imprimindo o número de linhas do arquivo    
    print(f"\nNúmero de linhas do arquivo: {len(lines)}")
    
    # Encontrando a linha com maior número de caracteres    
    longest_line = max(lines, key=len)    
    print(f"\nLinha com maior número de caracteres: {longest_line.strip()}")
    
    # Contando as menções aos personagens "Nonato" e "Íria"    
    nonato_count = sum(line.lower().count("nonato") for line in lines)   
    iria_count = sum(line.lower().count("íria") for line in lines)   
    
    print(f"\nNúmero de menções a 'Nonato': {nonato_count}")   
    print(f"Número de menções a 'Íria': {iria_count}")

