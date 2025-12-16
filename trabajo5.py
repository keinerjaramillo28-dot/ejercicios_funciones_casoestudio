#********zona funcion***********
def pedir_precio():
    precio = float(input("precio del producto"))
    return precio
def pedir_cantidad():
    cantidad = int(input("cantidad: "))
    return cantidad
def procesar_datos():
    subtotal = 0
    seguir = input("agregar otro producto si/no")
    return subtotal
def calcular_descuento(subtotal):
    if subtotal > 2000:
        descuento = subtotal * 0.20
    else:
        if subtotal > 1000:
            descuento = subtotal *0.10
        else:
            descuento = 0
            total = subtotal - descuento
            return total, descuento
def mostrar_resultado(total, descuento):
    print("descuento aplicado", +str(descuento))
    print("monto final", +str(total))
    
#*******+codigo principal*******++
precio = pedir_precio()
cantidad = pedir_cantidad()
subtotal = procesar_datos()
total, descuento = calcular_descuento(subtotal)
mostrar_resultado(total, subtotal)

        