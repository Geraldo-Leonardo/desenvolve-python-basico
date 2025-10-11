"""
1 - Faça um programa para ler as dimensões de um terreno em inteiros 
(comprimento e largura), bem como o preço do metro quadrado da região 
em ponto flutuante. Calcule o valor do terreno e imprima o resultado 
como mostra o exemplo a seguir:

O terreno possui 250m2 e custa R$512,490.50
Comente na linha acima de cada instrução uma breve descrição da instrução.
Fórmulas:

area_m2 = comprimento * largura
preco_total = preco_m2 * area_m2

"""

# Lê o comprimento do terreno em metros
comprimento = int(input("Digite o comprimento do terreno em metros: "))
# Lê a largura do terreno em metros
largura = int(input("Digite a largura do terreno em metros: "))
# Lê o preço do metro quadrado em ponto flutuante
preco_m2 = float(input("Digite o preço do metro quadrado: "))
# Calcula a área do terreno em metros quadrados
area_m2 = comprimento * largura
# Calcula o preço total do terreno
preco_total = preco_m2 * area_m2
# Imprime o resultado formatado com duas casas decimais
print()
print(f"Comprimento do terreno: {comprimento} metros")
print(f'Largura do terreno: {largura} metros')
print(f'Área total do terreno: {area_m2}m2')
print(f'Preço por m2: {preco_m2 :.2f}')
print()
print(f"O terreno possui {area_m2}m2 e custa R${preco_total :,.2f}")
print()