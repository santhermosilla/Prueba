inventario = {
    "P001": [50, -10, -5, 20, -15],
    "P002": [30, -8, -12, 15],
    "P003": [100, -40, -30, -20],
}


def calcular_stock(lista_movimientos):
    stock_final = 0
    for valor in lista_movimientos:
        stock_final += valor
    return stock_final


for i in inventario:
    print(f"Producto {i}: Stock final = {calcular_stock(inventario[i])}")
print("hola")
