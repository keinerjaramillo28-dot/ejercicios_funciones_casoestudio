#*******zona funcion********
def pedir_datos():
    cpu = float(input("uso de cpu"))
    return cpu
def procesar_cpu():
    alertas = 0
    mediciones = 0
    uso = pedir_datos()
    while uso >= 0:
        mediciones = mediciones + 1
        if uso > 80:
            print("alerta uso en mal estado")
            alertas = alertas + 1
            uso = pedir_datos()
            return alertas, mediciones
def mostrar_resultado(alertas, mediciones):
    print("total de mediciones", +str(mediciones))
    print("alerta aviso", +str(alertas))
    
#******codigo principal********

cpu = pedir_datos()
alertas, mediciones = procesar_cpu()
mostrar_resultado = (alertas, mediciones)

