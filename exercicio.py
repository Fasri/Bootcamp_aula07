#Calcular Média de Valores em uma Lista

def media(lista):
    soma = 0
    for n in lista:
        soma = soma + n
    media = soma / len(lista)
    return media

print(media([23,2,34,4,5]))