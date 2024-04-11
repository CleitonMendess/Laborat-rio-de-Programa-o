def converter_tempo(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    
    tempo_formatado = f"{horas} Horas {minutos} Minutos {segundos_restantes} segundos"
    return tempo_formatado

segundos = int(input("Informe a quantidade de segundos: "))
tempo_formatado = converter_tempo(segundos)
print("Tempo formatado:", tempo_formatado)