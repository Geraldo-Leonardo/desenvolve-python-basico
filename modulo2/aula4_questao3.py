"""
3 - Você está desenvolvendo um programa para calcular o preço total de 
uma compra em uma loja online. O preço dos produtos é calculado 
multiplicando a quantidade pelo preço unitário. Escreva um programa em 
Python que solicite do usuário o nome, o preço unitário e a quantidade de 
3 produtos comprados e imprima ao final o preço total da compra. 
Note no exemplo a seguir que:

Cada entrada de dados tem uma mensagem indicando o dado solicitado 
(mensagens em itálico, dado de entrada em negrito)
A saída deve estar formatada exatamente como indicado (a string 
"Total: R$" e o preço com um separador de milhar e duas casas decimais).

Entrada
Digite o nome do produto 1:calça
Digite o preço unitário do produto 1:199.90
Digite a quantidade do produto 1: 3
Digite o nome do produto 2:camisa
Digite o preço unitário do produto 2:49.95
Digite a quantidade do produto 2:10
Digite o nome do produto 3:cinto
Digite o preço unitário do produto 3:25
Digite a quantidade do produto 3:3
Saída
Total: R$1,174.20
"""

produto1 = input("\033[3m Digite o nome do produto 1:\033[0m ") 
preco1 = float(input("\033[3m Digite o preço unitário do produto 1:\033[0m "))
quantidade1 = int(input("\033[3m Digite a quantidade do produto 1:\033[0m "))
produto2 = input("\033[3m Digite o nome do produto 2:\033[0m ")
preco2 = float(input("\033[3m Digite o preço unitário do produto 2:\033[0m "))
quantidade2 = int(input("\033[3m Digite a quantidade do produto 2:\033[0m "))
produto3 = input("\033[3m Digite o nome do produto 3:\033[0m ")
preco3 = float(input("\033[3m Digite o preço unitário do produto 3:\033[0m "))
quantidade3 = int(input("\033[3m Digite a quantidade do produto 3:\033[0m "))
total = (preco1 * quantidade1) + (preco2 * quantidade2) + (preco3 * quantidade3)
print(f"Total: R${total:,.2f}")

