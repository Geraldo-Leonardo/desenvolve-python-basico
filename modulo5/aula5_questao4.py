"""
Escreva um programa em Python que utiliza a biblioteca datetime para exibir a data e hora atuais com a 
formatação apresentada a seguir:

Data: 15/03/2023 

Hora: 14:05

Você pode consultar esse  tutorial da Alura sobre a biblioteca datetime. Existem várias maneiras 
de resolver essa questão. Uma sugestão é:
Função datetime.datetime.now() cujo retorno possui os atributos: day, month, year, hour, minute
Usar a formatação com f-strings no momento de imprimir. Atenção para os atributos que devem sempre ter 
2 dígitos precedidos por zero se necessário.
"""
import datetime
data_atual = datetime.datetime.now()
data_formatada = f"Data: {data_atual.day:02d}/{data_atual.month:02d}/{data_atual.year}"
hora_formatada = f"Hora: {data_atual.hour:02d}:{data_atual.minute:02d}"
print()
print(data_formatada)
print(hora_formatada)
print() 

