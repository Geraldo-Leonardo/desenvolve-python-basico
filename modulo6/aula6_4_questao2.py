
frase = input("Digite uma frase: ")

vogais = sorted([letra for letra in frase if letra.lower() in 'aeiou'])
consoantes = [letra for letra in frase if letra.isalpha() and letra.lower() not in 'aeiou']
print()
print("\nAs vogais são: ", vogais)
print("\nAs consoantes são: ", consoantes)
print()