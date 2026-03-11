
# Criando o arquivo CSV e escrevendo os dados dos livros
with open("meus_livros.csv", "w") as arquivo:
    # Escrevendo os títulos das colunas da planilha
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")
    
    # Escrevendo os dados dos livros
    arquivo.write("O Caçador de Pipas,Khaled Hosseini,2003,368\n")
    arquivo.write("Torto Arado,Itamar Vieira Junior,2019,264\n")
    arquivo.write("1984,George Orwell,1949,328\n")
    arquivo.write("Dom Casmurro,Machado de Assis,1899,256\n")
    arquivo.write("O Alquimista,Paulo Coelho,1988,208\n")
    arquivo.write("A Menina que Roubava Livros,Markus Zusak,2005,552\n")
    arquivo.write("Cem Anos de Solidão,Gabriel García Márquez,1967,417\n")
    arquivo.write("O Senhor dos Anéis,J.R.R. Tolkien,1954,1216\n")
    arquivo.write("A Guerra dos Tronos,George R.R. Martin,1996,694\n")
    arquivo.write("O Pequeno Príncipe,Antoine de Saint-Exupéry,1943,96\n")















