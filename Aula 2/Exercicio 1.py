def numeroInt(numero):
    if numero > 0:
        return True #isso é para que retorne um valor lógico invés de apenas imprimer "print('False ou True')"
    else:
        return False
numero = int(input('Digite um número: '))
print(numeroInt(numero))