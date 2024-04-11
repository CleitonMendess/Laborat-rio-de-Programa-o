def recebeValor(valor):
    if valor % 2 == 0: # O operador % é usado para verificar o resto da divisão por 2. Se o resto for 0, então o número é par.
        return f'O valor é par'
    else:
        return f'O valor é ímpar'
valor = int(input('Digite um valor: '))
print(recebeValor(valor))
