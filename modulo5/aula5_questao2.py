"""
Escreva um código que gere n valores inteiros aleatórios entre 0 e 100 e calcule a raíz 
quadrada da soma dos valores. Peça ao usuário o valor de n

Biblioteca random: Função randint()

Biblioteca math:  Função sqrt()
"""
import random
import math
# Solicitar ao usuário a quantidade de números aleatórios a serem gerados
quantidade_n_aleatorios = int(input("Digite a quantidade de numéros aleatórios: ")) 
soma = 0
print()
for i in range(quantidade_n_aleatorios):
    valor = random.randint(0, 100)        # Gerar números aleatórios entre 0 e 100
    soma += valor
    print(valor)
raiz_quadrada = math.sqrt(soma)           # Calcular a raiz quadrada da soma
raiz_quadrada = round(raiz_quadrada, 2)   # Arredondar para 2 casas decimais
print()
print("A raiz quadrada da soma dos valores é:", raiz_quadrada)
print()
