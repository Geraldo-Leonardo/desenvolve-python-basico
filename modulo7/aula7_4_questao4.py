

import random

def imprime_enforcado(erros):

    if erros == 1:
        print('\n    |----|\n\n    |    O\n\n    |\n\n    |\n\n ==========')

    elif erros == 2:
        print('\n    |----|\n\n    |    O\n\n    |    |\n\n    |\n\n ==========')

    elif erros == 3:
        print('\n    |----|\n\n    |    O\n\n    |   /|\n\n    |\n\n ==========')

    elif erros == 4:
        print('\n    |----|\n\n    |    O\n\n    |   /|\\\n\n    |\n\n ==========')

    elif erros == 5:
        print('\n    |----|\n\n    |    O\n\n    |   /|\\\n\n    |   /\n\n ==========')

    elif erros == 6:
        print('\n    |----|\n\n    |    O\n\n    |   /|\\\n\n    |   / \\\n\n ==========')

def main():
    with open("gabarito_forca.txt", "r") as arquivo:
        palavras = arquivo.read().splitlines()
    
    palavra_secreta = random.choice(palavras)
    letras_adivinhadas = set()
    erros = 0

    print('\n  JOGO DA FORCA\n\n    |----|\n\n    |\n\n    |\n\n    |\n\n ==========')

    while erros < 6:
        display_palavra = " ".join([letra if letra in letras_adivinhadas else "_" for letra in palavra_secreta])
        print()
        print(display_palavra)

        if "_" not in display_palavra:
            print()
            print("\n     Parabéns!\nVocê acertou a palavra!\n")
            break

        letra = input("Digite uma letra: ").lower()

        if letra in palavra_secreta:
            letras_adivinhadas.add(letra)
        else:
            erros += 1
            imprime_enforcado(erros)

        if erros == 6:
            print(f"\n    Game Over!\nA palavra era: {palavra_secreta}\n")

if __name__ == "__main__":
    main()
