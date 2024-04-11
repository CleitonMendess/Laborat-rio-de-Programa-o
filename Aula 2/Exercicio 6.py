def ordenar_em_ordem_crescente(valor1, valor2, valor3):
    lista_valores = [valor1, valor2, valor3]  # Colocando os valores em uma lista
    lista_valores.sort()  # Ordenando os valores em ordem crescente
    valores_string = [str(valor) for valor in lista_valores]  # Convertendo os valores para strings
    valores_separados_por_virgula = ",".join(valores_string)  # Juntando as strings com vírgula
    return valores_separados_por_virgula  # Retornando a string resultante

# Exemplo de uso da função
valor1 = int(input("Digite o primeiro valor inteiro: "))
valor2 = int(input("Digite o segundo valor inteiro: "))
valor3 = int(input("Digite o terceiro valor inteiro: "))

valores_ordenados = ordenar_em_ordem_crescente(valor1, valor2, valor3)
print("Valores ordenados em ordem crescente:", valores_ordenados)
