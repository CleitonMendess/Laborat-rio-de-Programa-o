def pesoIdeal(altura, sexo):
    if sexo == 'M':
        pesoHomem = (72.7 * altura / 100) - 58
        return pesoHomem
    elif sexo == 'F':
        pesoMulher = (62.1 * altura / 100) - 44.7
        return pesoMulher

sexo = input('Informe o sexo desejado: ')
altura = int(input('Informe sua altura em metros: '))
imc = pesoIdeal(altura, sexo)
if imc:
    print(f'Pessoal ideia para uma pessoa de sexo {sexo} e que mede {altura} é de {imc: .2f}')      