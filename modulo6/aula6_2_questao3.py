
import random

# Preenchendo as listas com valores aleatórios
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Encontrando a interseção
interseccao = list(set(lista1) & set(lista2))
interseccao.sort()

# Contando a quantidade de vezes que cada elemento aparece em cada lista
contagem_lista1 = {i: lista1.count(i) for i in interseccao}
contagem_lista2 = {i: lista2.count(i) for i in interseccao}

# Imprimindo os resultados
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Interseção das listas 1 e 2:", interseccao)
print("Contagem dos valores da interseção na Lista 1:", contagem_lista1)
print("Contagem dos valores da interseção na Lista 2:", contagem_lista2)