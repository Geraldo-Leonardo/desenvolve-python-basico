#Transforme em código o fluxograma a seguir

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
media = (n1 + n2 + n3) / 3
print(f"Média:  {media:.2f}")
if media >= 60:
    print("Aprovado")
elif media >= 40:
    print("Recuperação")
else:
    print("Reprovado") 
print('Fim')    