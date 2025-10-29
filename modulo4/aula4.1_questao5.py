"""
Um instituto realizou uma pesquisa de público e precisa calcular a média de 
idade dos respondentes. Escreva um programa que leia um inteiro N com a 
quantidade de respondentes e em seguida leia as N idades de cada respondente. 
Ao final, imprima a média das idades.

(idade1 + idade2 + idade3 + … + idade_n)/N
"""
Numero_respondentes = int(input("Digite a quantidade de respondentes: "))
soma_idades = 0
for i in range(Numero_respondentes):
    idade_respondentes = int(input(f"Digite a idade do respondente {i + 1}: "))
    soma_idades += idade_respondentes
    media_idades = soma_idades / Numero_respondentes
print(f"A média das idades dos respondentes é: {media_idades:.2f}")
 