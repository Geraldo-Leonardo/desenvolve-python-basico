
# Solução
data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")
# Separar o dia, mês e ano
dia, mes, ano = data_nascimento.split("/")
# Lista com os nomes dos meses
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
# Obter o nome do mês usando o índice (mes - 1) pois a lista começa em 0
nome_mes = meses[int(mes) - 1]
# Imprimir a data com o nome do mês por extenso
print(f"Você nasceu em {dia} de {nome_mes} de {ano}.")
