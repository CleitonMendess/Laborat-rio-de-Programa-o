from func import meu_count
import random

tamanholista = 10
listaaleatoria =[random.randint(1, 5)for _ in range(tamanholista)]

resultado = meu_count(listaaleatoria, 1)
print(listaaleatoria, resultado)