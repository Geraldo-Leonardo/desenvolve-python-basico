
# Função para receber uma lista de números do usuário
def receber_lista(nome_lista):
    lista = []
    quantidade = int(input(f"Quantos números você deseja adicionar à {nome_lista}? "))
    for i in range(quantidade):
        numero = int(input(f"Digite o número {i + 1} da {nome_lista}: "))
        lista.append(numero)
    return lista

# Função para combinar duas listas de forma alternada
def combinar_listas(lista1, lista2):
    lista_combinada = []
    for i in range(max(len(lista1), len(lista2))):
        if i < len(lista1):
            lista_combinada.append(lista1[i])
        if i < len(lista2):
            lista_combinada.append(lista2[i])
    return lista_combinada

# Recebendo as duas listas do usuário
lista1 = receber_lista("Lista 1")
lista2 = receber_lista("Lista 2")

# Combinando as listas
lista_combinada = combinar_listas(lista1, lista2)

# Exibindo o resultado
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista combinada:", lista_combinada)