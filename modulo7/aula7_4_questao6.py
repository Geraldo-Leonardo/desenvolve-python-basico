
# Abrindo o arquivo para leitura
with open("spotify-2023.csv", "r", encoding='latin-1') as arquivo:
    # Lendo as linhas do arquivo
    linhas = arquivo.readlines()
    
# Criando uma lista para armazenar as músicas mais tocadas de cada ano
musicas_mais_tocadas = []

# Iterando sobre as linhas do arquivo, ignorando a primeira linha (cabeçalho)
for linha in linhas[1:]:

    # Verificando se a linha contém aspas, o que indica que é uma linha a ser ignorada
    if '"' in linha:
        continue
    
    # Dividindo a linha em colunas usando a vírgula como separador
    colunas = linha.strip().split(',')
    
    # Extraindo as informações relevantes
    track_name = colunas[0]
    artist_name = colunas[1]
    released_year = int(colunas[3])
    streams = colunas[8]
    
    # Verificando se o ano de lançamento está entre 2012 e 2022
    if 2012 <= released_year <= 2022:
        # Adicionando a música à lista de músicas mais tocadas
        musicas_mais_tocadas.append([track_name, artist_name, released_year, streams])

# Criando um dicionário para armazenar a música mais tocada de cada ano
musica_mais_tocada_por_ano = {}
for musica in musicas_mais_tocadas:
    track_name, artist_name, released_year, streams = musica
    
    if released_year not in musica_mais_tocada_por_ano:
        musica_mais_tocada_por_ano[released_year] = musica
        
    else:
        if streams > musica_mais_tocada_por_ano[released_year][3]:
            musica_mais_tocada_por_ano[released_year] = musica
               
# Criando uma lista com as músicas mais tocadas de cada ano
musicas_mais_tocadas_por_ano = list(musica_mais_tocada_por_ano.values())

# Imprimindo a lista de músicas mais tocadas de cada ano
print()
for musica in musicas_mais_tocadas_por_ano:
    print(musica)
print()