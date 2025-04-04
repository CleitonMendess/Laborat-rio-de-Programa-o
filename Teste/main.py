#listas 
lista_nomes = []
lista_salarios = []

#dados dos funcionários
nome_funcionario = input('Qual é o nome do funcionário? ')
while nome_funcionario != '0':
    salario_funcionario = float(input('Qual é o salário do funcionário? '))
    lista_nomes.append(nome_funcionario)
    lista_salarios.append(salario_funcionario)
    
    nome_funcionario = input('Qual é o nome do funcionário? ')

#calculo do abono
total_abono = 0
numero_minimo = 0
maior_abono = 0
abonos_acima_da_media = 0

for i in range(len(lista_nomes)):
    nome = lista_nomes[i]
    salario = lista_salarios[i]
    abono = salario * 0.20 if salario * 0.20 >= 100 else 100
    total_abono += abono
    if abono == 100:
        numero_minimo += 1
    if abono > maior_abono:
        maior_abono = abono

total_gasto = sum(lista_salarios) + total_abono
media_abono = total_abono / len(lista_nomes)

#print resultados
print("\nProjeção de Gastos com Abono")

print("Colaborador   Salário   Abono")
print("-----------   -------   -----")

for i in range(len(lista_nomes)):
    nome = lista_nomes[i]
    salario = lista_salarios[i]
    abono = salario * 0.20 if salario * 0.20 >= 100 else 100
    print(f"{nome}   R$ {salario:.2f}   R$ {abono:.2f}")

print("--------------   -------   ----------")
print(f"Total   R$ {sum(lista_salarios):.2f}   R$ {total_abono:.2f}")
print(f"Foram processados {len(lista_nomes)} colaboradores")
print(f"Total gasto com salários e abonos: R$ {total_gasto:.2f}")
print(f"Valor mínimo pago a {numero_minimo} colaboradores")
print(f"Maior abono pago a {maior_abono:.2f}")
print(f"Média do abono salarial: R$ {media_abono:.2f}")

for i in range(len(lista_salarios)):
    if lista_salarios[i] > media_abono:
        abonos_acima_da_media += 1

print(f"Foram pagos abonos acima da média a {abonos_acima_da_media} colaboradores.")
