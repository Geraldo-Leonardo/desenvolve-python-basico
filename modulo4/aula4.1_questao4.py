#Transforme em código o fluxograma a seguir
# Inicialize a variável maior com 0
# Solicite ao usuário que digite um número N
maior = 0
n = int(input("Digite um número N : "))
print("N:", n)
#
if n > 0:
    # repetir o laço while enquanto N for maior que 0
    while n > 0:
        x = int(input("Digite outro número X : "))
        x > maior
        #print("Maior =", maior)   # mostrar o valor de maior a cada iteração
        maior = x
        #print("x =", maior)       # mostrar o valor de x a cada iteração
        n = n - 1
        #print("n =", n)           # mostrar o valor de n a cada iteração
print("Maior:", maior)