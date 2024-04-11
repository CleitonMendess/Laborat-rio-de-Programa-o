# definimos uma função que aceita dois argumentos: o iterável (como uma lista) e o elemento que queremos contar.
#Iteramos sobre o iterável e incrementamos um contador sempre que encontramos o elemento desejado.
def meu_count(iteravel, elemento):
    count = 0
    for intem in iteravel:
        if intem == elemento:
            count += 1
    return count 