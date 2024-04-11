def calcular_media(nota1, nota2, nota3, tipo_media):
    if tipo_media == 'A':  # Calcular média aritmética
        media = (nota1 + nota2 + nota3) / 3
    elif tipo_media == 'P':  # Calcular média ponderada
        media = (nota1 * 5 + nota2 * 3 + nota3 * 2) / (5 + 3 + 2)
    else:
        return "Tipo de média inválido. Escolha 'A' para média aritmética ou 'P' para média ponderada."
    return media

# Solicita as notas e o tipo de média ao usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
tipo = input("Digite 'A' para média aritmética ou 'P' para média ponderada: ")

# Chamada da função para calcular a média
media_final = calcular_media(nota1, nota2, nota3, tipo)
print("A média do aluno é:", media_final)
