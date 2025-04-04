def frase_em_maiusculas(frase):
    frase_maiuscula = ""
    for letra in frase:
        frase_maiuscula += letra.upper()
    return frase_maiuscula

frase = "Esta é uma frase de exemplo."
resultado = frase_em_maiusculas(frase)
print(resultado)  