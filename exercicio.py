#Calcular Média de Valores em uma Lista

# def media(lista:list[float]) ->float:
#     soma = 0
#     for n in lista:
#         soma = soma + n
#     media = soma / len(lista)
#     return media

# print(media([23,2,34,4,5]))


# Filtrar Dados Acima de um Limite

# def filtrar(lista:list[float],limite:float) ->list[float]:
#     lista_filtrada = []
#     for n in lista:
#         if n > limite:
#             lista_filtrada.append(n)
#     return lista_filtrada

# print(filtrar([23,2,34,4,5],2))

#Contar Valores Únicos em uma Lista

# def contar_unicos(lista:list[float]) ->int:
#     lista_unicos = []
#     for n in lista:
#         if n not in lista_unicos:
#             lista_unicos.append(n)
#     return len(lista_unicos)

# print(contar_unicos([23,2,5,4,5]))

#Converter Celsius para Fahrenheit em uma Lista

# def converter_celsius_fahrenheit(lista:list[float]) ->list[float]:
#     lista_fahrenheit = []
#     for n in lista:
#         fahrenheit = (n * 1.8) + 32
#         lista_fahrenheit.append(fahrenheit)
#     return lista_fahrenheit

# print(converter_celsius_fahrenheit([23,2,5,4,5]))

#Calcular Desvio Padrão de uma Lista

# def desvio_padrao(lista:list[float]) ->float:
#      media= sum(lista) / len(lista)
#      desvio = 0
#      for n in lista:
#          desvio += (n - media) ** 2
#      desvio = desvio / len(lista)
#      desvio = desvio ** 0.5
#      return desvio

# print(desvio_padrao([23,2,5,4,5]))

# Encontrar Valores Ausentes em uma Sequência

def encontrar_valores_ausentes(sequencia: list[int]) -> list[int]:
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - set(sequencia))

print(encontrar_valores_ausentes([23,2,5,4,5]))
