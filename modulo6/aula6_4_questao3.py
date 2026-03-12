
# Lista com as horas trabalhadas por cada funcionário na semana
horas_trabalhadas = [40, 37, 45, 40, 40, 48]

# Definindo os valores de ganho por hora e hora extra
ganho_por_hora = 20
print('\nValor da hora trabalhada: ', ganho_por_hora)
hora_extra = 25
print('\nValor da hora extra: ', hora_extra)

# Calculando os pagamentos
pagamentos = [ganho_por_hora * min(hora, 40) + hora_extra * max(0, hora-40) for hora in horas_trabalhadas]
print("\nhoras_trabalhadas:", horas_trabalhadas)
print('\nValores de pagamentos:', pagamentos)
print()