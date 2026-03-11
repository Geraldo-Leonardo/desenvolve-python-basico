
import re

senha = input("Digite a senha para validação: ")

def validador_senha(senha):
    
    if len(senha) < 8:
        return False
    if not re.search(r'[A-Z]', senha):
        return False
    if not re.search(r'[a-z]', senha):
        return False
    if not re.search(r'[0-9]', senha):
        return False
    if not re.search(r'[@#$/#%]', senha):
        return False
    return True

print(validador_senha(senha))
