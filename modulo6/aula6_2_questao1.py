
import random


# Gerar 20 valores inteiros aleatórios entre -100 e 100
lista_original = [random.randint(-100, 100) for i in range(20)]

# Criar uma cópia da lista original e ordená-la
lista_ordenada = sorted(lista_original)

# Encontrar os índices do maior e menor valor na lista original
indice_maior = lista_original.index(max(lista_original))
indice_menor = lista_original.index(min(lista_original))

# Imprimir os resultados
print("Lista ordenada:", lista_ordenada)
print("Lista original:", lista_original)
print("Índice e o valor do maior número da lista original: ")
print('Indice:', indice_maior, ', valor:', max(lista_original))
print("Índice e o valor do menor número da lista original: ")
print('Indice:', indice_menor, ', valor:', min(lista_original))
