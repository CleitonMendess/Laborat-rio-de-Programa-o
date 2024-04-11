def recebeValor(valor):
    if valor > 0:
        return f'O valor {valor} informado é possitivo'
    else:
        return  f'O valor {valor} informado é negativo'
valor = int(input('Digite um valor: '))
print(recebeValor(valor))