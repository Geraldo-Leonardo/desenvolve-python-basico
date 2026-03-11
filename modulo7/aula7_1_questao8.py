
def calcular_digito_verificador(cpf_parcial):
    soma = 0
    multiplicador = len(cpf_parcial) + 1
    
   # print(multiplicador)

    for digito in cpf_parcial:
        soma += int(digito) * multiplicador
        multiplicador -= 1

        #print(cpf_parcial)
        #print(list[digito])
        #print(multiplicador)

    resto = soma % 11
    if resto < 2:
        return '0'
    else:
        return str(11 - resto)

def validar_cpf(cpf):
    cpf_numeros = cpf.replace('.', '').replace('-', '')
    cpf_parcial = cpf_numeros[:9]
    digito1 = calcular_digito_verificador(cpf_parcial)
    digito2 = calcular_digito_verificador(cpf_parcial + digito1)

    return cpf_numeros[-2:] == digito1 + digito2

cpf_input = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")
if validar_cpf(cpf_input):
    print()
    print("Válido")
    print()
else:
    print()
    print("\nInválido")
    print("\nO CPF deve estar no formato XXX.XXX.XXX-XX")
    print()

