def somaCpf(cpf):
    soma = 0
    cpf = cpf.replace('.', '-')  # Substitui pontos por traços
    cpf = cpf.split('-')  # Divide o CPF em partes separadas pelo traço
    for i in cpf:
        soma += int(i)
    return soma