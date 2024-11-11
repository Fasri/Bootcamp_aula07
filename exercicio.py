#Calcular Média de Valores em uma Lista

# def media(lista:list[float]) ->float:
#     soma = 0
#     for n in lista:
#         soma = soma + n
#     media = soma / len(lista)
#     return media

# print(media([23,2,34,4,5]))


# Filtrar Dados Acima de um Limite

def filtrar(lista:list[float],limite:float) ->list[float]:
    lista_filtrada = []
    for n in lista:
        if n > limite:
            lista_filtrada.append(n)
    return lista_filtrada

print(filtrar([23,2,34,4,5],2))