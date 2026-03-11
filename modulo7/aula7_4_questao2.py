
import re

# Lê o conteúdo do arquivo "texto.txt"
with open("frase.txt", "r") as file:
    content = file.read()

# Remove espaços em branco e caracteres não alfabéticos, e separa cada palavra em uma linha
words = re.findall(r'\b\w+\b', content)

# Salva as palavras em um novo arquivo "palavras.txt"
with open("palavras.txt", "w") as file:
    for word in words:
        file.write(word + "\n")

# Imprime o conteúdo do arquivo "palavras.txt"
with open("palavras.txt", "r") as file:
    print(file.read())






