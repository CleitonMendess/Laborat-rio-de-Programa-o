def idadePessoa(anos,meses,dias):
    totalDias = ((anos * 360) + (meses * 30) + dias )
    return totalDias
dias = int(input('Quantos dias? '))
anos = int(input('Quantos anos? '))
meses = int(input('Quantos meses? '))
idadeFinal = idadePessoa(anos, meses, dias)
print(f'A pessoa viveu exatamente {idadeFinal} de dias na terra')