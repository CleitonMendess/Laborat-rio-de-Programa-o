def func_insert(Lista, Lista2):
    for i in range(len(Lista2)):
        Lista.insert(i, Lista2[i])
    return Lista