
numeros = []

while True:
    entrada = input("Digite um número inteiro (ou 'sair' para finalizar): ")
    if entrada == 'sair':
        if len(numeros) >= 4:
            break
        else:
            print("Por favor, insira pelo menos 4 números antes de sair.")
            continue
    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
print()
print("Lista original:", numeros)
print("Os 3 primeiros elementos:", numeros[:3])
print("Os 2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Elementos de índice par:", numeros[::2])
print("Elementos de índice ímpar:", numeros[1::2])
print()