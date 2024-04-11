def numePerfeito(numero):
    somaDivisor = 0
    divisor = 1
    while divisor < numero:
        if numero % divisor == 0:
            somaDivisor += divisor 
            divisor += 1
    return somaDivisor == numero
numero = int(input("Digite um número inteiro positivo: "))
if numePerfeito(numero):
    print(f"{numero} é um número perfeito.")
else:
    print(f"{numero} não é um número perfeito.")