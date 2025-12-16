#*******zona funcion*******
def pedir_pedido():
    pedido = int(input("que pedidos deseas llevar"))
    return pedido
def pedir_cantidad():
    cantida = int(input("que pedido llevas"))
    return cantida
def procesar_datos():
    total = 0
    contador = 0
    for n in range(cantida):
        print ("califiacar el pedido")
        calificar = int(input("del 1 al 5"))
        if calificar > 5:
            calificar = 5
        if calificar < 1:
            calificar = 1
        if calificar == 5:
            print("excelente")
        total = total + calificar
        contador = contador + 1
        return total, contador
    def calcular_pedido(total, contador):
        if contador > 0:
            promedio = total / contador
        else:
            promedio = 0
        return promedio
    def mostar_resulado(promedio):
        print("el promedio es:", +str(promedio))
        
    
    #*****codigo principal********
    
    pedido  = pedir_pedido()
    cantida = pedir_cantidad()
    total, contador = procesar_datos(cantida)
    promedio = calcular_pedido(total, contador)
    mostar_resulado(promedio)
    
    