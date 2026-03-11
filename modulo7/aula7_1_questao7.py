
import random

def encrypt(nomes):
    chave_aleatoria = random.randint(1, 10)
    nomes_criptografados = []

    for nome in nomes:
        nome_criptografado = ''.join(chr((ord(c) - 33 + chave_aleatoria) % 94 + 33) for c in nome)
        nomes_criptografados.append(nome_criptografado)

    return nomes_criptografados, chave_aleatoria

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
print("\nNomes Originais:", nomes)
nomes_criptografados, chave = encrypt(nomes)

print("\nNomes Criptografados:", nomes_criptografados)
print("\nChave de Criptografia:", chave)
print()

""" Função para descriptografar os nomes usando a chave fornecida """
"""
def desencrypt(nomes_criptografados, chave):
    nomes_descriptografados = []

    for nome in nomes_criptografados:
        nome_descriptografado = ''.join(chr((ord(c) - 33 - chave) % 94 + 33) for c in nome)
        nomes_descriptografados.append(nome_descriptografado)

    return nomes_descriptografados

print("\nNomes Descriptografados:", desencrypt(nomes_criptografados, chave))
"""