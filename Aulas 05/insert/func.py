def meu_insert(lista, indice, elemento):
    # Dividindo a lista em duas partes
    parte_anterior = lista[:indice]
    parte_posterior = lista[indice:]

    # Concatenando as partes com o elemento a ser inserido no meio
    lista[:] = parte_anterior + [elemento] + parte_posterior
    