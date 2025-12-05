#*********zona funcion******
def pedir_producto():
    producto =int(input("que producto lleva:"))
    return producto
def cantidad_pedidos(producto):
    pedidos = int(input("digite la cantidad de pedidos"))
    return pedidos
def prosesar_datos(pedidos):
    c = 0
    for i in range (pedidos):
        calificacion = int(input("del 1 al 5 que calificacion le da al pedido"))
        if calificacion==5:
            print("excelente")
        c=c+calificacion
        sum=c
        return sum
def hacer_calculo(sum, pedidos):
    prom = sum / pedidos
    return prom
def mostrar_resultado(prom):
    print("el promedio es:"+ str(prom))
    
#********zona codigo******
producto = pedir_producto()
pedidos = cantidad_pedidos(producto)
sum = prosesar_datos(pedidos)
prom = hacer_calculo(producto, pedidos)
mostrar_resultado(prom)

    
    