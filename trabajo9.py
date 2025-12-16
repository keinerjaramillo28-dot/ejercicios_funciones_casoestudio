#*************zona funcion**********
stock_inicial = 70
punto_repositorio = 20
stock_actual = stock_inicial

print("stock inicial {stock_actual}unidades")
print("punto de punto_repositorio{punto_repositorio}unidadees")
while True:
    try:
        cantidad_vendida = int(input("ingresa cantidad vendidad"))
        if cantidad_vendida == 0:
            print("finalizar proceso")
            break
        if cantidad_vendida > stock_actual:
            print("error no hay")
            continue
        stock_actual -= cantidad_vendida
        print("venta registrada {cantidad_vendida} unidades")
        print("stock actual {stock_actual} unidades")
        
        if stock_actual <= punto_repositorio:
            print(" aviso de repositorio")
            print("el stock ({stock_actual}unidades)")
            print(" se detiene el proceso de ventas")
            break
    except ValueError:
        print("por favor ingrese un numero valido")
                
        
       