"""
Exercício de maratona:  https://www.beecrowd.com.br/judge/pt/problems/view/1094

Maria precisa de sua ajuda para organizar os experimentos de seu laboratório. 
Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório 
e o percentual de cada tipo de cobaia utilizada. Este laboratório utiliza três 
tipos de cobaias: sapos, ratos e coelhos. 
Entrada: A primeira linha de entrada é um inteiro N com a quantidade de experimentos 
registrados. As N linhas seguintes contém um inteiro Quantia que representa a 
quantidade de cobaias utilizadas e um caractere Tipo ('S', 'R' ou 'C') com o tipo 
de cobaia (S:Sapo, R:Rato ou C:Coelho).

Saída: Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia e o 
percentual de cada uma em relação ao total de cobaias utilizadas
"""
total_experimentos = int(input("Digite a quantidade de experimentos registrados: "))
total_cobaias = 0 
total_sapos = 0
total_ratos = 0
total_coelhos = 0
for i in range(total_experimentos):
    quantidade = int(input("Quantidade de cobaias: "))
    tipo = input("Tipo de cobaias: ")
    total_cobaias += quantidade
    if tipo == 'S' or tipo == 's':
        total_sapos += quantidade
    elif tipo == 'R' or tipo == 'r':
        total_ratos += quantidade
    elif tipo == 'C' or tipo == 'c':
        total_coelhos += quantidade
print(f'Total: {total_cobaias} cobaias')
print(f'Total de coelhos: {total_coelhos}') 
print(f'Total de ratos: {total_ratos}')
print(f'Total de sapos: {total_sapos}')
percentual_coelhos = (total_coelhos / total_cobaias) * 100 if total_cobaias > 0 else 0
percentual_ratos = (total_ratos / total_cobaias) * 100 if total_cobaias > 0 else 0
percentual_sapos = (total_sapos / total_cobaias) * 100 if total_cobaias > 0 else 0  
print(f'Percentual de coelhos: {percentual_coelhos:.2f} %')
print(f'Percentual de ratos: {percentual_ratos:.2f} %')
print(f'Percentual de sapos: {percentual_sapos:.2f} %')

