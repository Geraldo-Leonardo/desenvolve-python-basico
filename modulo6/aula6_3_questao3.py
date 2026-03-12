
import random

# Criação da lista com 20 elementos aleatórios entre -10 e 10
lista = [random.randint(-10, 10) for i in range(20)]
print()
print("Lista original:", lista)
print()
# Encontrar o intervalo com a maior quantidade de números negativos
maior_intervalo = 0
atual_intervalo = 0
inicio = 0

for i in range(len(lista)):
    if lista[i] < 0:
        atual_intervalo += 1
    else:
        if atual_intervalo > maior_intervalo:
            maior_intervalo = atual_intervalo
            inicio = i - atual_intervalo
        atual_intervalo = 0
# Verificar o último intervalo
if atual_intervalo > maior_intervalo:
    maior_intervalo = atual_intervalo
    inicio = len(lista) - atual_intervalo

# Deletar o intervalo da lista
del lista[inicio:inicio + maior_intervalo]
print("Lista editada :", lista)
print()