
import random

num_elementos = random.randint(5, 20)
elementos = [random.randint(1, 10) for i in range(num_elementos)]

print("A lista elementos:", elementos)
print("A soma dos valores da lista:", sum(elementos))
print("A média dos valores da lista:", sum(elementos) / len(elementos))