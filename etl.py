import csv

file_path = 'vendas.csv'

""" Funcão para ler um arquivo CSV e retornar uma lista de dicionários """

def ler_csv(file_path: str) -> list[dict]:
    lista = []
    with open(file_path, 'r',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            lista.append(row)
    return lista      


""" filtrar produtos da categoria Electronics """

def filtrar_produtos(produtos: list[dict]) -> list[dict]:
    produtos_filtrados = []
    for produto in produtos:
        if produto['Categoria'] == 'Electronics':
            produtos_filtrados.append(produto)
    return produtos_filtrados

""" Somar o total de vendas de produtos da categoria Electronics """
def somar_produtos(produtos: list[dict]) -> float:
    valor_total = 0
    for produto in produtos:
        if produto['Categoria'] == 'Electronics':
            valor_total += float(produto['Venda'])
    return valor_total

lista_produtos = ler_csv(file_path)
produtos_entregues = filtrar_produtos(lista_produtos)
soma = somar_produtos(produtos_entregues)
print(soma)
