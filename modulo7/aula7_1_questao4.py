
numero = input("\nDigite um número de celular : ")
if len(numero) == 8:
    numero = "9" + numero
elif len(numero) == 9 and numero[0] != "9":
    numero = "9" + numero
numero = numero[:5] + "-" + numero[5:]
print("\nNúmero do celular completo:", numero)
print()