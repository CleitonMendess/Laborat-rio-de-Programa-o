def tipo_triangulo(x, y, z):
    if x + y <= z or x + z <= y or y + z <= x:
        return "Não é um triângulo"
    elif x == y == z:
        return "Triângulo Equilátero"
    elif x == y or x == z or y == z:
        return "Triângulo Isósceles"
    else:
        return "Triângulo Escaleno"


x = float(input("Digite o comprimento do lado X: "))
y = float(input("Digite o comprimento do lado Y: "))
z = float(input("Digite o comprimento do lado Z: "))

tipo = tipo_triangulo(x, y, z)
print("Tipo de triângulo:", tipo)