import random

frase = input("\nDigite uma frase: ")

def embaralhar_palavras(frase):
    palavras = frase.split()
    palavras_embaralhadas = []
    
    for palavra in palavras:
        if len(palavra) > 2:
            meio = list(palavra[1:-1])
            random.shuffle(meio)
            palavra_embaralhada = palavra[0] + ''.join(meio) + palavra[-1]
            palavras_embaralhadas.append(palavra_embaralhada)
        else:
            palavras_embaralhadas.append(palavra)
    
    return ' '.join(palavras_embaralhadas)

resultado = embaralhar_palavras(frase)
print('\nFrase embaralhada: ', resultado)
print()



 