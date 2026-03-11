
def is_palindrome(frase):
    # Remove espaços em branco e ponto, e converte para minúsculas
    frase = ''.join(palavras for palavras in frase if palavras.isalnum()).lower()
    # Exibir a frase para verificação 
    #print(frase)
    # Verifica se a frase limpa é igual à sua reversa
    return frase == frase[::-1]
 

while True:
    frase_usuario = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase_usuario.lower() == 'fim':
        break
    if is_palindrome(frase_usuario):
        print(f'"{frase_usuario}" é palíndromo\n')
    else:
        print(f'"{frase_usuario}" não é palíndromo\n')
