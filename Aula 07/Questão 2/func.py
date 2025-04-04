def verifica_parentesco(frase):
    palavras = frase.split()  
    ultima_palavra = palavras[-1].lower()  
    
    if ultima_palavra == 'junior' or ultima_palavra == 'filho' or ultima_palavra == 'neto' or ultima_palavra == 'sobrinho':
        return True
    else:
        return False