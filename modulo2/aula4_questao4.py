"""
4 - Escreva um programa que leia um valor inteiro referente a uma quantia 
em reais e calcule a menor quantidade possível de notas necessárias para 
pagar aquele valor. As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. 
A saída deve estar formatada exatamente como indicado.

Entrada:  576

Saída       5 nota(s) de R$100,00
            1 nota(s) de R$50,00
            1 nota(s) de R$20,00
            0 nota(s) de R$10,00
            1 nota(s) de R$5,00
            0 nota(s) de R$2,00
            1 nota(s) de R$1,00
"""

# Leitura do valor inteiro
valor = int(input("Digite um valor inteiro : "))
# valor exemplo de entrada 576

# processamento começando da maior nota
notas_100 = valor // 100 # valor // 100 = 5 
#atualiza o valor depois de calcular a quantidade de notas de 100 conforme exemplo de entrada
valor = valor % 100      # valor % 100 = 76 # o resto da divisão

notas_50 = valor // 50   # valor // 50 = 1
valor = valor % 50      # valor % 50 = 26

notas_20 = valor // 20   # valor // 20 = 1
valor = valor % 20      # valor % 20 = 6

notas_10 = valor // 10   # valor // 10 = 0
valor = valor % 10      # valor % 6 

notas_5 = valor // 5   # valor // 5 = 1
valor = valor % 5      #  1

notas_2 = valor // 2   # valor // 2 = 0
valor = valor % 2      #  1

notas_1 = valor

print(f"{notas_100} nota(s) de 100")
print(f"{notas_50} nota(s) de 50")
print(f"{notas_20} nota(s) de 20")
print(f"{notas_10} nota(s) de 10")
print(f"{notas_5} nota(s) de 5")
print(f"{notas_2} nota(s) de 2")
print(f"{notas_1} nota(s) de 1")