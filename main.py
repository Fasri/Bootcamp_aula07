from etl import somar_produtos, filtrar_produtos, ler_csv

lista_produtos = ler_csv('vendas.csv')
produtos_entregues = filtrar_produtos(lista_produtos)
soma = somar_produtos(produtos_entregues)
print(soma)